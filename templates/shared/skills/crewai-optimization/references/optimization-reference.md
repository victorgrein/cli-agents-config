# CrewAI Optimization - Full Reference

> Source: Official CrewAI Documentation

## Model Selection by Optimization Target

| Optimization | Main LLM | Function Calling LLM |
|--------------|----------|---------------------|
| Cost | gpt-4o-mini | gpt-3.5-turbo |
| Latency | gpt-4o-mini | gpt-4o-mini |
| Quality | gpt-4o | gpt-4o-mini |
| Balanced | gpt-4o-mini | gpt-3.5-turbo |

## Approximate Costs (per 1K tokens)

| Model | Input | Output |
|-------|-------|--------|
| gpt-4o | $0.005 | $0.015 |
| gpt-4o-mini | $0.00015 | $0.0006 |
| gpt-3.5-turbo | $0.0005 | $0.0015 |
| claude-3-5-sonnet | $0.003 | $0.015 |
| claude-3-opus | $0.015 | $0.075 |
| claude-3-haiku | $0.00025 | $0.00125 |

## Configuration Templates

### Cost Optimization

```python
agent = Agent(
    llm="gpt-4o-mini",
    function_calling_llm="gpt-3.5-turbo",
    cache=True,
    max_iter=15
)
```

### Quality Optimization

```python
agent = Agent(
    llm="gpt-4o",
    reasoning=True,
    max_iter=25,
    memory=True
)
```

### Latency Optimization

```python
agent = Agent(
    llm="gpt-4o-mini",
    cache=True,
    max_iter=10,
    max_execution_time=60
)
```
