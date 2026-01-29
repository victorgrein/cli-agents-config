#!/usr/bin/env python3
"""
Script to convert OpenCode agents to shared base format.
"""

import re
import yaml
from pathlib import Path

# Tool mapping from OpenCode format to base format
TOOL_MAP = {
    'read': 'Read',
    'write': 'Write', 
    'edit': 'Edit',
    'grep': 'Grep',
    'glob': 'Glob',
    'bash': 'Bash',
    'task': 'Task',
    'skill': 'Skill',
}

# Skill mapping based on agent name
SKILL_MAP = {
    'agent-designer': ['crewai-agents'],
    'task-designer': ['crewai-tasks'],
    'crew-architect': ['crewai-crews', 'crewai-agents', 'crewai-tasks'],
    'flow-engineer': ['crewai-flows', 'crewai-crews'],
    'tool-specialist': ['crewai-tools'],
    'debugger': ['crewai-debugging'],
    'llm-optimizer': ['crewai-llms', 'crewai-optimization'],
    'migration-specialist': ['crewai-migration', 'crewai-project-structure'],
    'performance-analyst': ['crewai-optimization', 'crewai-llms'],
    'crewai-documenter': ['crewai-project-structure', 'crewai-code-quality'],
    'coder-agent': [],
    'reviewer': ['crewai-code-quality'],
    'tester': [],
    'build-agent': [],
}


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].lstrip('\n')
        return frontmatter or {}, body
    except yaml.YAMLError:
        return {}, content


def convert_tools(tools_dict: dict) -> list[str]:
    """Convert OpenCode tools format to base format."""
    result = []
    for tool, enabled in tools_dict.items():
        if enabled and tool in TOOL_MAP:
            result.append(TOOL_MAP[tool])
    return result


def create_base_frontmatter(original: dict, agent_name: str) -> dict:
    """Create base format frontmatter from original."""
    base = {
        'name': original.get('id', agent_name),
        'description': original.get('description', ''),
    }
    
    # Convert tools
    if 'tools' in original and isinstance(original['tools'], dict):
        base['tools'] = convert_tools(original['tools'])
    
    # Add skills
    if agent_name in SKILL_MAP and SKILL_MAP[agent_name]:
        base['skills'] = SKILL_MAP[agent_name]
    
    # Model
    base['model'] = 'inherit'
    
    return base


def clean_body(body: str) -> str:
    """Clean the body - remove OpenCode-specific skill loading instructions."""
    # Remove skill loading instruction lines
    lines = body.split('\n')
    cleaned_lines = []
    for line in lines:
        # Skip lines that reference old context paths
        if '.opencode/context/' in line:
            continue
        # Modify skill loading instruction
        if "skill tool to load" in line:
            # Extract skill name and simplify
            match = re.search(r"'([^']+)'", line)
            if match:
                skill_name = match.group(1)
                line = f"  <instruction>Load the {skill_name} skill for reference</instruction>"
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)


def format_frontmatter(data: dict) -> str:
    """Format frontmatter as YAML."""
    return '---\n' + yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False) + '---\n\n'


def convert_agent(source_path: Path, dest_path: Path):
    """Convert a single agent file."""
    content = source_path.read_text()
    frontmatter, body = parse_frontmatter(content)
    
    agent_name = source_path.stem
    base_frontmatter = create_base_frontmatter(frontmatter, agent_name)
    cleaned_body = clean_body(body)
    
    result = format_frontmatter(base_frontmatter) + cleaned_body
    
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(result)
    print(f"Converted: {source_path} -> {dest_path}")


def main():
    base_dir = Path('/root/crewai/opencode')
    
    # Convert CrewAI agents
    crewai_source = base_dir / 'agent/subagents/crewai'
    crewai_dest = base_dir / 'templates/shared/agents/crewai'
    
    for source_file in crewai_source.glob('*.md'):
        dest_file = crewai_dest / source_file.name
        convert_agent(source_file, dest_file)
    
    # Convert Code agents
    code_source = base_dir / 'agent/subagents/code'
    code_dest = base_dir / 'templates/shared/agents/code'
    
    for source_file in code_source.glob('*.md'):
        dest_file = code_dest / source_file.name
        convert_agent(source_file, dest_file)
    
    print("\nConversion complete!")


if __name__ == '__main__':
    main()
