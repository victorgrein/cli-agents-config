# CrewAI LLMs - Full Reference

> Source: Official CrewAI Documentation

## OpenAI Models

```python
from crewai import Agent

# Using model name string
agent = Agent(
    role="Researcher",
    goal="Research topics",
    backstory="Expert researcher",
    llm="gpt-4o"  # or "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"
)
```

**Available Models:**
| Model | Context Window | Best For |
|-------|---------------|----------|
| `gpt-4o` | 128K | Complex reasoning, multimodal |
| `gpt-4o-mini` | 128K | Fast, cost-effective, function calling |
| `gpt-4-turbo` | 128K | Strong reasoning, long documents |
| `gpt-3.5-turbo` | 16K | Simple tasks, prototyping |

## Anthropic Models

```python
agent = Agent(
    role="Analyst",
    goal="Analyze data",
    backstory="Expert analyst",
    llm="claude-3-5-sonnet"  # or "claude-3-opus", "claude-3-sonnet", "claude-3-haiku"
)
```

**Available Models:**
| Model | Context Window | Best For |
|-------|---------------|----------|
| `claude-3-5-sonnet` | 200K | Excellent reasoning, coding |
| `claude-3-opus` | 200K | Highest quality, best reasoning |
| `claude-3-sonnet` | 200K | Good balance of quality/speed |
| `claude-3-haiku` | 200K | Fast, cost-effective |

## Context Window Behavior

When context exceeds limit with `respect_context_window=True`:
- Warning: "Context length exceeded. Summarizing content..."
- Automatic summarization of conversation history
- Execution continues with summarized context

When context exceeds limit with `respect_context_window=False`:
- Error: "Context length exceeded. Consider using smaller text or RAG tools."
- Execution stops
