# CrewAI Migration - Full Reference

> Source: Official CrewAI Documentation

## Migration Types

### 1. Crew to Flow Migration

Convert standalone crew to flow-based architecture.

### 2. Code to YAML Migration

Move inline definitions to YAML configuration.

### 3. Monolithic to Modular

Break large crew into smaller, reusable components.

### 4. Version Upgrade

Update to latest CrewAI version.

## Standard Flow Project Structure

```
my_project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py              # Flow entry point
│       ├── crews/
│       │   ├── __init__.py
│       │   ├── research_crew/
│       │   │   ├── __init__.py
│       │   │   ├── config/
│       │   │   │   ├── agents.yaml
│       │   │   │   └── tasks.yaml
│       │   │   └── research_crew.py
│       │   └── writing_crew/
│       │       └── ...
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py
├── tests/
├── pyproject.toml
├── README.md
└── .env
```

## Migration Checklist

- [ ] Backup existing project
- [ ] Create target structure
- [ ] Move/update crew files
- [ ] Update imports
- [ ] Create flow (if migrating to flow)
- [ ] Update pyproject.toml
- [ ] Test all functionality
- [ ] Update documentation
- [ ] Clean up old files
