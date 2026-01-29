# CrewAI Tools - Full Reference

> Source: Official CrewAI Documentation

## Complete Built-in Tools List

### Search & Research

| Tool | Description |
|------|-------------|
| `SerperDevTool` | Web search via Serper API |
| `WebsiteSearchTool` | RAG-based website search |
| `GithubSearchTool` | Search GitHub repositories |
| `WikipediaTools` | Wikipedia search |
| `YoutubeChannelSearchTool` | YouTube channel search |
| `YoutubeVideoSearchTool` | YouTube video search |
| `EXASearchTool` | Exhaustive data source search |

### File & Document

| Tool | Description |
|------|-------------|
| `FileReadTool` | Read file contents |
| `FileWriteTool` | Write to files |
| `DirectoryReadTool` | Read directory contents |
| `DirectorySearchTool` | Search within directories |
| `PDFSearchTool` | Search PDF documents |
| `CSVSearchTool` | Search CSV files |
| `JSONSearchTool` | Search JSON files |
| `DOCXSearchTool` | Search Word documents |
| `TXTSearchTool` | Search text files |
| `MDXSearchTool` | Search Markdown files |
| `XMLSearchTool` | Search XML files |

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
| `ScrapeElementFromWebsiteTool` | Scrape specific elements |
| `SeleniumScrapingTool` | Browser-based scraping |
| `FirecrawlScrapeWebsiteTool` | Firecrawl scraping |
| `FirecrawlCrawlWebsiteTool` | Firecrawl crawling |

### AI & Code

| Tool | Description |
|------|-------------|
| `CodeInterpreterTool` | Execute Python code |
| `RagTool` | General RAG operations |
| `VisionTool` | Image analysis |
| `DALL-E Tool` | Image generation |
| `LlamaIndexTool` | LlamaIndex integration |

## Tool Input Schema Example

```python
from pydantic import BaseModel, Field
from typing import Type

class MyToolInput(BaseModel):
    """Input schema for MyTool."""
    query: str = Field(..., description="The search query")
    limit: int = Field(default=10, description="Max results to return")

class MyCustomTool(BaseTool):
    name: str = "my_custom_tool"
    description: str = "Searches for data"
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self, query: str, limit: int = 10) -> str:
        try:
            results = self._perform_search(query)
            return f"Results: {results}"
        except Exception as e:
            return f"Error: {str(e)}"
```
