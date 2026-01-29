# CrewAI Agents - Full Reference

> Source: Official CrewAI Documentation

## Complete Agent Attributes

### Essential Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | `str` | Defines the agent's function and expertise |
| `goal` | `str` | Individual objective guiding decision-making |
| `backstory` | `str` | Provides context and personality |

### LLM Configuration

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `llm` | `Union[str, LLM, Any]` | `gpt-4` | Language model powering the agent |
| `function_calling_llm` | `Optional[Any]` | None | Separate LLM for tool calling |
| `step_callback` | `Optional[Any]` | None | Function called after each step |
| `knowledge_sources` | `Optional[List[Any]]` | None | Domain knowledge sources |
| `embedder` | `Optional[Dict]` | None | Embedder configuration |
| `use_system_prompt` | `Optional[bool]` | True | Use system prompt (for o1 models) |

### Behavior Settings

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `verbose` | `bool` | False | Enable detailed logging |
| `allow_delegation` | `bool` | False | Allow delegating to other agents |
| `max_iter` | `int` | 20 | Max iterations before best answer |
| `max_rpm` | `Optional[int]` | None | Rate limit for API calls |
| `max_execution_time` | `Optional[int]` | None | Timeout in seconds |
| `max_retry_limit` | `int` | 2 | Retries on error |

### Advanced Features

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `memory` | `bool` | False | Maintain conversation history |
| `cache` | `bool` | True | Cache tool results |
| `reasoning` | `bool` | False | Enable planning before execution |
| `max_reasoning_attempts` | `Optional[int]` | None | Limit planning iterations |
| `multimodal` | `bool` | False | Process text and images |
| `allow_code_execution` | `bool` | False | Enable code execution |
| `code_execution_mode` | `Literal["safe", "unsafe"]` | "safe" | Docker or direct execution |
| `respect_context_window` | `bool` | True | Auto-summarize if context exceeded |
| `inject_date` | `bool` | False | Inject current date into tasks |
| `date_format` | `str` | "%Y-%m-%d" | Date format string |

### Templates

| Attribute | Type | Description |
|-----------|------|-------------|
| `system_template` | `Optional[str]` | Custom system prompt |
| `prompt_template` | `Optional[str]` | Custom input format |
| `response_template` | `Optional[str]` | Custom output format |

## Context Window Management

### Auto-Summarization (Default)

```python
agent = Agent(
    role="...",
    respect_context_window=True  # Auto-summarize when exceeded
)
```

### Strict Mode

```python
agent = Agent(
    role="...",
    respect_context_window=False  # Error on context limit
)
```

## Direct Code Definition Example

```python
from crewai import Agent
from crewai_tools import SerperDevTool

agent = Agent(
    role="Senior Data Scientist",
    goal="Analyze and interpret complex datasets",
    backstory="With over 10 years of experience in data science...",
    llm="gpt-4o",
    tools=[SerperDevTool()],
    verbose=True,
    memory=True
)
```
