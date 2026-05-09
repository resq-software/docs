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
    RESQ_PORT: Port for SSE server
    RESQ_HOST: Host to bind to
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

<a id="resq_mcp.core.config.Settings.PORT"></a>

#### PORT

<a id="resq_mcp.core.config.Settings.HOST"></a>

#### HOST

<a id="resq_mcp.core.config.Settings.SAFE_MODE"></a>

#### SAFE\_MODE

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
  

**Raises**:

- `ConfigurationError` - If any required environment variable is missing or invalid.
  

**Example**:

  >>> from resq_mcp.core.config import validate_environment
  >>> validate_environment(require_api_key=True)
