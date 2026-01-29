---
name: crewai-tools
description: Create custom tools and use built-in tools for CrewAI agents with proper error handling and caching
license: MIT
compatibility: opencode
metadata:
  category: crewai-concept
  audience: developers
  complexity: moderate
---

## What This Skill Does

Provides comprehensive guidance for creating and using CrewAI tools - capabilities that empower agents with web searching, data analysis, file operations, and more. Includes built-in tools, custom tool creation, and async tool patterns.

## When to Use This Skill

- Creating custom tools for agents
- Using built-in tools (search, file, database)
- Implementing async tools
- Setting up tool caching
- Writing effective tool descriptions
- Handling tool errors gracefully

## Quick Reference

### Key Characteristics

- **Utility**: Web searching, data analysis, content generation
- **Integration**: Seamlessly integrate into agent workflows
- **Customizability**: Create custom tools or use existing ones
- **Error Handling**: Robust error handling mechanisms
- **Caching**: Intelligent caching to optimize performance
- **Async Support**: Both synchronous and asynchronous tools

### Installation

```bash
pip install 'crewai[tools]'
```

## Built-in Tools

### Search & Research

| Tool | Description |
|------|-------------|
| `SerperDevTool` | Web search via Serper API |
| `WebsiteSearchTool` | RAG-based website search |
| `GithubSearchTool` | Search GitHub repositories |
| `WikipediaTools` | Wikipedia search |
| `EXASearchTool` | Exhaustive data source search |

### File & Document

| Tool | Description |
|------|-------------|
| `FileReadTool` | Read file contents |
| `FileWriteTool` | Write to files |
| `DirectoryReadTool` | Read directory contents |
| `PDFSearchTool` | Search PDF documents |
| `CSVSearchTool` | Search CSV files |
| `JSONSearchTool` | Search JSON files |

### Database

| Tool | Description |
|------|-------------|
| `PGSearchTool` | PostgreSQL search |
| `MySQLTool` | MySQL operations |
| `NL2SQLTool` | Natural language to SQL |

### Web Scraping

| Tool | Description |
|------|-------------|
| `ScrapeWebsiteTool` | Scrape entire websites |
| `SeleniumScrapingTool` | Browser-based scraping |
| `FirecrawlScrapeWebsiteTool` | Firecrawl scraping |

### AI & Code

| Tool | Description |
|------|-------------|
| `CodeInterpreterTool` | Execute Python code |
| `RagTool` | General RAG operations |
| `VisionTool` | Image analysis |

## Creating Custom Tools

### Using BaseTool Subclass

```python
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MyToolInput(BaseModel):
    """Input schema for MyTool."""
    query: str = Field(..., description="The search query")
    limit: int = Field(default=10, description="Max results to return")

class MyCustomTool(BaseTool):
    name: str = "my_custom_tool"
    description: str = """
    Searches for data based on query.
    Use this when you need to find specific information.
    """
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self, query: str, limit: int = 10) -> str:
        try:
            # Tool implementation
            results = self._search(query, limit)
            return f"Found {len(results)} results: {results}"
        except Exception as e:
            return f"Error: {str(e)}"
```

### Using @tool Decorator

```python
from crewai.tools import tool

@tool("calculate_metrics")
def calculate_metrics(data: str) -> str:
    """Calculate key metrics from the provided data.
    
    Use this when you need to compute statistics or metrics.
    
    Args:
        data: JSON string containing the data to analyze
    """
    try:
        import json
        parsed = json.loads(data)
        # Calculate metrics
        return f"Metrics calculated: {metrics}"
    except Exception as e:
        return f"Error: {str(e)}"
```

## Async Tools

### Async with Decorator

```python
@tool("fetch_data_async")
async def fetch_data_async(query: str) -> str:
    """Asynchronously fetch data based on the query."""
    await asyncio.sleep(1)  # Simulate async operation
    return f"Data retrieved for {query}"
```

### Async with BaseTool

```python
class AsyncAPITool(BaseTool):
    name: str = "async_api_tool"
    description: str = "Fetches data from external API asynchronously"

    async def _run(self, endpoint: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                data = await response.json()
                return str(data)
```

## Custom Caching

```python
@tool
def expensive_operation(query: str) -> str:
    """Performs an expensive operation."""
    return result

def cache_func(args, result):
    # Only cache if result doesn't contain error
    return "error" not in result.lower()

expensive_operation.cache_function = cache_func
```

## Using Tools with Agents

```python
from crewai import Agent
from crewai_tools import SerperDevTool, FileReadTool

search_tool = SerperDevTool()
file_tool = FileReadTool()

researcher = Agent(
    role="Research Analyst",
    goal="Find and analyze information",
    backstory="Expert researcher",
    tools=[search_tool, file_tool],
    verbose=True
)
```

## Tool Description Guidelines

**Good description:**
```python
description = """
Use this tool to search the web for current information.
Best for: Finding recent news, articles, and data.
Input: A search query string.
Output: List of relevant search results with titles and snippets.
"""
```

**Bad description:**
```python
description = "Searches the web"  # Too vague
```

## Best Practices

1. **Clear Descriptions**: Agents use descriptions to decide which tool to use
2. **Error Handling**: Always wrap operations in try/except, return error strings
3. **Input Validation**: Use Pydantic models with Field descriptions
4. **Caching**: Enable for expensive operations
5. **Async**: Use for I/O-bound operations
6. **Rate Limiting**: Consider API limits in tool implementation

## Related Skills

- `crewai-agents` - Assigning tools to agents
- `crewai-tasks` - Task-specific tool overrides
- `crewai-debugging` - Debugging tool issues
