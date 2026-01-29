# CrewAI Code Quality - Full Reference

> Source: Official CrewAI Documentation

## Naming Conventions

| Component | Convention | Example |
|-----------|------------|---------|
| Project | snake_case | `my_crew_project` |
| Crew class | PascalCase | `ResearchCrew` |
| Agent methods | snake_case | `research_analyst` |
| Task methods | snake_case | `research_task` |
| YAML keys | snake_case | `research_analyst` |
| Tool classes | PascalCase | `CustomSearchTool` |

## Quality Checklist

- [ ] Project follows standard structure
- [ ] Naming conventions followed
- [ ] Agents have detailed roles, goals, backstories
- [ ] Tasks have clear descriptions and expected outputs
- [ ] Tools have proper error handling
- [ ] Environment variables documented
- [ ] README.md complete
- [ ] Tests included

## Agent Design Principles

1. **Role**: Be specific about expertise and seniority
2. **Goal**: Focus on outcomes, make it measurable
3. **Backstory**: Provide context, keep to 2-4 sentences

## Task Design Principles

1. **Description**: Be specific, include numbered requirements
2. **Expected Output**: Define format, length, structure
3. **Context**: List all tasks whose output is needed
