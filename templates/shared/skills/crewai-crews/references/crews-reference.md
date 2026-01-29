# CrewAI Crews - Full Reference

> Source: Official CrewAI Documentation

## Complete Crew Attributes

| Attribute | Parameter | Description |
|-----------|-----------|-------------|
| **Tasks** | `tasks` | A list of tasks assigned to the crew |
| **Agents** | `agents` | A list of agents that are part of the crew |
| **Process** | `process` | The process flow (sequential, hierarchical). Default: `sequential` |
| **Verbose** | `verbose` | Verbosity level for logging. Default: `False` |
| **Manager LLM** | `manager_llm` | LLM used by manager in hierarchical process. **Required for hierarchical** |
| **Manager Agent** | `manager_agent` | Custom agent as manager |
| **Function Calling LLM** | `function_calling_llm` | LLM for tool calling (overrides agent LLMs) |
| **Max RPM** | `max_rpm` | Maximum requests per minute (overrides agent settings) |
| **Memory** | `memory` | Enable execution memories (short-term, long-term, entity) |
| **Cache** | `cache` | Cache tool execution results. Default: `True` |
| **Embedder** | `embedder` | Embedder configuration. Default: `{"provider": "openai"}` |
| **Planning** | `planning` | Enable planning before each iteration |
| **Planning LLM** | `planning_llm` | LLM for AgentPlanner |
| **Knowledge Sources** | `knowledge_sources` | Knowledge sources accessible to all agents |
| **Stream** | `stream` | Enable streaming output. Default: `False` |
| **Output Log File** | `output_log_file` | Save logs to file (`.txt` or `.json`) |
| **Config** | `config` | Optional configuration settings |
| **Step Callback** | `step_callback` | Function called after each agent step |
| **Task Callback** | `task_callback` | Function called after each task completion |
| **Share Crew** | `share_crew` | Share crew data with CrewAI team |
| **Prompt File** | `prompt_file` | Path to prompt JSON file |

## Crew Output Structure

The `CrewOutput` class provides structured access to results:

| Attribute | Type | Description |
|-----------|------|-------------|
| `raw` | `str` | Raw output string |
| `pydantic` | `Optional[BaseModel]` | Structured Pydantic output |
| `json_dict` | `Optional[Dict]` | JSON dictionary output |
| `tasks_output` | `List[TaskOutput]` | Individual task outputs |
| `token_usage` | `Dict[str, Any]` | Token usage summary |

```python
crew_output = crew.kickoff()
print(f"Raw: {crew_output.raw}")
print(f"Token Usage: {crew_output.token_usage}")
```

## Sequential vs Hierarchical

### Sequential Process

```
Task 1 → Task 2 → Task 3 → Output
   ↓        ↓        ↓
Agent 1  Agent 2  Agent 3
```

### Hierarchical Process

```
        ┌─────────────────┐
        │  Manager Agent  │
        │   (Delegator)   │
        └────────┬────────┘
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Worker 1 │ │ Worker 2 │ │ Worker 3 │
└──────────┘ └──────────┘ └──────────┘
```
