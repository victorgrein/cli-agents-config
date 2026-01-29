---
name: crewai-flows
description: Create CrewAI flows with state management, routing, persistence, and crew orchestration using decorators
license: MIT
compatibility: opencode
metadata:
  category: crewai-concept
  audience: developers
  complexity: advanced
---

## What This Skill Does

Provides comprehensive guidance for creating CrewAI Flows - a powerful feature for building sophisticated AI workflows. Flows allow combining crews and tasks with state management, event-driven architecture, and flexible control flow.

## When to Use This Skill

- Creating multi-step AI workflows
- Orchestrating multiple crews together
- Implementing state management across tasks
- Adding conditional routing logic
- Building parallel execution patterns
- Implementing human-in-the-loop approval
- Creating persistent workflows

## Quick Reference

### Key Benefits

1. **Simplified Workflow Creation**: Chain multiple Crews and tasks
2. **State Management**: Easy state sharing between tasks
3. **Event-Driven Architecture**: Dynamic and responsive workflows
4. **Flexible Control Flow**: Conditional logic, loops, branching

### Core Decorators

| Decorator | Purpose |
|-----------|---------|
| `@start()` | Marks entry points for a Flow |
| `@listen()` | Listens for output of another task |
| `@router()` | Defines conditional routing logic |

### Conditional Logic

| Function | Purpose |
|----------|---------|
| `or_()` | Trigger when ANY specified methods emit |
| `and_()` | Trigger when ALL specified methods emit |

## Basic Flow Pattern

```python
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class MyFlowState(BaseModel):
    input_data: str = ""
    result: str = ""

class MyFlow(Flow[MyFlowState]):
    @start()
    def begin(self):
        return self.state.input_data
    
    @listen(begin)
    def process(self, data):
        self.state.result = f"Processed: {data}"
        return self.state.result

def kickoff():
    flow = MyFlow()
    result = flow.kickoff(inputs={"input_data": "test"})
    print(result)
```

## Flow with Crew Integration

```python
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel
from .crews.research_crew.research_crew import ResearchCrew
from .crews.writing_crew.writing_crew import WritingCrew

class ContentFlowState(BaseModel):
    topic: str = ""
    research: str = ""
    article: str = ""

class ContentFlow(Flow[ContentFlowState]):
    @start()
    def prepare(self):
        print(f"Starting content flow for: {self.state.topic}")
        return {"topic": self.state.topic}
    
    @listen(prepare)
    def run_research(self, inputs):
        result = ResearchCrew().crew().kickoff(inputs=inputs)
        self.state.research = result.raw
        return {"topic": self.state.topic, "research": result.raw}
    
    @listen(run_research)
    def run_writing(self, inputs):
        result = WritingCrew().crew().kickoff(inputs=inputs)
        self.state.article = result.raw
        return result.raw

def kickoff():
    flow = ContentFlow()
    result = flow.kickoff(inputs={"topic": "AI trends"})
    print(f"Article: {result}")

def plot():
    flow = ContentFlow()
    flow.plot("content_flow")
```

## Flow with Router (Conditional Logic)

```python
from crewai.flow.flow import Flow, listen, router, start
from pydantic import BaseModel

class ReviewFlowState(BaseModel):
    content: str = ""
    quality_score: int = 0
    final_content: str = ""

class ReviewFlow(Flow[ReviewFlowState]):
    @start()
    def generate_content(self):
        self.state.content = "Generated content..."
        return self.state.content
    
    @listen(generate_content)
    def assess_quality(self, content):
        self.state.quality_score = 85  # Example score
        return self.state.quality_score
    
    @router(assess_quality)
    def route_by_quality(self):
        if self.state.quality_score >= 80:
            return "publish"
        elif self.state.quality_score >= 60:
            return "revise"
        else:
            return "reject"
    
    @listen("publish")
    def publish_content(self):
        self.state.final_content = self.state.content
        print("Content published!")
        return self.state.final_content
    
    @listen("revise")
    def revise_content(self):
        self.state.content = "Revised content..."
        return self.state.content
    
    @listen("reject")
    def reject_content(self):
        print("Content rejected, starting over...")
        return None
```

## Flow with Parallel Execution

```python
from crewai.flow.flow import Flow, listen, start, and_
from pydantic import BaseModel
from typing import List

class ParallelFlowState(BaseModel):
    topics: List[str] = []
    research_a: str = ""
    research_b: str = ""
    combined: str = ""

class ParallelFlow(Flow[ParallelFlowState]):
    @start()
    def begin(self):
        return self.state.topics
    
    @listen(begin)
    def research_topic_a(self, topics):
        self.state.research_a = f"Research on {topics[0]}"
        return self.state.research_a
    
    @listen(begin)
    def research_topic_b(self, topics):
        # Runs in parallel with research_topic_a
        self.state.research_b = f"Research on {topics[1]}"
        return self.state.research_b
    
    @listen(and_(research_topic_a, research_topic_b))
    def combine_research(self):
        # Runs after BOTH complete
        self.state.combined = f"{self.state.research_a}\n{self.state.research_b}"
        return self.state.combined
```

## State Management

### Structured State (Recommended)

```python
from pydantic import BaseModel

class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""

class StructuredFlow(Flow[ExampleState]):
    @start()
    def first_method(self):
        self.state.message = "Hello from structured flow"
        self.state.counter += 1
```

### Unstructured State

```python
class UnstructuredFlow(Flow):
    @start()
    def first_method(self):
        self.state['counter'] = 0
        self.state['message'] = "Hello"
```

## Flow Persistence

```python
from crewai.flow.flow import Flow, persist

@persist  # Class-level persistence
class MyFlow(Flow[MyState]):
    @start()
    def initialize_flow(self):
        self.state.counter = 1
```

## Human-in-the-Loop

```python
from crewai.flow.human_feedback import human_feedback, HumanFeedbackResult

@start()
@human_feedback(
    message="Do you approve this content?",
    emit=["approved", "rejected"],
    llm="gpt-4o-mini",
    default_outcome="needs_revision",
)
def generate_content(self):
    return "Content to be reviewed..."

@listen("approved")
def on_approval(self, result: HumanFeedbackResult):
    print(f"Approved! Feedback: {result.feedback}")
```

## Running Flows

```bash
# Using CLI
crewai run
# or
crewai flow kickoff

# Using uv
uv run kickoff
```

## Visualization

```python
flow = MyFlow()
flow.plot("my_flow_diagram")  # Generates HTML visualization
```

## Flow Project Structure

```
my_flow/
├── crews/
│   └── poem_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── poem_crew.py
├── tools/
│   └── custom_tool.py
├── main.py
├── pyproject.toml
└── README.md
```

## Best Practices

1. **Use Pydantic State**: Type-safe, validated state
2. **Clear Method Names**: Describe what each step does
3. **State Updates**: Update state in each method
4. **Error Handling**: Handle failures gracefully
5. **Visualization**: Use plot() for debugging
6. **Persistence**: Enable for long-running flows

## Related Skills

- `crewai-crews` - Creating crews for flows
- `crewai-agents` - Agent configuration
- `crewai-tasks` - Task configuration
- `crewai-project-structure` - Flow project structure
