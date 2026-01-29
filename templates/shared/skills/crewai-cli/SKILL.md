---
name: crewai-cli
description: Use CrewAI CLI for project creation, dependency management, running crews and flows, and debugging
license: MIT
compatibility: opencode
metadata:
  category: crewai-concept
  audience: developers
  complexity: basic
---

## What This Skill Does

Provides comprehensive guidance for using the CrewAI command-line interface (CLI) for creating, managing, and running CrewAI projects. Includes project creation, dependency management, and debugging commands.

## When to Use This Skill

- Creating new crew or flow projects
- Installing and managing dependencies
- Running crews and flows
- Debugging with task replay
- Managing virtual environments

## Quick Reference

### Essential Commands

| Command | Purpose |
|---------|---------|
| `crewai create crew <name>` | Create new crew project |
| `crewai create flow <name>` | Create new flow project |
| `crewai install` | Install dependencies |
| `crewai run` | Run crew or flow |
| `crewai log-tasks-outputs` | View task outputs |
| `crewai replay -t <id>` | Replay from task |

## Project Commands

### Create New Project

```bash
# Create a new crew project
crewai create crew my_crew

# Create a new flow project
crewai create flow my_flow
```

### Generated Structure (Crew)

```
my_crew/
├── src/
│   └── my_crew/
│       ├── __init__.py
│       ├── main.py
│       ├── crew.py
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── tools/
│           └── custom_tool.py
├── tests/
├── pyproject.toml
└── README.md
```

### Generated Structure (Flow)

```
my_flow/
├── src/
│   └── my_flow/
│       ├── __init__.py
│       ├── main.py
│       ├── crews/
│       │   └── poem_crew/
│       │       ├── config/
│       │       │   ├── agents.yaml
│       │       │   └── tasks.yaml
│       │       └── poem_crew.py
│       └── tools/
│           └── custom_tool.py
├── tests/
├── pyproject.toml
└── README.md
```

### Install Dependencies

```bash
crewai install
```

This runs `uv sync` to install all dependencies from `pyproject.toml`.

### Run Project

```bash
# Run crew or flow (auto-detects type)
crewai run

# Explicitly run flow
crewai flow kickoff
```

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

## Dependency Management

### Add Dependencies

```bash
# Add a package
uv add package_name

# Add CrewAI tools
uv add 'crewai[tools]'

# Add specific version
uv add package_name@1.2.3
```

### Sync Dependencies

```bash
uv sync
```

### Update Dependencies

```bash
uv add crewai@latest
uv add 'crewai[tools]'@latest
```

## Debugging Commands

### View Task Outputs

```bash
crewai log-tasks-outputs
```

Shows the latest kickoff task IDs for replay.

### Replay from Task

```bash
crewai replay -t <task_id>
```

Replays execution from a specific task, retaining context from previous tasks.

## Flow Commands

### Kickoff Flow

```bash
crewai flow kickoff
```

### Plot Flow

```bash
crewai flow plot
```

Generates an HTML visualization of the flow.

## Running with uv

Alternative to `crewai run`:

```bash
# Run the project
uv run kickoff

# Run with specific inputs
uv run kickoff --topic "AI trends"

# Run tests
uv run pytest
```

## Project Configuration

### pyproject.toml (Crew)

```toml
[project]
name = "my_crew"
version = "0.1.0"
description = "My CrewAI project"
requires-python = ">=3.10"
dependencies = [
    "crewai>=0.100.0",
    "crewai-tools>=0.17.0",
]

[project.scripts]
kickoff = "my_crew.main:kickoff"

[tool.crewai]
type = "crew"
```

### pyproject.toml (Flow)

```toml
[project]
name = "my_flow"
version = "0.1.0"
description = "My CrewAI Flow"
requires-python = ">=3.10"
dependencies = [
    "crewai>=0.100.0",
]

[project.scripts]
kickoff = "my_flow.main:kickoff"
plot = "my_flow.main:plot"

[tool.crewai]
type = "flow"
```

### Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key
ANTHROPIC_API_KEY=your_api_key
SERPER_API_KEY=your_api_key
```

## Common Workflows

### Starting a New Crew Project

```bash
# Create project
crewai create crew my_project
cd my_project

# Install dependencies
crewai install

# Activate environment
source .venv/bin/activate

# Edit agents and tasks
# Edit src/my_project/config/agents.yaml
# Edit src/my_project/config/tasks.yaml

# Run
crewai run
```

### Starting a New Flow Project

```bash
# Create project
crewai create flow my_flow
cd my_flow

# Install dependencies
crewai install

# Activate environment
source .venv/bin/activate

# Edit flow and crews
# Edit src/my_flow/main.py
# Edit crews in src/my_flow/crews/

# Run
crewai run
```

### Debugging a Crew

```bash
# Run with verbose output
# (Set verbose=True in crew definition)

# View task outputs
crewai log-tasks-outputs

# Replay from specific task
crewai replay -t <task_id>
```

## Tips

1. **Always use virtual environment**: `source .venv/bin/activate`
2. **Use uv for dependencies**: Faster than pip
3. **Check pyproject.toml**: Ensure type is set correctly (crew/flow)
4. **Use verbose mode**: Set `verbose=True` for debugging
5. **Save logs**: Use `output_log_file` for persistent logs

## Related Skills

- `crewai-crews` - Crew configuration
- `crewai-flows` - Flow configuration
- `crewai-debugging` - Debugging strategies
- `crewai-project-structure` - Project structure standards
