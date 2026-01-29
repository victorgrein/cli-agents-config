# CrewAI Development Skills

A comprehensive collection of skills, agents, and workflows for CrewAI development, compatible with both **Claude Code** and **OpenCode**.

## Quick Start

```bash
# Clone or download this repository
git clone https://github.com/your-org/crewai-skills.git
cd crewai-skills

# Run the installer
python install.py
```

The installer will guide you through:
1. Selecting your platform (Claude Code or OpenCode)
2. Choosing a package (minimal, standard, or full)
3. Choosing install mode (add or update) if existing installation detected
4. Installing the selected components

## Packages

| Package | Skills | Agents | Workflows | Commands | Description |
|---------|--------|--------|-----------|----------|-------------|
| **minimal** | 3 | 3 | 1 | 1 | Core skills for basic crew creation |
| **standard** | 15 | 10 | 5 | 8 | Complete CrewAI development toolkit |
| **full** | 16 | 14 | 5 | 8 | Everything including code agents |

### Minimal
- **Skills**: crewai-agents, crewai-tasks, crewai-crews
- **Agents**: crew-architect, agent-designer, task-designer
- **Workflows**: create-crew
- **Commands**: /crew create

### Standard (Recommended)
Everything in Minimal, plus:
- **Skills**: flows, tools, llms, memory, debugging, optimization, migration, and more
- **Agents**: flow-engineer, tool-specialist, debugger, llm-optimizer, and more
- **Workflows**: debug-crew, optimize-crew, migrate-project, create-flow
- **Commands**: Full /crew command suite

### Full
Everything in Standard, plus:
- **Skills**: task-management
- **Agents**: coder-agent, reviewer, tester, build-agent

## Installation

### Interactive Mode
```bash
python install.py
```

### Command Line Options

```bash
# Basic installation
python install.py --platform claude --package standard

# All options
python install.py [OPTIONS]

Options:
  -p, --platform {claude,opencode}  Target platform
  -k, --package {minimal,standard,full}  Package to install
  -t, --target PATH                 Target directory (default: current)
  -n, --dry-run                     Preview without making changes
  -y, --yes                         Skip confirmation prompts
  -u, --update                      Update mode: overwrite all files
  --no-backup                       Skip backup creation
```

### Examples

```bash
# Install for Claude Code
python install.py --platform claude --package standard

# Install for OpenCode
python install.py --platform opencode --package full

# Preview installation
python install.py --dry-run --platform claude --package minimal

# Install to specific directory
python install.py --target /path/to/project --platform claude

# Non-interactive installation
python install.py --platform claude --package standard --yes

# Update existing installation (overwrite all)
python install.py --platform claude --package standard --update --yes
```

## Install vs Update Mode

When an existing installation is detected (`.claude` or `.opencode` folder exists):

| Mode | Flag | Behavior |
|------|------|----------|
| **Add** | (default) | Creates new files, preserves customized files (saves new version as `.new`) |
| **Update** | `--update` | Overwrites ALL files with latest versions (creates backup first) |

In interactive mode, you'll be prompted to choose:
```
Existing claude installation detected (.claude)

Choose action:
  [1] Add - Add new files, keep customized files
  [2] Update - Overwrite all files with latest versions
```

## Platform Differences

| Feature | Claude Code | OpenCode |
|---------|-------------|----------|
| Config directory | `.claude/` | `.opencode/` |
| Orchestrator | `CLAUDE.md` (file) | Built-in agent |
| Agents location | `.claude/agents/` | `.opencode/agent/subagents/` |
| Commands location | `.claude/commands/` | `.opencode/command/` |
| Settings | `settings.json` | N/A |

## Directory Structure

### Repository Structure
```
crewai-skills/
├── templates/
│   ├── shared/                    # Shared between platforms
│   │   ├── skills/               # 16 CrewAI skills
│   │   ├── agents/               # 14 agents (adapted on install)
│   │   │   ├── crewai/          # CrewAI specialist agents
│   │   │   └── code/            # Code agents
│   │   ├── workflows/            # 5 workflow skills
│   │   └── commands/             # 8 slash commands
│   │       └── crew/
│   └── claude/                   # Claude Code specific
│       ├── CLAUDE.md            # Orchestrator prompt
│       └── settings.json        # Permissions
├── install.py                    # Installer script
├── packages.json                 # Package definitions
└── README.md
```

