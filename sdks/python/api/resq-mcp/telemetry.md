<a id="resq_mcp.telemetry"></a>

# resq\_mcp.telemetry

Telemetry setup for the ResQ MCP server.

Provides initialization hooks for OpenTelemetry tracing and metrics.
Currently operates in no-op mode with structured logging as a fallback.

Future integration path:
    1. Install: opentelemetry-api, opentelemetry-sdk, opentelemetry-exporter-otlp
    2. Configure TracerProvider with appropriate exporters
    3. Configure MeterProvider for Prometheus metrics
    4. Add trace decorators to key operations

<a id="resq_mcp.telemetry.annotations"></a>

## annotations

<a id="resq_mcp.telemetry.logging"></a>

## logging

<a id="resq_mcp.telemetry.TYPE_CHECKING"></a>

## TYPE\_CHECKING

<a id="resq_mcp.telemetry.settings"></a>

## settings

<a id="resq_mcp.telemetry.logger"></a>

#### logger

<a id="resq_mcp.telemetry.setup_telemetry"></a>

#### setup\_telemetry

```python
def setup_telemetry() -> None
```

Initialize OpenTelemetry tracing and metrics.

Currently operates in no-op mode. When DEBUG is enabled, logs the
initialization for visibility.

<a id="resq_mcp.telemetry.trace"></a>

#### trace

```python
def trace(name: str | None = None) -> Callable[[F], F]
```

Decorator stub for tracing function execution.

**Arguments**:

- `name` - Optional span name. Defaults to the function name.
  

**Returns**:

  A no-op decorator that returns the original function.
  

**Example**:

  @trace("custom.operation.name")
  def my_function():
  ...
