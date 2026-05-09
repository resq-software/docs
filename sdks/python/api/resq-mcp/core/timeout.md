<a id="resq_mcp.core.timeout"></a>

# resq\_mcp.core.timeout

Centralized timeout configuration for ResQ MCP server.

Provides consistent, env-var-configurable timeout values across all tools.
Inspired by Archon MCP server timeout patterns.

Environment variables:
    RESQ_REQUEST_TIMEOUT: Total request timeout in seconds (default: 30)
    RESQ_CONNECT_TIMEOUT: Connection timeout in seconds (default: 5)
    RESQ_READ_TIMEOUT: Read timeout in seconds (default: 20)
    RESQ_POLLING_BASE_INTERVAL: Base polling interval in seconds (default: 1)
    RESQ_POLLING_MAX_INTERVAL: Max polling interval in seconds (default: 5)
    RESQ_MAX_POLLING_ATTEMPTS: Max polling attempts (default: 30)

<a id="resq_mcp.core.timeout.annotations"></a>

## annotations

<a id="resq_mcp.core.timeout.os"></a>

## os

<a id="resq_mcp.core.timeout.dataclass"></a>

## dataclass

<a id="resq_mcp.core.timeout.TimeoutConfig"></a>

## TimeoutConfig Objects

```python
@dataclass(frozen=True)
class TimeoutConfig()
```

Immutable timeout configuration.

<a id="resq_mcp.core.timeout.TimeoutConfig.total"></a>

#### total

<a id="resq_mcp.core.timeout.TimeoutConfig.connect"></a>

#### connect

<a id="resq_mcp.core.timeout.TimeoutConfig.read"></a>

#### read

<a id="resq_mcp.core.timeout.get_default_timeout"></a>

#### get\_default\_timeout

```python
def get_default_timeout() -> TimeoutConfig
```

Get default timeout configuration from environment or defaults.

<a id="resq_mcp.core.timeout.get_max_polling_attempts"></a>

#### get\_max\_polling\_attempts

```python
def get_max_polling_attempts() -> int
```

Get maximum number of polling attempts.

<a id="resq_mcp.core.timeout.get_polling_interval"></a>

#### get\_polling\_interval

```python
def get_polling_interval(attempt: int) -> float
```

Get polling interval with exponential backoff.

**Arguments**:

- `attempt` - Current attempt number (0-based).
  

**Returns**:

  Sleep interval in seconds.
