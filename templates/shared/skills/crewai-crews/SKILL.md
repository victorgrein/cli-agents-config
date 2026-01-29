---
name: crewai-crews
description: Create and configure CrewAI crews with agents, tasks, process types, memory, and execution settings
license: MIT
compatibility: opencode
metadata:
  category: crewai-concept
  audience: developers
  complexity: moderate
---

## What This Skill Does

Provides comprehensive guidance for creating CrewAI crews - collaborative groups of agents working together to achieve tasks. Includes process types (sequential/hierarchical), memory configuration, output handling, and kickoff methods.

## When to Use This Skill

- Creating a new crew to orchestrate agents
- Choosing between sequential and hierarchical processes
- Configuring crew-level memory and caching
- Setting up streaming execution
- Handling crew outputs and metrics
- Using kickoff methods (sync/async/batch)

## Quick Reference

### Key Attributes

| Attribute | Description | Default |
|-----------|-------------|---------|
| `agents` | List of agents in the crew | Required |
| `tasks` | List of tasks to execute | Required |
| `process` | Execution flow (sequential/hierarchical) | `sequential` |
| `verbose` | Enable detailed logging | `False` |
| `memory` | Enable execution memories | `False` |
| `cache` | Cache tool results | `True` |
| `manager_llm` | LLM for hierarchical manager | Required for hierarchical |

### Crew Output

| Attribute | Type | Description |
|-----------|------|-------------|
| `raw` | `str` | Raw output string |
| `pydantic` | `Optional[BaseModel]` | Structured Pydantic output |
| `json_dict` | `Optional[Dict]` | JSON dictionary output |
| `tasks_output` | `List[TaskOutput]` | Individual task outputs |
| `token_usage` | `Dict[str, Any]` | Token usage summary |

## Basic Crew Pattern

### YAML Configuration

```yaml
# config/agents.yaml
researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}.
```

```yaml
# config/tasks.yaml
research_task:
  description: >
    Research the latest developments in {topic}
  expected_output: >
    A comprehensive report on {topic}
  agent: researcher
```

### Crew Class

```python
from crewai import Agent, Crew, Process
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class ResearchCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
```

## Process Types

### Sequential Process (Default)

Tasks execute one after another in order:

```python
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)
```

**Flow:** `Task 1 → Task 2 → Task 3 → Output`

### Hierarchical Process

Manager agent coordinates and delegates:

```python
crew = Crew(
    agents=[researcher, writer, analyst],
    tasks=[research_task, write_task, analysis_task],
    process=Process.hierarchical,
    manager_llm="gpt-4o"  # Required for hierarchical
)
```

## Decorators

| Decorator | Purpose |
|-----------|---------|
| `@CrewBase` | Marks class as crew base |
| `@agent` | Denotes method returning Agent |
| `@task` | Denotes method returning Task |
| `@crew` | Denotes method returning Crew |
| `@before_kickoff` | Execute before crew starts |
| `@after_kickoff` | Execute after crew finishes |

## Kickoff Methods

### Synchronous

```python
result = crew.kickoff(inputs={"topic": "AI"})
result = crew.kickoff_for_each(inputs=[{"topic": "AI"}, {"topic": "ML"}])
```

### Asynchronous (Native)

```python
result = await crew.akickoff(inputs={"topic": "AI"})
results = await crew.akickoff_for_each(inputs=[...])
```

### Asynchronous (Thread-based)

```python
result = await crew.kickoff_async(inputs={"topic": "AI"})
results = await crew.kickoff_for_each_async(inputs=[...])
```

## Streaming Execution

```python
crew = Crew(
    agents=[researcher],
    tasks=[task],
    stream=True
)

streaming = crew.kickoff(inputs={"topic": "AI"})
for chunk in streaming:
    print(chunk.content, end="", flush=True)
result = streaming.result
```

## Memory and Cache

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True,  # Enable memory
    cache=True,   # Enable caching
    embedder={"provider": "openai"}
)
```

## Usage Metrics

```python
crew.kickoff()
print(crew.usage_metrics)
# {'total_tokens': 15000, 'prompt_tokens': 12000, ...}
```

## Logging

```python
crew = Crew(
    agents=[...],
    output_log_file="logs.json"  # or "logs.txt" or True
)
```

## Replay from Task

```bash
# View task IDs
crewai log-tasks-outputs

# Replay from specific task
crewai replay -t <task_id>
```

## Best Practices

1. **Choose Process Wisely**: Sequential for linear, hierarchical for complex
2. **Enable Memory**: For multi-step or iterative tasks
3. **Use Caching**: Reduces redundant API calls
4. **Set Rate Limits**: Avoid API limit errors
5. **Log Outputs**: For debugging and monitoring
6. **Use Verbose Mode**: During development

## Related Skills

- `crewai-agents` - Creating agents for crews
- `crewai-tasks` - Creating tasks for crews
- `crewai-processes` - Detailed process comparison
- `crewai-flows` - Orchestrating multiple crews
