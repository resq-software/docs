<a id="resq_mcp.core.ratelimit"></a>

# resq\_mcp.core.ratelimit

Per-tool rate limiting for the ResQ MCP server.

Implements the "Denial of service and fatigue-based techniques" mitigation from
NSA PP-26-1834 (May 2026): MCP servers acting as agent orchestrators are
susceptible to prompt storms and recursive task requests that exhaust resources.
A sliding-window limiter keyed per tool bounds the call rate so a single tool
cannot be hammered into a denial-of-service condition.

The limiter is process-local and in-memory: each worker process keeps its own
counters. It therefore does not enforce an aggregate limit across multiple worker
processes on a single host, nor across replicas — a client can dilute the limit by
spreading calls over workers or instances. Any deployment that runs more than one
worker should back the limiter with a shared store (e.g. Redis) so the limit holds
globally rather than per process.

<a id="resq_mcp.core.ratelimit.annotations"></a>

## annotations

<a id="resq_mcp.core.ratelimit.threading"></a>

## threading

<a id="resq_mcp.core.ratelimit.time"></a>

## time

<a id="resq_mcp.core.ratelimit.defaultdict"></a>

## defaultdict

<a id="resq_mcp.core.ratelimit.deque"></a>

## deque

<a id="resq_mcp.core.ratelimit.settings"></a>

## settings

<a id="resq_mcp.core.ratelimit.RateLimitExceeded"></a>

## RateLimitExceeded Objects

```python
class RateLimitExceeded(Exception)
```

Raised when a tool exceeds its allowed call rate within the window.

<a id="resq_mcp.core.ratelimit.RateLimitExceeded.__init__"></a>

#### RateLimitExceeded.\_\_init\_\_

```python
def __init__(tool: str, limit: int, window_seconds: int) -> None
```

<a id="resq_mcp.core.ratelimit.RateLimiter"></a>

## RateLimiter Objects

```python
class RateLimiter()
```

Thread-safe sliding-window rate limiter keyed by an arbitrary string.

Each key (typically a tool name) tracks the monotonic timestamps of recent
calls. On ``check`` the window is pruned and the call rejected if the number
of in-window calls has reached the limit.

<a id="resq_mcp.core.ratelimit.RateLimiter.__init__"></a>

#### RateLimiter.\_\_init\_\_

```python
def __init__(max_calls: int | None = None,
             window_seconds: int | None = None) -> None
```

Initialise the limiter.

**Arguments**:

- `max_calls` - Maximum number of calls permitted per key per window. When
  ``None`` the value is read live from ``settings.RATE_LIMIT_MAX_CALLS``
  so runtime configuration changes take effect without re-instantiation.
- `window_seconds` - Width of the sliding window, in seconds. When ``None`` the
  value is read live from ``settings.RATE_LIMIT_WINDOW_SECONDS``.

<a id="resq_mcp.core.ratelimit.RateLimiter.max_calls"></a>

#### RateLimiter.max\_calls

```python
@property
def max_calls() -> int
```

Effective per-window call cap (explicit override or live setting).

<a id="resq_mcp.core.ratelimit.RateLimiter.max_calls"></a>

#### RateLimiter.max\_calls

```python
@max_calls.setter
def max_calls(value: int) -> None
```

<a id="resq_mcp.core.ratelimit.RateLimiter.window_seconds"></a>

#### RateLimiter.window\_seconds

```python
@property
def window_seconds() -> int
```

Effective window width in seconds (explicit override or live setting).

<a id="resq_mcp.core.ratelimit.RateLimiter.window_seconds"></a>

#### RateLimiter.window\_seconds

```python
@window_seconds.setter
def window_seconds(value: int) -> None
```

<a id="resq_mcp.core.ratelimit.RateLimiter.check"></a>

#### RateLimiter.check

```python
def check(key: str, *, now: float | None = None) -> None
```

Record a call for ``key`` and raise if it breaches the limit.

**Arguments**:

- `key` - The bucket key (e.g. a tool name).
- `now` - Optional monotonic timestamp override (for deterministic tests).
  

**Raises**:

- `RateLimitExceeded` - If the limit for ``key`` has already been reached
  within the current window. The call is *not* recorded in that case.

<a id="resq_mcp.core.ratelimit.RateLimiter.reset"></a>

#### RateLimiter.reset

```python
def reset(key: str | None = None) -> None
```

Clear recorded calls for one key, or all keys when ``key`` is ``None``.

<a id="resq_mcp.core.ratelimit.rate_limiter"></a>

#### rate\_limiter

<a id="resq_mcp.core.ratelimit.enforce_rate_limit"></a>

#### enforce\_rate\_limit

```python
def enforce_rate_limit(tool: str) -> None
```

Enforce the configured per-tool rate limit, honouring the feature flag.

**Arguments**:

- `tool` - The tool name used as the limiter key.
  

**Raises**:

- `RateLimitExceeded` - If the tool has exceeded its limit and rate limiting
  is enabled (``RESQ_RATE_LIMIT_ENABLED``).
