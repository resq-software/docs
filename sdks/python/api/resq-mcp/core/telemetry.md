<a id="resq_mcp.core.telemetry"></a>

# resq\_mcp.core.telemetry

Telemetry subsystem for the ResQ MCP server.

Provides unified OpenTelemetry tracing, Prometheus-compatible metrics,
and structured logging with automatic PII redaction.

<a id="resq_mcp.core.telemetry.annotations"></a>

## annotations

<a id="resq_mcp.core.telemetry.functools"></a>

## functools

<a id="resq_mcp.core.telemetry.logging"></a>

## logging

<a id="resq_mcp.core.telemetry.re"></a>

## re

<a id="resq_mcp.core.telemetry.time"></a>

## time

<a id="resq_mcp.core.telemetry.contextmanager"></a>

## contextmanager

<a id="resq_mcp.core.telemetry.TYPE_CHECKING"></a>

## TYPE\_CHECKING

<a id="resq_mcp.core.telemetry.Any"></a>

## Any

<a id="resq_mcp.core.telemetry.ParamSpec"></a>

## ParamSpec

<a id="resq_mcp.core.telemetry.TypeVar"></a>

## TypeVar

<a id="resq_mcp.core.telemetry.settings"></a>

## settings

<a id="resq_mcp.core.telemetry.P"></a>

#### P

<a id="resq_mcp.core.telemetry.R"></a>

#### R

<a id="resq_mcp.core.telemetry.logger"></a>

#### logger

<a id="resq_mcp.core.telemetry.tracer"></a>

#### tracer

<a id="resq_mcp.core.telemetry.meter"></a>

#### meter

<a id="resq_mcp.core.telemetry.setup_telemetry"></a>

#### setup\_telemetry

```python
def setup_telemetry() -> None
```

Initialize OpenTelemetry tracing and metrics.

<a id="resq_mcp.core.telemetry.metrics"></a>

#### metrics

<a id="resq_mcp.core.telemetry.trace"></a>

#### trace

```python
def trace(_func_or_name: Callable[P, R] | str | None = None,
          name: str | None = None,
          *,
          record_args: bool = False,
          record_result: bool = False) -> Any
```

Instrument a function with an OpenTelemetry span.

<a id="resq_mcp.core.telemetry.span"></a>

#### span

```python
@contextmanager
def span(name: str,
         attributes: dict[str, Any] | None = None) -> Generator[Any]
```

<a id="resq_mcp.core.telemetry.log_event"></a>

#### log\_event

```python
def log_event(event: str, level: int = logging.INFO, **attrs: Any) -> None
```

<a id="resq_mcp.core.telemetry.shutdown_telemetry"></a>

#### shutdown\_telemetry

```python
def shutdown_telemetry(timeout_ms: int = 5_000) -> None
```
