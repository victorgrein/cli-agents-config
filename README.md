# CrewAI Development Platform

<div align="center">

### AI-powered system for CrewAI development, optimization, debugging, migration, and documentation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Features:** Crew Creation • Flow Engineering • Performance Optimization • Debugging • Migration • Documentation

</div>

---

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Commands](#commands)
- [Context Files](#context-files)
- [Workflows](#workflows)
- [Integrations](#integrations)
- [Testing](#testing)
- [Common Questions](#common-questions)
- [Support](#support)

---

## Overview

The CrewAI Development Platform provides expert-level assistance for all CrewAI operations through a main orchestrator and 10 specialized subagents, backed by comprehensive context files extracted from official CrewAI documentation.

### What It Does

- **Create Crews**: Design complete crew architectures from natural language specifications
- **Build Flows**: Create and manage CrewAI Flows with advanced state management
- **Optimize Performance**: Analyze and optimize for cost, latency, or quality
- **Debug Issues**: Trace execution and identify root causes of problems
- **Migrate Projects**: Refactor and standardize project structures
- **Generate Documentation**: Auto-generate comprehensive documentation and diagrams

---

## Quick Start

### Installation

The CrewAI platform is included in your `.opencode` directory structure. Ensure you have:

```bash
# Verify CrewAI platform files exist
ls -la .opencode/agent/crewai/
ls -la .opencode/context/crewai/
ls -la .opencode/command/crew/
```

### Basic Commands

```bash
# Create a new crew from specification
/crew create "A research crew that analyzes market trends"

# Review an existing crew
/crew review ./my_crew

# Optimize for cost
/crew optimize ./my_crew --target="cost"

# Debug issues
/crew debug ./my_crew

# Generate documentation
/crew docs ./my_crew

# Create a flow
/crew generate-flow "A customer support flow with triage and resolution"
```

### Example Workflow

```bash
# Create a research crew
/crew create "A research crew with web search and analysis capabilities"

# The system will:
# 1. Analyze your specification
# 2. Design appropriate agents and tasks
# 3. Ask for LLM preference (OpenAI or Anthropic)
# 4. Generate YAML configuration and Python code
# 5. Request permission before creating files
# 6. Create the crew structure in your project
```

---

## Architecture

### Main Orchestrator

**`crewai-orchestrator`** - Coordinates all CrewAI operations

- Analyzes request complexity and determines appropriate subagents
- Routes to specialized subagents based on task requirements
- Manages context allocation (80% Level 1, 20% Level 2)
- Integrates with code generation agents for implementation
- Ensures quality and best practices throughout

### Specialized Subagents

| Agent | Purpose |
|-------|---------|
| `crew-architect` | Design and review crew architectures |
| `flow-engineer` | Create and manage CrewAI Flows |
| `agent-designer` | Design and configure agents |
| `task-designer` | Design and configure tasks |
| `tool-specialist` | Create and integrate tools |
| `llm-optimizer` | Optimize LLM configurations |
| `debugger` | Debug and trace execution issues |
| `migration-specialist` | Migrate and refactor projects |
| `performance-analyst` | Analyze performance and bottlenecks |
| `crewai-documenter` | Generate documentation and diagrams |

### Directory Structure

```
.opencode/
├── agent/crewai/
│   ├── crewai-orchestrator.md
│   └── subagents/
│       ├── crew-architect.md
│       ├── flow-engineer.md
│       ├── agent-designer.md
│       ├── task-designer.md
│       ├── tool-specialist.md
│       ├── llm-optimizer.md
│       ├── debugger.md
│       ├── migration-specialist.md
│       ├── performance-analyst.md
│       └── crewai-documenter.md
├── context/crewai/
│   ├── domain/concepts/      # Core CrewAI concepts
│   ├── processes/            # Best practices and workflows
│   ├── standards/            # Code quality and structure
│   └── templates/            # YAML and Python templates
├── workflows/crewai/         # Predefined workflows
├── command/crew/             # Slash commands
└── CREWAI-TESTING.md        # Testing guide
```

---

## Commands

| Operation | Command | Description |
|-----------|---------|-------------|
| Create crew | `/crew create "{spec}"` | Create new crew from specification |
| Create flow | `/crew generate-flow "{type}"` | Create flow with multiple crews |
| Review architecture | `/crew review {path}` | Review existing crew/flow |
| Analyze performance | `/crew analyze {path}` | Analyze performance metrics |
| Optimize | `/crew optimize {path} --target="cost\|latency\|quality"` | Optimize crew performance |
| Debug | `/crew debug {path}` | Debug execution issues |
| Migrate | `/crew migrate {path} --to="flow"` | Migrate to standard structure |
| Document | `/crew docs {path}` | Generate documentation |
| Diagram | `/crew diagram {path}` | Generate architecture diagrams |

### Detailed Examples

#### Create a Crew

```bash
# Simple crew
/crew create "A research crew with one agent that searches the web"

# Multi-agent crew
/crew create "A content creation crew with researcher, writer, and editor agents"

# Complex crew with specific process
/crew create "A customer support crew with triage, response, escalation, and quality review agents using hierarchical process"
```

#### Optimize a Crew

```bash
# Optimize for cost
/crew optimize ./my_crew --target="cost"

# Optimize for latency
/crew optimize ./my_crew --target="latency"

# Optimize for quality
/crew optimize ./my_crew --target="quality"
```

#### Debug a Crew

```bash
# Debug specific crew
/crew debug ./my_crew

# Debug with error context
/crew debug ./my_crew --error="AttributeError: 'Agent' object has no attribute 'execute'"
```

---

## Context Files

### Domain Knowledge (`context/crewai/domain/concepts/`)

| File | Description |
|------|-------------|
| `flows.md` | Flow architecture, decorators, state management |
| `crews.md` | Crew configuration, processes, outputs |
| `agents.md` | Agent attributes, archetypes, roles |
| `tasks.md` | Task configuration, context passing, dependencies |
| `tools.md` | Built-in tools, custom tool creation, integration |
| `llms.md` | LLM providers, model selection, configuration |
| `memory.md` | Memory types, configuration, usage patterns |
| `processes.md` | Sequential vs hierarchical processes |
| `cli.md` | CLI commands and utilities |

### Processes (`context/crewai/processes/`)

| File | Description |
|------|-------------|
| `crew-creation.md` | Step-by-step crew creation workflow |
| `debugging.md` | Debugging procedures and common issues |
| `optimization.md` | Performance optimization strategies |
| `migration.md` | Migration patterns and best practices |

### Standards (`context/crewai/standards/`)

| File | Description |
|------|-------------|
| `code-quality.md` | Code quality standards and best practices |
| `project-structure.md` | Standard project structure organization |

### Templates (`context/crewai/templates/`)

| File | Description |
|------|-------------|
| `agent-yaml.md` | Agent YAML templates |
| `task-yaml.md` | Task YAML templates |
| `flow-class.md` | Flow class templates |

---

## Workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| `create-crew` | `/crew create` | Create new crew from specification |
| `create-flow` | `/crew generate-flow` | Create flow with multiple crews |
| `debug-crew` | `/crew debug` | Debug execution issues and errors |
| `optimize-crew` | `/crew optimize` | Optimize performance metrics |
| `migrate-project` | `/crew migrate` | Migrate to standard structure |

---

## Integrations

### LLM Providers

The platform supports multiple LLM providers. The system always asks for your preference:

**OpenAI Options:**
- `gpt-4o` - Best quality, most capable
- `gpt-4o-mini` - Fast and cost-effective
- `gpt-3.5-turbo` - Cheapest, good for simple tasks

**Anthropic Options:**
- `claude-3-5-sonnet` - Excellent reasoning and analysis
- `claude-3-haiku` - Fast, cost-effective for routine tasks

### Tools and Services

- **CrewAI Tracing**: Built-in trace analysis and execution monitoring
- **uv**: Modern dependency management for Python
- **OpenAI API**: Access to GPT models for agent execution
- **Anthropic API**: Access to Claude models for agent execution

### File Operations

| Operation | Permission |
|-----------|------------|
| Read/Search | ✅ Always allowed |
| Create/Modify/Delete | ⚠️ Asks permission before proceeding |

---

## Testing

### Pre-Testing Setup

1. Ensure you have a CrewAI project to test with
2. Configure API keys (OPENAI_API_KEY or ANTHROPIC_API_KEY)
3. Familiarize yourself with command syntax

### Command Tests

#### /crew create

```bash
# Test 1: Simple crew
/crew create "A research crew with one agent that searches the web"

# Test 2: Multi-agent crew
/crew create "A content creation crew with researcher, writer, and editor agents"

# Test 3: Complex crew
/crew create "A customer support crew with triage, response, escalation, and quality review agents using hierarchical process"
```

**Expected:**
- [ ] Specification analyzed correctly
- [ ] Appropriate agents identified
- [ ] Tasks designed with dependencies
- [ ] YAML configuration generated
- [ ] Python code generated
- [ ] LLM preference asked
- [ ] Permission requested before file creation

#### /crew review

```bash
# Test on existing crew
/crew review ./path/to/crew
```

**Expected:**
- [ ] Crew structure analyzed
- [ ] Quality score provided
- [ ] Strengths identified
- [ ] Issues found with severity levels
- [ ] Improvement recommendations given

#### /crew analyze

```bash
/crew analyze ./path/to/crew
```

**Expected:**
- [ ] Configuration analyzed
- [ ] Token usage estimated
- [ ] Cost projections provided
- [ ] Bottlenecks identified
- [ ] Optimization opportunities listed

#### /crew optimize

```bash
# Test cost optimization
/crew optimize ./path/to/crew --target="cost"

# Test latency optimization
/crew optimize ./path/to/crew --target="latency"

# Test quality optimization
/crew optimize ./path/to/crew --target="quality"
```

**Expected:**
- [ ] Current state analyzed
- [ ] Recommendations generated for target
- [ ] LLM preference asked
- [ ] Before/after comparison shown
- [ ] Permission requested for changes

#### /crew debug

```bash
/crew debug ./path/to/crew
```

**Expected:**
- [ ] Code analyzed
- [ ] Common issues checked
- [ ] Root cause identified (if issue exists)
- [ ] Fix suggested with code
- [ ] Verification steps provided

#### /crew migrate

```bash
/crew migrate ./path/to/crew --to="flow"
```

**Expected:**
- [ ] Current structure analyzed
- [ ] Migration plan created
- [ ] New structure generated
- [ ] Before/after comparison shown
- [ ] Backup mentioned
- [ ] Permission requested

#### /crew docs

```bash
/crew docs ./path/to/crew
```

**Expected:**
- [ ] Structure analyzed
- [ ] README content generated
- [ ] Architecture diagram included
- [ ] Agent/task tables created
- [ ] Usage examples provided

#### /crew diagram

```bash
/crew diagram ./path/to/crew --type="architecture"
```

**Expected:**
- [ ] Structure analyzed
- [ ] Diagram generated (ASCII or Mermaid)
- [ ] Components shown correctly
- [ ] Relationships indicated

### Context Loading Tests

Test that context files load correctly:

```bash
# Ask about flows
"Explain how CrewAI flows work"

# Ask about agents
"What are the best practices for designing CrewAI agents?"

# Ask about optimization
"How do I optimize my crew for cost?"
```

**Expected:**
- [ ] Relevant context loaded
- [ ] Accurate information provided
- [ ] Official documentation followed

### Subagent Routing Tests

Test that requests route to correct subagents:

```bash
# Should route to crew-architect
"Review my crew architecture"

# Should route to flow-engineer
"Create a flow with multiple crews"

# Should route to llm-optimizer
"Optimize my LLM settings for cost"

# Should route to debugger
"Debug this error in my crew"
```

**Expected:**
- [ ] Correct subagent engaged
- [ ] Appropriate context loaded
- [ ] Specialized response provided

### Testing Checklist

- [ ] Test `/crew create` with simple specification
- [ ] Test `/crew review` on existing crew
- [ ] Test `/crew analyze` for performance metrics
- [ ] Test `/crew optimize` with different targets
- [ ] Test `/crew debug` with error scenario
- [ ] Test `/crew migrate` on crew project
- [ ] Test `/crew docs` for documentation generation
- [ ] Test `/crew diagram` for visualization
- [ ] Verify context files load correctly
- [ ] Verify LLM preference prompts work

### Troubleshooting

#### Context Not Loading
- Check file paths in agent definitions
- Verify context files exist
- Check navigation.md files

#### Wrong Subagent Routing
- Review keyword triggers in orchestrator
- Check routing intelligence section
- Verify subagent registry

#### Permission Not Asked
- Check file_operations section in orchestrator
- Verify operation type detection

#### LLM Preference Not Asked
- Check llm_configuration section
- Verify workflow includes LLM step

---

## Common Questions

**Q: How do I create a new crew?**
A: Use `/crew create "{spec}"` with a clear description of what your crew should do. The system will design agents, tasks, and generate all necessary code.

**Q: Can I optimize for different goals?**
A: Yes! Use `/crew optimize {path} --target="cost|latency|quality"` to optimize for cost, speed, or output quality.

**Q: What LLMs are supported?**
A: We support OpenAI (gpt-4o, gpt-4o-mini, gpt-3.5-turbo) and Anthropic (claude-3-5-sonnet, claude-3-haiku). The system will ask your preference.

**Q: How do I debug my crew?**
A: Use `/crew debug {path}` to analyze execution issues. The debugger will identify root causes and suggest fixes.

**Q: Can I migrate existing projects?**
A: Yes! Use `/crew migrate {path} --to="flow"` to migrate crews to flows or standardize project structure.

**Q: How does the system choose which subagent to use?**
A: The orchestrator analyzes your request and routes to the appropriate specialized subagent (e.g., crew-architect for design, debugger for issues).

**Q: Are file operations safe?**
A: Yes! The system always asks permission before creating, modifying, or deleting files. Read operations are allowed without asking.

**Q: Can I generate documentation automatically?**
A: Use `/crew docs {path}` to generate comprehensive documentation including README, architecture diagrams, and usage examples.

**Q: What context files are included?**
A: The platform includes comprehensive context files covering CrewAI concepts, processes, standards, and templates extracted from official documentation.

**Q: How do I create a flow?**
A: Use `/crew generate-flow "{type}"` to create flows with multiple crews, state management, and event-driven execution.

---

## Tips for Success

1. **Start simple**: Test with basic crews before complex flows
2. **Be specific**: Provide clear, detailed specifications for better results
3. **Use verbose mode**: Enable `verbose=True` for debugging
4. **Check context**: The system automatically loads relevant context files
5. **Iterate**: Refine crews based on actual usage and performance
6. **Review carefully**: Always review generated code before approval
7. **Test thoroughly**: Use the testing checklist to verify functionality

---

## Support

### Official CrewAI Documentation
For official CrewAI documentation: https://docs.crewai.com/

### Getting Help
For issues with the CrewAI Development Platform:
1. Review the context files in `.opencode/context/crewai/`
2. Check the troubleshooting section above
3. Ask specific questions about CrewAI concepts or operations

### License
This project is licensed under the MIT License.

---

**Ready to build powerful CrewAI systems? Start with `/crew create` and let the platform guide you through the process!**
