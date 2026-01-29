# CrewAI Debugging - Full Reference

> Source: Official CrewAI Documentation

## Complete Issue Categories

| Category | Symptoms | Check |
|----------|----------|-------|
| Rate Limits | 429 errors, intermittent failures | max_rpm settings |
| Context Window | Truncated output, lost context | respect_context_window |
| Tool Errors | Tool not found, wrong arguments | Tool assignment, descriptions |
| Agent Loops | max_iter reached, repeated actions | Task clarity, delegation |
| Output Parsing | Pydantic errors, JSON failures | Output format, model |

## Debugging Commands

```bash
# View task outputs
crewai log-tasks-outputs

# Replay from specific task
crewai replay -t <task_id>
```

## Verbose Logging Setup

```python
# Agent-level
agent = Agent(role="...", verbose=True)

# Crew-level
crew = Crew(agents=[...], verbose=True)

# File logging
crew = Crew(
    agents=[...],
    output_log_file="debug_logs.json"
)
```

## Token Usage Analysis

```python
result = crew.kickoff()
print(crew.usage_metrics)

# Per-task analysis
for task_output in result.tasks_output:
    print(f"Task: {task_output.description[:50]}")
    print(f"Tokens: {task_output.token_usage}")
```

## Common Fixes Summary

| Issue | Fix |
|-------|-----|
| Rate limits | Add `max_rpm=30` to agent/crew |
| Context exceeded | Set `respect_context_window=True` |
| Tool not used | Improve tool description, check instantiation |
| Agent loops | Reduce `max_iter`, clarify task |
| Parse errors | Use `Optional` fields, improve `expected_output` |
| Async errors | Use `asyncio.run()` properly |
