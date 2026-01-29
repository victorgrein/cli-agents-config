# CrewAI Tasks - Full Reference

> Source: Official CrewAI Documentation

## Complete Task Attributes

### Essential Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `description` | `str` | Clear, detailed description of what needs to be done |
| `expected_output` | `str` | Specific description of expected deliverable |
| `agent` | `Agent` | Agent responsible for the task |
| `name` | `str` | Identifier for the task |

### Context and Dependencies

| Attribute | Type | Description |
|-----------|------|-------------|
| `context` | `List[Task]` | Tasks whose output provides context |
| `tools` | `List[BaseTool]` | Task-specific tools (override agent tools) |

### Output Handling

| Attribute | Type | Description |
|-----------|------|-------------|
| `output_file` | `str` | Save output to file |
| `output_json` | `Type[BaseModel]` | Parse output as JSON |
| `output_pydantic` | `Type[BaseModel]` | Parse output as Pydantic model |
| `markdown` | `bool` | False | Return output as Markdown |
| `create_directory` | `bool` | True | Create output file directory |

### Execution Settings

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `async_execution` | `bool` | False | Run asynchronously |
| `human_input` | `bool` | False | Require human approval |
| `callback` | `Callable` | None | Function called after completion |
| `config` | `Dict` | None | Task-specific configuration |
| `guardrail` | `Callable` | None | Validation function |
| `guardrails` | `List[Callable]` | None | List of validation functions |
| `guardrail_max_retries` | `int` | 3 | Retries on validation failure |

## Direct Code Definition

```python
from crewai import Task

research_task = Task(
    description="Research the latest AI developments",
    expected_output="A detailed report with key findings",
    agent=researcher,
    tools=[SerperDevTool()]
)

analysis_task = Task(
    description="Analyze the research findings",
    expected_output="Analysis with recommendations",
    agent=analyst,
    context=[research_task]  # Uses research_task output
)
```

## Analysis Task Pattern

```python
analysis_task = Task(
    description="""
    Analyze the provided research and identify key patterns, insights,
    and actionable recommendations.
    """,
    expected_output="""
    An analysis report with:
    1) Key insights (3-5 points)
    2) Supporting evidence
    3) Actionable recommendations (3-5 items)
    """,
    agent=analyst,
    context=[research_task]
)
```
