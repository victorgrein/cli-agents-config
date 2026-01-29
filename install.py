#!/usr/bin/env python3
"""
CrewAI Skills Installer for Claude Code and OpenCode

This installer allows you to install CrewAI development skills, agents, and workflows
to either Claude Code or OpenCode projects.

Usage:
    python install.py                           # Interactive mode
    python install.py --platform claude --package standard
    python install.py --platform opencode --package full
    python install.py --dry-run --platform claude --package minimal
"""

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)


# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_header(text: str):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text:^60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 60}{Colors.ENDC}\n")


def print_success(text: str):
    print(f"{Colors.GREEN}✓ {text}{Colors.ENDC}")


def print_warning(text: str):
    print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")


def print_error(text: str):
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")


def print_info(text: str):
    print(f"{Colors.CYAN}ℹ {text}{Colors.ENDC}")


def get_script_dir() -> Path:
    """Get the directory where this script is located."""
    return Path(__file__).parent.resolve()


def load_packages() -> dict:
    """Load package definitions from packages.json."""
    packages_file = get_script_dir() / "packages.json"
    with open(packages_file) as f:
        return json.load(f)


def detect_existing_installation(target_dir: Path) -> Optional[str]:
    """Detect if there's an existing Claude Code or OpenCode installation."""
    claude_dir = target_dir / ".claude"
    opencode_dir = target_dir / ".opencode"
    
    if claude_dir.exists():
        return "claude"
    elif opencode_dir.exists():
        return "opencode"
    return None


def prompt_platform() -> str:
    """Prompt user to select platform."""
    print(f"{Colors.BOLD}Select platform:{Colors.ENDC}")
    print("  [1] Claude Code")
    print("  [2] OpenCode")
    
    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()
        if choice == "1":
            return "claude"
        elif choice == "2":
            return "opencode"
        print_error("Invalid choice. Please enter 1 or 2.")