### Installed Structure (Claude Code)
```
your-project/
└── .claude/
    ├── CLAUDE.md                 # Orchestrator
    ├── settings.json             # Permissions
    ├── agents/                   # Specialist agents
    ├── skills/                   # CrewAI skills + workflows
    └── commands/
        └── crew/                 # /crew commands
```

### Installed Structure (OpenCode)
```
your-project/
└── .opencode/
    ├── agent/
    │   └── subagents/           # Specialist agents
    │       ├── crewai/
    │       └── code/
    ├── skills/                   # CrewAI skills + workflows
    └── command/
        └── crew/                 # /crew commands
```

## Skills Reference

### Concept Skills
| Skill | Description |
|-------|-------------|
| `crewai-agents` | Agent creation with roles, goals, backstories |
| `crewai-tasks` | Task configuration with outputs, context |
| `crewai-crews` | Crew composition and processes |
| `crewai-flows` | Flow creation with state management |
| `crewai-tools` | Custom and built-in tools |
| `crewai-llms` | LLM configuration and optimization |
| `crewai-memory` | Memory system configuration |
| `crewai-processes` | Sequential vs hierarchical processes |
| `crewai-cli` | CLI commands reference |

### Process Skills
| Skill | Description |
|-------|-------------|
| `crewai-debugging` | Troubleshooting crews and flows |
| `crewai-optimization` | Cost, latency, quality optimization |
| `crewai-migration` | Project migration and refactoring |
| `crewai-crew-creation` | Step-by-step crew creation |

### Standard Skills
| Skill | Description |
|-------|-------------|
| `crewai-code-quality` | Code quality standards |
| `crewai-project-structure` | Project structure templates |

## Agents Reference

### CrewAI Agents
| Agent | Description |
|-------|-------------|
| `crew-architect` | Crew/flow design and architecture |
| `agent-designer` | Agent creation and configuration |
| `task-designer` | Task configuration and outputs |
| `tool-specialist` | Custom tool creation |
| `flow-engineer` | Flow code and state management |
| `debugger` | Error analysis and troubleshooting |
| `llm-optimizer` | LLM selection and optimization |
| `migration-specialist` | Project migration |
| `performance-analyst` | Performance analysis |
| `crewai-documenter` | Documentation generation |

### Code Agents (Full package)
| Agent | Description |
|-------|-------------|
| `coder-agent` | Code generation |
| `reviewer` | Code review |
| `tester` | Test creation |
| `build-agent` | Build and deployment |

## Slash Commands

| Command | Description |
|---------|-------------|
| `/crew create` | Create a new crew |
| `/crew debug` | Debug crew issues |
| `/crew optimize` | Optimize performance |
| `/crew migrate` | Migrate project structure |
| `/crew review` | Review existing code |
| `/crew analyze` | Analyze crew architecture |
| `/crew diagram` | Generate diagrams |
| `/crew docs` | Generate documentation |

## Contributing

### Adding a New Skill

1. Create directory: `templates/shared/skills/your-skill/`
2. Add `SKILL.md` with YAML frontmatter
3. Add `references/` and `templates/` as needed
4. Update `packages.json`

### Adding a New Agent

1. Create file: `templates/shared/agents/category/agent-name.md`
2. Use the base format (see existing agents)
3. Update `packages.json`

### Skill Format

```yaml
---
name: my-skill
description: What this skill does
---

## Overview
...

## Quick Reference
...
```

### Agent Format

```yaml
---
name: my-agent
description: What this agent does
tools:
  - Read
  - Write
  - Edit
skills:
  - relevant-skill
model: inherit
---

# Agent Name

<context>
  ...
</context>

<role>
  ...
</role>

<instructions>
  ...
</instructions>
```

## License

MIT License
