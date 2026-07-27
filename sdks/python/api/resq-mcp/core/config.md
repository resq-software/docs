<a id="resq_mcp.core.config"></a>

# resq\_mcp.core.config

Configuration management for the ResQ MCP server.

Settings are loaded from environment variables with sensible defaults.
Use a .env file or export environment variables to override.

Environment variables:
    RESQ_PROJECT_NAME: Display name for the MCP server
    RESQ_VERSION: Version string for the server
    RESQ_DEBUG: Enable debug logging (true/false)
    RESQ_API_KEY: API key for authenticated endpoints
    RESQ_TRANSPORT: MCP transport — stdio (default), http, sse, or streamable-http
    RESQ_PORT: Port for HTTP/SSE server
    RESQ_HOST: Host to bind to (HTTP/SSE transports)
    RESQ_SAFE_MODE: If True, side-effecting tools are disabled or mocked safely

<a id="resq_mcp.core.config.annotations"></a>

## annotations

<a id="resq_mcp.core.config.Literal"></a>

## Literal

<a id="resq_mcp.core.config.Field"></a>

## Field

<a id="resq_mcp.core.config.BaseSettings"></a>

## BaseSettings

<a id="resq_mcp.core.config.SettingsConfigDict"></a>

## SettingsConfigDict

<a id="resq_mcp.core.config.DEFAULT_DEV_API_KEY"></a>

#### DEFAULT\_DEV\_API\_KEY

The shipped development fallback token. Treated as "unset" for any deployment
that requires real authentication (see :func:`validate_environment`).

<a id="resq_mcp.core.config.NETWORK_TRANSPORTS"></a>

#### NETWORK\_TRANSPORTS

Transports that open a network listener and therefore must not run with the
default development token. ``stdio`` is excluded — it is spawned by a local
MCP client over the process's stdin/stdout and is not network-reachable.

<a id="resq_mcp.core.config.ConfigurationError"></a>

## ConfigurationError Objects

```python
class ConfigurationError(Exception)
```

Raised when required configuration is missing or invalid.

<a id="resq_mcp.core.config.Settings"></a>

## Settings Objects

```python
class Settings(BaseSettings)
```

Application configuration via environment variables.

<a id="resq_mcp.core.config.Settings.model_config"></a>

#### model\_config

<a id="resq_mcp.core.config.Settings.PROJECT_NAME"></a>

#### PROJECT\_NAME

<a id="resq_mcp.core.config.Settings.VERSION"></a>

#### VERSION

<a id="resq_mcp.core.config.Settings.DEBUG"></a>

#### DEBUG

<a id="resq_mcp.core.config.Settings.API_KEY"></a>

#### API\_KEY

<a id="resq_mcp.core.config.Settings.API_KEY_PREVIOUS"></a>

#### API\_KEY\_PREVIOUS

<a id="resq_mcp.core.config.Settings.API_KEY_GRACE_SECONDS"></a>

#### API\_KEY\_GRACE\_SECONDS

<a id="resq_mcp.core.config.Settings.TRANSPORT"></a>

#### TRANSPORT

<a id="resq_mcp.core.config.Settings.PORT"></a>

#### PORT

<a id="resq_mcp.core.config.Settings.HOST"></a>

#### HOST

<a id="resq_mcp.core.config.Settings.SAFE_MODE"></a>

#### SAFE\_MODE

<a id="resq_mcp.core.config.Settings.AUDIT_ENABLED"></a>

#### AUDIT\_ENABLED

<a id="resq_mcp.core.config.Settings.RATE_LIMIT_ENABLED"></a>

#### RATE\_LIMIT\_ENABLED

<a id="resq_mcp.core.config.Settings.RATE_LIMIT_MAX_CALLS"></a>

#### RATE\_LIMIT\_MAX\_CALLS

<a id="resq_mcp.core.config.Settings.RATE_LIMIT_WINDOW_SECONDS"></a>

#### RATE\_LIMIT\_WINDOW\_SECONDS

<a id="resq_mcp.core.config.Settings.TELEMETRY_BACKEND"></a>

#### TELEMETRY\_BACKEND

<a id="resq_mcp.core.config.Settings.OTEL_EXPORTER_OTLP_ENDPOINT"></a>

#### OTEL\_EXPORTER\_OTLP\_ENDPOINT

<a id="resq_mcp.core.config.Settings.OTEL_SERVICE_NAME"></a>

#### OTEL\_SERVICE\_NAME

<a id="resq_mcp.core.config.settings"></a>

#### settings

<a id="resq_mcp.core.config.validate_environment"></a>

#### validate\_environment

```python
def validate_environment(require_api_key: bool = False) -> None
```

Validate required environment variables at startup.

This function performs fail-fast validation by raising ConfigurationError
if any required environment variables are missing.

**Arguments**:

- `require_api_key` - If True, API_KEY must be set and not be the default dev token.
  Authentication is *also* required automatically whenever a network
  transport (``http``/``sse``/``streamable-http``) is selected, since such
  transports expose a listener that random traffic can reach.
  

**Raises**:

- `ConfigurationError` - If any required environment variable is missing or invalid.
  

**Example**:

  >>> from resq_mcp.core.config import validate_environment
  >>> validate_environment(require_api_key=True)
