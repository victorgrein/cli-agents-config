# CrewAI Processes - Full Reference

> Source: Official CrewAI Documentation

## Process Types Overview

Processes in CrewAI define how tasks are executed and how agents collaborate. The process type determines the flow of work through the crew.

## Sequential Process (Default)

Tasks execute one after another in the order they are defined.

### Context Passing

Each task can access outputs from previous tasks:

```python
task1 = Task(
    description="Research the topic",
    expected_output="Research findings",
    agent=researcher
)

task2 = Task(
    description="Analyze the research findings",
    expected_output="Analysis report",
    agent=analyst,
    context=[task1]  # Explicitly receive task1 output
)

task3 = Task(
    description="Write based on research and analysis",
    expected_output="Final document",
    agent=writer,
    context=[task1, task2]  # Receive both outputs
)
```

## Hierarchical Process

### Manager Responsibilities

1. **Task Analysis**: Understand task requirements
2. **Delegation**: Assign tasks to appropriate agents
3. **Coordination**: Manage dependencies and order
4. **Validation**: Review and approve outputs
5. **Iteration**: Request revisions if needed

## Comparison Table

| Aspect | Sequential | Hierarchical |
|--------|------------|--------------|
| **Complexity** | Simple | Complex |
| **Control** | Predictable | Dynamic |
| **Coordination** | Implicit (order) | Explicit (manager) |
| **Validation** | None built-in | Manager validates |
| **Best For** | Linear workflows | Complex projects |
| **Requirements** | None | manager_llm or manager_agent |
| **Token Usage** | Lower | Higher (manager overhead) |
