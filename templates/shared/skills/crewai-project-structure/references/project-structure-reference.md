# CrewAI Project Structure - Full Reference

> Source: Official CrewAI Documentation

## Directory Purposes

| Directory | Purpose |
|-----------|---------|
| `src/` | Source code |
| `config/` | YAML configurations |
| `tools/` | Custom tools |
| `tests/` | Test files |
| `output/` | Generated outputs |

## Crew Project Structure

```
my_crew/
├── src/
│   └── my_crew/
│       ├── __init__.py
│       ├── main.py              # Entry point
│       ├── crew.py              # Crew definition
│       ├── config/
│       │   ├── agents.yaml      # Agent configurations
│       │   └── tasks.yaml       # Task configurations
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py   # Custom tools
├── tests/
│   ├── __init__.py
│   └── test_crew.py
├── output/                      # Generated outputs
├── pyproject.toml
├── README.md
├── .env                         # Environment variables
└── .gitignore
```

## Flow Project Structure

```
my_flow/
├── src/
│   └── my_flow/
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
├── output/
├── pyproject.toml
├── README.md
├── .env
└── .gitignore
```

## Best Practices

1. **Keep configs in YAML**: Easier to maintain and modify
2. **Separate tools**: Custom tools in dedicated directory
3. **Use __init__.py**: Proper Python package structure
4. **Output directory**: Keep generated files organized
5. **Environment variables**: Never commit .env files
6. **Tests**: Include basic tests for crews
