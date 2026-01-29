# CrewAI CLI - Full Reference

> Source: Official CrewAI Documentation

## Installation

CrewAI uses `uv` as its dependency management and package handling tool:

```bash
pip install crewai
```

## All Commands

### Project Creation

```bash
crewai create crew <name>  # Create crew project
crewai create flow <name>  # Create flow project
```

### Dependency Management

```bash
crewai install  # Install dependencies (runs uv sync)
```

### Execution

```bash
crewai run           # Run crew or flow
crewai flow kickoff  # Run flow explicitly
crewai flow plot     # Generate flow visualization
```

### Debugging

```bash
crewai log-tasks-outputs  # View task outputs and IDs
crewai replay -t <id>     # Replay from specific task
```

## uv Commands

```bash
uv add <package>           # Add dependency
uv add 'crewai[tools]'     # Add with extras
uv add <package>@<version> # Add specific version
uv sync                    # Sync dependencies
uv run <script>            # Run script in venv
uv run pytest              # Run tests
```

## Adding a New Crew to Flow

```bash
# Copy existing crew as template
cp -r src/my_flow/crews/poem_crew src/my_flow/crews/new_crew

# Edit the new crew
# Edit config/agents.yaml
# Edit config/tasks.yaml
# Edit new_crew.py

# Import in main.py and add to flow
```
