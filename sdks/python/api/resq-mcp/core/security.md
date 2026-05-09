<a id="resq_mcp.core.security"></a>

# resq\_mcp.core.security

Security utilities for the ResQ MCP server.

Provides API key verification for authenticated endpoints using FastAPI's
HTTPBearer security scheme for token extraction.

**Notes**:

  This implementation uses a simple comparison against the configured API_KEY.
  Production deployments should use secure token storage and validation.

<a id="resq_mcp.core.security.annotations"></a>

## annotations

<a id="resq_mcp.core.security.logging"></a>

## logging

<a id="resq_mcp.core.security.secrets"></a>

## secrets

<a id="resq_mcp.core.security.HTTPException"></a>

## HTTPException

<a id="resq_mcp.core.security.Request"></a>

## Request

<a id="resq_mcp.core.security.status"></a>

## status

<a id="resq_mcp.core.security.HTTPBearer"></a>

## HTTPBearer

<a id="resq_mcp.core.security.settings"></a>

## settings

<a id="resq_mcp.core.security.logger"></a>

#### logger

<a id="resq_mcp.core.security.security_scheme"></a>

#### security\_scheme

<a id="resq_mcp.core.security.verify_api_key"></a>

#### verify\_api\_key

```python
def verify_api_key(request: Request) -> str
```

Verify the Bearer token against the configured API_KEY.

Used as a dependency for SSE endpoints if wrapping in FastAPI.
For FastMCP's SSE adapter, authentication may need to be handled
at the deployment level (Ingress/Gateway) for strict OAuth.

**Arguments**:

- `request` - The incoming FastAPI request.
  

**Returns**:

  The validated API token.
  

**Raises**:

- `HTTPException` - 401 if missing/invalid auth scheme, 403 if invalid key.
