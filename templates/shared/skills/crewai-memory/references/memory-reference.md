# CrewAI Memory - Full Reference

> Source: Official CrewAI Documentation

## Memory Types Overview

### Short-Term Memory

Stores information from the current session/execution:
- Recent conversation context
- Current task outputs
- Temporary working data

### Long-Term Memory

Persists information across sessions:
- Historical interactions
- Learned patterns
- Accumulated knowledge

### Entity Memory

Tracks information about specific entities:
- People, organizations, concepts
- Relationships between entities
- Entity-specific context

## Embedder Providers

| Provider | Configuration |
|----------|---------------|
| OpenAI | `{"provider": "openai"}` |
| Cohere | `{"provider": "cohere"}` |
| HuggingFace | `{"provider": "huggingface"}` |
| Custom | `{"provider": "custom", "config": {...}}` |

## Full Configuration Example

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
)
```

## Limitations

- Memory increases token consumption
- Long-term memory requires persistent storage
- Entity extraction may not be perfect
- Memory retrieval adds latency
