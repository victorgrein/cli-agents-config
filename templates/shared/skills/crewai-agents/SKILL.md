---
name: crewai-agents
description: Create and configure CrewAI agents with roles, goals, backstories, tools, and LLM settings
license: MIT
compatibility: opencode
metadata:
  category: crewai-concept
  audience: developers
  complexity: moderate
---

## What This Skill Does

Provides comprehensive guidance for creating CrewAI agents - autonomous units that perform tasks, make decisions, use tools, and collaborate with other agents. Includes agent archetypes, configuration patterns, and best practices.

## When to Use This Skill

- Creating a new agent for a crew
- Configuring agent attributes (role, goal, backstory)
- Setting up LLM configuration for agents
- Enabling agent features (memory, reasoning, code execution)
- Designing agent archetypes (researcher, developer, analyst)
- Direct agent interaction with `kickoff()`

## Quick Reference

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

### Behavior Settings

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `verbose` | `bool` | False | Enable detailed logging |
| `allow_delegation` | `bool` | False | Allow delegating to other agents |
| `max_iter` | `int` | 20 | Max iterations before best answer |
| `max_rpm` | `Optional[int]` | None | Rate limit for API calls |
| `memory` | `bool` | False | Maintain conversation history |
| `cache` | `bool` | True | Cache tool results |
| `reasoning` | `bool` | False | Enable planning before execution |

### YAML Configuration Pattern

```yaml
# config/agents.yaml
researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.
```

```python
@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config['researcher'],
        tools=[SerperDevTool()],
        verbose=True
    )
```

## Agent Archetypes

### Research Agent

```python
researcher = Agent(
    role="Research Analyst",
    goal="Find and summarize information about specific topics",
    backstory="Experienced researcher with attention to detail",
    tools=[SerperDevTool()],
    verbose=True
)
```

### Code Development Agent

```python
developer = Agent(
    role="Senior Python Developer",
    goal="Write and debug Python code",
    backstory="Expert Python developer with 10 years of experience",
    allow_code_execution=True,
    code_execution_mode="safe",
    max_execution_time=300,
    max_retry_limit=3
)
```

### Analysis Agent

```python
analyst = Agent(
    role="Data Analyst",
    goal="Perform deep analysis of large datasets",
    backstory="Specialized in big data analysis",
    memory=True,
    respect_context_window=True,
    max_rpm=10,
    function_calling_llm="gpt-4o-mini"
)
```

### Reasoning Agent

```python
strategic_agent = Agent(
    role="Strategic Planner",
    goal="Analyze complex problems and create execution plans",
    backstory="Expert strategic planner",
    reasoning=True,
    max_reasoning_attempts=3,
    max_iter=30,
    verbose=True
)
```

## Direct Agent Interaction

Use `kickoff()` for direct agent interaction without crew:

```python
result = agent.kickoff("What are the latest developments in AI?")
print(result.raw)

# With structured output
class ResearchFindings(BaseModel):
    main_points: List[str]
    key_technologies: List[str]

result = agent.kickoff(
    "Summarize AI developments",
    response_format=ResearchFindings
)
print(result.pydantic.main_points)

# Async
result = await agent.kickoff_async("Query here")
```

## Best Practices

1. **Role Design**: Be specific about expertise area and seniority
2. **Goal Design**: Focus on outcomes, be measurable
3. **Backstory Design**: Provide relevant context, keep concise (2-4 sentences)
4. **Tool Assignment**: Match tools to agent's purpose
5. **Memory**: Enable for complex, multi-step tasks
6. **Rate Limiting**: Set `max_rpm` to avoid API limits
7. **Caching**: Keep enabled for repetitive operations

## Templates

### Basic Agent YAML Template

```yaml
agent_name:
  role: >
    {Role title with expertise area}
  goal: >
    {Specific, measurable objective}
  backstory: >
    {Context and personality in 2-4 sentences}
```

### Domain-Specific Templates

#### AI/ML Researcher

```yaml
ai_researcher:
  role: >
    AI/ML Research Specialist
  goal: >
    Research and analyze the latest developments in artificial
    intelligence and machine learning, focusing on practical applications
  backstory: >
    You're a researcher with deep expertise in AI/ML technologies.
    You stay current with the latest papers, tools, and frameworks,
    and can explain complex concepts clearly.
```

#### Code Reviewer

```yaml
code_reviewer:
  role: >
    Senior Code Review Specialist
  goal: >
    Review code for quality, security, and best practices,
    providing actionable feedback for improvement
  backstory: >
    You're an experienced developer who specializes in code
    review. You identify issues, suggest improvements, and
    help maintain high code quality standards.
```

## Related Skills

- `crewai-tasks` - Task configuration for agents
- `crewai-crews` - Assembling agents into crews
- `crewai-tools` - Creating tools for agents
- `crewai-llms` - LLM configuration and optimization
