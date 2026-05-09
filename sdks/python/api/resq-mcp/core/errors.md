<a id="resq_mcp.core.errors"></a>

# resq\_mcp.core.errors

Structured error handling for ResQ MCP tools.

Provides consistent, AI-client-friendly error responses with actionable
context. Inspired by Archon MCP server error handling patterns.

<a id="resq_mcp.core.errors.annotations"></a>

## annotations

<a id="resq_mcp.core.errors.json"></a>

## json

<a id="resq_mcp.core.errors.Any"></a>

## Any

<a id="resq_mcp.core.errors.MCPErrorFormatter"></a>

## MCPErrorFormatter Objects

```python
class MCPErrorFormatter()
```

Formats errors consistently for MCP AI clients.

<a id="resq_mcp.core.errors.MCPErrorFormatter.format_error"></a>

#### MCPErrorFormatter.format\_error

```python
@staticmethod
def format_error(error_type: str,
                 message: str,
                 details: dict[str, Any] | None = None,
                 suggestion: str | None = None,
                 http_status: int | None = None) -> str
```

Format a structured error response as JSON.

<a id="resq_mcp.core.errors.MCPErrorFormatter.from_exception"></a>

#### MCPErrorFormatter.from\_exception

```python
@staticmethod
def from_exception(exception: Exception,
                   operation: str,
                   context: dict[str, Any] | None = None) -> str
```

Format error from a Python exception.