def prompt_package(packages: dict) -> str:
    """Prompt user to select package."""
    print(f"\n{Colors.BOLD}Select package:{Colors.ENDC}")
    for i, (name, pkg) in enumerate(packages["packages"].items(), 1):
        recommended = " (recommended)" if name == "standard" else ""
        print(f"  [{i}] {name}{recommended}")
        print(f"      {Colors.CYAN}{pkg['description']}{Colors.ENDC}")
    
    package_names = list(packages["packages"].keys())
    while True:
        choice = input("\nEnter choice (1-3): ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(package_names):
                return package_names[idx]
        except ValueError:
            pass
        print_error(f"Invalid choice. Please enter 1-{len(package_names)}.")


def prompt_install_mode(platform: str) -> str:
    """Prompt user to choose install or update mode when existing installation detected."""
    config_dir = ".claude" if platform == "claude" else ".opencode"
    print(f"\n{Colors.WARNING}Existing {platform} installation detected ({config_dir}){Colors.ENDC}")
    print(f"\n{Colors.BOLD}Choose action:{Colors.ENDC}")
    print(f"  [1] {Colors.GREEN}Add{Colors.ENDC} - Add new files, keep customized files")
    print(f"  [2] {Colors.CYAN}Update{Colors.ENDC} - Overwrite all files with latest versions")
    
    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()
        if choice == "1":
            return "add"
        elif choice == "2":
            return "update"
        print_error("Invalid choice. Please enter 1 or 2.")


def get_package_contents(packages: dict, package_name: str) -> dict:
    """Get the full contents of a package, including inherited items."""
    pkg = packages["packages"][package_name]
    result = {
        "skills": list(pkg.get("skills", [])),
        "agents": list(pkg.get("agents", [])),
        "workflows": list(pkg.get("workflows", [])),
        "commands": list(pkg.get("commands", []))
    }
    
    # Handle inheritance
    if "extends" in pkg:
        parent = get_package_contents(packages, pkg["extends"])
        for key in result:
            result[key] = parent[key] + result[key]
    
    return result


def compute_file_hash(filepath: Path) -> str:
    """Compute MD5 hash of a file."""
    if not filepath.exists():
        return ""
    return hashlib.md5(filepath.read_bytes()).hexdigest()


def is_file_customized(source: Path, target: Path, hashes_file: Path) -> bool:
    """Check if a file has been customized by the user."""
    if not target.exists():
        return False
    
    # Load stored hashes
    hashes = {}
    if hashes_file.exists():
        with open(hashes_file) as f:
            hashes = json.load(f)
    
    # Get stored original hash
    target_key = str(target)
    original_hash = hashes.get(target_key)
    
    if original_hash is None:
        # No record of original, assume customized if different from source
        return compute_file_hash(target) != compute_file_hash(source)
    
    # Compare current hash with original
    current_hash = compute_file_hash(target)
    return current_hash != original_hash


def store_file_hash(target: Path, hashes_file: Path):
    """Store the hash of a file for future comparison."""
    hashes = {}
    if hashes_file.exists():
        with open(hashes_file) as f:
            hashes = json.load(f)
    
    hashes[str(target)] = compute_file_hash(target)
    
    hashes_file.parent.mkdir(parents=True, exist_ok=True)
    with open(hashes_file, 'w') as f:
        json.dump(hashes, f, indent=2)


def adapt_agent_for_claude(content: str) -> str:
    """Adapt agent file for Claude Code format."""
    if not content.startswith('---'):
        return content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return content
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].lstrip('\n')
    except yaml.YAMLError:
        return content
    
    # Create Claude Code format frontmatter
    claude_fm = {
        'name': frontmatter.get('name', ''),
        'description': frontmatter.get('description', ''),
    }
    
    # Convert tools list to comma-separated string
    tools = frontmatter.get('tools', [])
    if isinstance(tools, list) and tools:
        claude_fm['tools'] = ', '.join(tools)
    
    # Add skills if present
    skills = frontmatter.get('skills', [])
    if skills:
        claude_fm['skills'] = skills
    
    # Model
    model = frontmatter.get('model', 'inherit')
    if model != 'inherit':
        claude_fm['model'] = model
    
    # Format output
    yaml_str = yaml.dump(claude_fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{yaml_str}---\n\n{body}"


def adapt_agent_for_opencode(content: str) -> str:
    """Adapt agent file for OpenCode format."""
    if not content.startswith('---'):
        return content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return content
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].lstrip('\n')
    except yaml.YAMLError:
        return content
    
    # Tool name mapping
    tool_map = {
        'Read': 'read', 'Write': 'write', 'Edit': 'edit',
        'Grep': 'grep', 'Glob': 'glob', 'Bash': 'bash',
        'Task': 'task', 'Skill': 'skill'
    }
    
    # Create OpenCode format frontmatter
    opencode_fm = {
        'id': frontmatter.get('name', ''),
        'name': frontmatter.get('name', '').replace('-', ' ').title().replace(' ', ''),
        'category': 'subagents/crewai',
        'type': 'subagent',
        'version': '1.0.0',
        'author': 'crewai-skills',
        'description': frontmatter.get('description', ''),
        'mode': 'subagent',
        'temperature': 1.0,
    }
    
    # Convert tools
    tools = frontmatter.get('tools', [])
    if isinstance(tools, list):
        tools_dict = {}
        for tool in tools:
            tool_lower = tool_map.get(tool, tool.lower())
            tools_dict[tool_lower] = True
        # Add task: false by default for subagents
        tools_dict['task'] = False
        opencode_fm['tools'] = tools_dict
    
    # Add default permissions
    opencode_fm['permission'] = {
        'bash': {
            '*': 'deny',
            'ls *': 'allow',
            'cat *': 'allow',
            'head *': 'allow',
            'tail *': 'allow',
            'find *': 'allow',
            'grep *': 'allow',
            'pwd': 'allow',
            'tree *': 'allow'
        },
        'edit': 'ask'
    }
    
    # Format output
    yaml_str = yaml.dump(opencode_fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{yaml_str}---\n\n{body}"


def copy_with_merge(source: Path, target: Path, hashes_file: Path, 
                    dry_run: bool = False, force_update: bool = False) -> str:
    """Copy file with merge logic. Returns action taken.
    
    Args:
        source: Source file path
        target: Target file path
        hashes_file: Path to hashes JSON file
        dry_run: If True, don't actually copy files
        force_update: If True, overwrite existing files even if customized
    """
    if not target.exists():
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            store_file_hash(target, hashes_file)
        return "created"
    
    if force_update:
        # Force update mode: overwrite everything
        if not dry_run:
            shutil.copy2(source, target)
            store_file_hash(target, hashes_file)
        return "updated (overwritten)"
    
    if is_file_customized(source, target, hashes_file):
        # File was customized, create .new file
        new_path = target.with_suffix(target.suffix + '.new')
        if not dry_run:
            shutil.copy2(source, new_path)
        return f"skipped (customized, new version at {new_path.name})"
    
    # Not customized, update
    if not dry_run:
        shutil.copy2(source, target)
        store_file_hash(target, hashes_file)
    return "updated"


def install_skills(contents: dict, platform: str, target_dir: Path, 
                   hashes_file: Path, dry_run: bool = False, force_update: bool = False) -> list:
    """Install skills from /skills directory to target."""
    results = []
    script_dir = get_script_dir()
    
    # Skills source is /templates/shared/skills in the repository
    skills_source = script_dir / "templates" / "shared" / "skills"
    
    # Target depends on platform
    if platform == "claude":
        skills_target = target_dir / ".claude" / "skills"
    else:
        skills_target = target_dir / ".opencode" / "skills"
    
    for skill in contents["skills"]:
        source = skills_source / skill
        target = skills_target / skill
        
        if source.is_dir():
            # Copy entire skill directory
            for file in source.rglob("*"):
                if file.is_file():
                    rel_path = file.relative_to(source)
                    target_file = target / rel_path
                    action = copy_with_merge(file, target_file, hashes_file, dry_run, force_update)
                    results.append((f"skills/{skill}/{rel_path}", action))
        else:
            print_warning(f"Skill not found: {skill}")
    
    return results


def install_agents(contents: dict, platform: str, target_dir: Path,
                   hashes_file: Path, dry_run: bool = False, force_update: bool = False) -> list:
    """Install agents from /templates/shared/agents with platform adaptation."""
    results = []
    script_dir = get_script_dir()
    
    agents_source = script_dir / "templates" / "shared" / "agents"
    
    # Target depends on platform
    if platform == "claude":
        agents_target = target_dir / ".claude" / "agents"
    else:
        agents_target = target_dir / ".opencode" / "agent" / "subagents"
    
    for agent_path in contents["agents"]:
        # agent_path is like "crewai/crew-architect"
        parts = agent_path.split("/")
        category = parts[0] if len(parts) > 1 else ""
        agent_name = parts[-1]
        
        source = agents_source / category / f"{agent_name}.md"
        
        if platform == "claude":
            target = agents_target / f"{agent_name}.md"
        else:
            target = agents_target / category / f"{agent_name}.md"
        
        if source.exists():
            content = source.read_text()
            
            # Adapt for platform
            if platform == "claude":
                content = adapt_agent_for_claude(content)
            else:
                content = adapt_agent_for_opencode(content)
            
            action = "would install" if dry_run else "created"
            
            if not dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                
                # Check if customized (unless force_update)
                if target.exists() and not force_update and is_file_customized(source, target, hashes_file):
                    new_path = target.with_suffix('.md.new')
                    new_path.write_text(content)
                    action = f"skipped (new at {new_path.name})"
                else:
                    if target.exists():
                        action = "updated (overwritten)" if force_update else "updated"
                    target.write_text(content)
                    store_file_hash(target, hashes_file)
            
            results.append((f"agents/{agent_path}.md", action))
        else:
            print_warning(f"Agent not found: {agent_path}")
    
    return results


def install_workflows(contents: dict, platform: str, target_dir: Path,
                      hashes_file: Path, dry_run: bool = False, force_update: bool = False) -> list:
    """Install workflows from /templates/shared/workflows as skills."""
    results = []
    script_dir = get_script_dir()
    
    workflows_source = script_dir / "templates" / "shared" / "workflows"
    
    # Workflows are installed as skills
    if platform == "claude":
        skills_target = target_dir / ".claude" / "skills"
    else:
        skills_target = target_dir / ".opencode" / "skills"
    
    for workflow in contents["workflows"]:
        source = workflows_source / workflow
        target = skills_target / workflow
        
        if source.is_dir():
            for file in source.rglob("*"):
                if file.is_file():
                    rel_path = file.relative_to(source)
                    target_file = target / rel_path
                    action = copy_with_merge(file, target_file, hashes_file, dry_run, force_update)
                    results.append((f"workflows/{workflow}/{rel_path}", action))
        else:
            print_warning(f"Workflow not found: {workflow}")
    
    return results


def install_commands(contents: dict, platform: str, target_dir: Path,
                     hashes_file: Path, dry_run: bool = False, force_update: bool = False) -> list:
    """Install slash commands from /templates/shared/commands."""
    results = []
    script_dir = get_script_dir()
    
    # Commands are shared between platforms
    commands_source = script_dir / "templates" / "shared" / "commands"
    
    # Target depends on platform
    if platform == "claude":
        commands_target = target_dir / ".claude" / "commands"
    else:
        commands_target = target_dir / ".opencode" / "command"
    
    for cmd_path in contents["commands"]:
        # cmd_path is like "crew/create"
        source = commands_source / f"{cmd_path}.md"
        target = commands_target / f"{cmd_path}.md"
        
        if source.exists():
            action = copy_with_merge(source, target, hashes_file, dry_run, force_update)
            results.append((f"commands/{cmd_path}.md", action))
        else:
            print_warning(f"Command not found: {cmd_path}")
    
    return results


def install_system_prompt(platform: str, target_dir: Path,
                          hashes_file: Path, dry_run: bool = False, force_update: bool = False) -> list:
    """Install system prompt (CLAUDE.md) and settings for Claude Code only."""
    results = []
    script_dir = get_script_dir()
    
    # Only Claude Code gets CLAUDE.md and settings.json
    # OpenCode uses its own agent orchestrator instead
    if platform != "claude":
        return results
    
    platform_dir = script_dir / "templates" / "claude"
    config_dir = target_dir / ".claude"
    
    # Install CLAUDE.md (orchestrator for Claude Code)
    source = platform_dir / "CLAUDE.md"
    target = config_dir / "CLAUDE.md"
    
    if source.exists():
        action = copy_with_merge(source, target, hashes_file, dry_run, force_update)
        results.append(("CLAUDE.md", action))
    
    # Install settings.json
    settings_source = platform_dir / "settings.json"
    settings_target = config_dir / "settings.json"
    if settings_source.exists():
        action = copy_with_merge(settings_source, settings_target, hashes_file, dry_run, force_update)
        results.append(("settings.json", action))
    
    return results


def backup_existing(target_dir: Path, platform: str):
    """Create backup of existing installation."""
    config_dir = target_dir / (".claude" if platform == "claude" else ".opencode")
    if not config_dir.exists():
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = target_dir / ".crewai-skills-backup" / timestamp
    
    print_info(f"Creating backup at {backup_dir}")
    shutil.copytree(config_dir, backup_dir / config_dir.name)


def main():
    parser = argparse.ArgumentParser(
        description="Install CrewAI skills for Claude Code or OpenCode"
    )
    parser.add_argument(
        "--platform", "-p",
        choices=["claude", "opencode"],
        help="Target platform"
    )
    parser.add_argument(
        "--package", "-k",
        choices=["minimal", "standard", "full"],
        help="Package to install"
    )
    parser.add_argument(
        "--target", "-t",
        default=".",
        help="Target directory (default: current directory)"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would be installed without making changes"
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip backup of existing installation"
    )
    parser.add_argument(
        "--yes", "-y",
        action="store_true",
        help="Skip confirmation prompt"
    )
    parser.add_argument(
        "--update", "-u",
        action="store_true",
        help="Update mode: overwrite all existing files"
    )
    
    args = parser.parse_args()
    
    print_header("CrewAI Skills Installer")
    
    # Load packages
    packages = load_packages()
    target_dir = Path(args.target).resolve()
    
    # Get platform
    if args.platform:
        platform = args.platform
    else:
        platform = prompt_platform()
    
    print_success(f"Platform: {platform}")
    
    # Check for existing installation for the selected platform
    config_dir = ".claude" if platform == "claude" else ".opencode"
    existing_dir = target_dir / config_dir
    has_existing = existing_dir.exists()
    
    # Determine install mode (add or update)
    force_update = args.update
    if has_existing and not args.update and not args.yes:
        install_mode = prompt_install_mode(platform)
        force_update = (install_mode == "update")
    
    if has_existing:
        if force_update:
            print_info(f"Mode: Update (overwrite existing files)")
        else:
            print_info(f"Mode: Add (keep customized files)")
    
    # Get package
    if args.package:
        package_name = args.package
    else:
        package_name = prompt_package(packages)
    
    print_success(f"Package: {package_name}")
    
    # Get package contents
    contents = get_package_contents(packages, package_name)
    
    # Summary
    print(f"\n{Colors.BOLD}Installation Summary:{Colors.ENDC}")
    print(f"  Skills:    {len(contents['skills'])}")
    print(f"  Agents:    {len(contents['agents'])}")
    print(f"  Workflows: {len(contents['workflows'])}")
    print(f"  Commands:  {len(contents['commands'])}")
    print(f"  Target:    {target_dir}")
    
    if args.dry_run:
        print_warning("\nDRY RUN - No changes will be made")
    
    # Confirm
    if not args.dry_run and not args.yes:
        confirm = input(f"\nProceed with installation? [y/N]: ").strip().lower()
        if confirm != 'y':
            print_info("Installation cancelled")
            return
    
    # Backup if existing and updating
    if has_existing and force_update and not args.no_backup and not args.dry_run:
        backup_existing(target_dir, platform)
    
    # Install components
    hashes_file = target_dir / config_dir / ".installed-hashes.json"
    
    all_results = []
    
    print(f"\n{Colors.BOLD}Installing...{Colors.ENDC}")
    
    # Install system prompt first
    results = install_system_prompt(platform, target_dir, hashes_file, args.dry_run, force_update)
    all_results.extend(results)
    
    # Install skills from /skills directory
    results = install_skills(contents, platform, target_dir, hashes_file, args.dry_run, force_update)
    all_results.extend(results)
    
    # Install workflows (as skills)
    results = install_workflows(contents, platform, target_dir, hashes_file, args.dry_run, force_update)
    all_results.extend(results)
    
    # Install agents
    results = install_agents(contents, platform, target_dir, hashes_file, args.dry_run, force_update)
    all_results.extend(results)
    
    # Install commands
    results = install_commands(contents, platform, target_dir, hashes_file, args.dry_run, force_update)
    all_results.extend(results)
    
    # Print results
    print(f"\n{Colors.BOLD}Results:{Colors.ENDC}")
    
    created = [r for r in all_results if r[1] == "created"]
    updated = [r for r in all_results if "updated" in r[1]]
    skipped = [r for r in all_results if "skipped" in r[1]]
    
    if created:
        print_success(f"Created: {len(created)} files")
    if updated:
        print_info(f"Updated: {len(updated)} files")
    if skipped:
        print_warning(f"Skipped (customized): {len(skipped)} files")
        for path, action in skipped:
            print(f"  - {path}: {action}")
    
    # Final message
    print(f"\n{Colors.GREEN}{Colors.BOLD}Installation complete!{Colors.ENDC}")
    print(f"\nFiles installed to: {target_dir / config_dir}")
    
    if platform == "claude":
        print(f"\n{Colors.CYAN}Next steps:{Colors.ENDC}")
        print("  1. Start Claude Code in your project")
        print("  2. Use /create-crew to create your first crew")
        print("  3. Or ask Claude to help with CrewAI development")
    else:
        print(f"\n{Colors.CYAN}Next steps:{Colors.ENDC}")
        print("  1. Start OpenCode in your project")
        print("  2. Use /crew create to create your first crew")
        print("  3. The orchestrator will guide you through the process")


if __name__ == "__main__":
    main()
