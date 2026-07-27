<a id="resq_mcp.core.security"></a>

# resq\_mcp.core.security

Security utilities for the ResQ MCP server.

Provides API key verification for authenticated endpoints using FastAPI's
HTTPBearer security scheme for token extraction.

**Notes**:

  Tokens are verified against a :class:`KeyRing` (the module-level ``key_ring``)
  using constant-time comparison, with zero-downtime rotation and a
  grace-windowed previous token. The ring is seeded from ``API_KEY`` /
  ``API_KEY_PREVIOUS``. For strict OAuth, terminate authentication at the
  gateway/ingress rather than relying on this bearer check alone.

<a id="resq_mcp.core.security.annotations"></a>

## annotations

<a id="resq_mcp.core.security.logging"></a>

## logging

<a id="resq_mcp.core.security.secrets"></a>

## secrets

<a id="resq_mcp.core.security.threading"></a>

## threading

<a id="resq_mcp.core.security.time"></a>

## time

<a id="resq_mcp.core.security.HTTPException"></a>

## HTTPException

<a id="resq_mcp.core.security.Request"></a>

## Request

<a id="resq_mcp.core.security.status"></a>

## status

<a id="resq_mcp.core.security.HTTPBearer"></a>

## HTTPBearer

<a id="resq_mcp.core.security.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.core.security.settings"></a>

## settings

<a id="resq_mcp.core.security.logger"></a>

#### logger

<a id="resq_mcp.core.security.security_scheme"></a>

#### security\_scheme

<a id="resq_mcp.core.security.KeyRing"></a>

## KeyRing Objects

```python
class KeyRing()
```

Holds the active bearer token plus a grace-windowed previous token.

Supports zero-downtime rotation: :meth:`rotate` promotes a freshly generated
(or supplied) token to active and demotes the prior active token to a
``previous`` slot that stays valid for ``grace_seconds``. In-flight clients
can keep using the old token until they pick up the new one, after which the
previous token silently expires. This addresses the token-lifecycle gaps
(rotation/revocation) flagged in NSA PP-26-1834.

All comparisons use :func:`secrets.compare_digest` for constant-time matching.

<a id="resq_mcp.core.security.KeyRing.__init__"></a>

#### KeyRing.\_\_init\_\_

```python
def __init__(active: str,
             previous: str = "",
             grace_seconds: int = 3600) -> None
```

Initialise the ring.

**Arguments**:

- `active` - The currently active bearer token.
- `previous` - An optional previously active token to honour during a grace
  window (empty disables the previous slot).
- `grace_seconds` - How long a rotated-out token remains acceptable.

<a id="resq_mcp.core.security.KeyRing.active"></a>

#### KeyRing.active

```python
@property
def active() -> str
```

The currently active bearer token.

<a id="resq_mcp.core.security.KeyRing.rotate"></a>

#### KeyRing.rotate

```python
def rotate(new_key: str | None = None) -> str
```

Rotate the active token, keeping the prior one valid during the grace window.

**Arguments**:

- `new_key` - The replacement token. When omitted, a cryptographically
  secure URL-safe token is generated.
  

**Returns**:

  The new active token.

<a id="resq_mcp.core.security.KeyRing.verify"></a>

#### KeyRing.verify

```python
def verify(token: str) -> bool
```

Return True if ``token`` matches the active or (unexpired) previous token.

Reads are taken under the lock so a concurrent :meth:`rotate` cannot expose
a torn view of the active/previous slots (which would transiently 403 a
valid token).

<a id="resq_mcp.core.security.key_ring"></a>

#### key\_ring

Process-wide key ring seeded from configuration. Rotation at runtime is done
via ``key_ring.rotate(...)`` (e.g. from an operator endpoint or signal handler).

<a id="resq_mcp.core.security.require_mutation_allowed"></a>

#### require\_mutation\_allowed

```python
def require_mutation_allowed(action: str) -> None
```

Block side-effecting tools while Safe Mode is enabled.

Safe Mode (``RESQ_SAFE_MODE=true``) is the secure default. It lets agents plan
and reason over high-impact tools without triggering real-world consequences —
the confused-deputy mitigation in NSA PP-26-1834. Disable it deliberately
(``RESQ_SAFE_MODE=false``) only when autonomous execution is intended.

**Arguments**:

- `action` - The mutating tool name, used in the error message.
  

**Raises**:

- `FastMCPError` - If Safe Mode is enabled.

<a id="resq_mcp.core.security.verify_api_key"></a>

#### verify\_api\_key

```python
def verify_api_key(request: Request) -> str
```

Verify the Bearer token against the active key ring.

Delegates to ``key_ring.verify``, which accepts the active token and, during a
rotation grace window, the previous token — both compared in constant time.

Used as a dependency for SSE endpoints if wrapping in FastAPI.
For FastMCP's SSE adapter, authentication may need to be handled
at the deployment level (Ingress/Gateway) for strict OAuth.

**Arguments**:

- `request` - The incoming FastAPI request.
  

**Returns**:

  The validated API token.
  

**Raises**:

- `HTTPException` - 401 if missing/invalid auth scheme, 403 if invalid key.
