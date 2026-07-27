<a id="resq_mcp.core.guards"></a>

# resq\_mcp.core.guards

Tool preflight guards for the ResQ MCP server.

A single ``preflight`` entry point composes the per-invocation security controls
recommended by NSA PP-26-1834 and normalises their failures into ``FastMCPError``
so tool wrappers stay terse and consistent:

1. **Rate limiting** — bound the per-tool call rate (DoS / fatigue mitigation).
2. **Safe Mode gate** — block mutating tools unless execution is explicitly enabled
   (confused-deputy mitigation).
3. **Identifier validation** — reject raw string arguments that fall outside the
   identifier allow-list (injection / traversal / parameter-forwarding mitigation).

Pydantic-modelled tool inputs are validated at the model boundary; ``preflight`` is
for the raw scalar arguments that arrive outside a model.

<a id="resq_mcp.core.guards.annotations"></a>

## annotations

<a id="resq_mcp.core.guards.Mapping"></a>

## Mapping

<a id="resq_mcp.core.guards.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.core.guards.RateLimitExceeded"></a>

## RateLimitExceeded

<a id="resq_mcp.core.guards.enforce_rate_limit"></a>

## enforce\_rate\_limit

<a id="resq_mcp.core.guards.require_mutation_allowed"></a>

## require\_mutation\_allowed

<a id="resq_mcp.core.guards.validate_identifier"></a>

## validate\_identifier

<a id="resq_mcp.core.guards.preflight"></a>

#### preflight

```python
def preflight(tool: str,
              *,
              mutating: bool = False,
              identifiers: Mapping[str, str] | None = None) -> None
```

Run the standard preflight security checks for a tool invocation.

**Arguments**:

- `tool` - The tool name (used as the rate-limit key and in error messages).
- `mutating` - If True, enforce the Safe Mode gate (the tool has side effects).
- `identifiers` - Optional mapping of ``field_name -> value`` raw string
  arguments to validate against the identifier allow-list.
  

**Raises**:

- `FastMCPError` - If the rate limit is exceeded, Safe Mode blocks a mutating
  tool, or an identifier fails validation. The underlying ``ValueError``
  / ``RateLimitExceeded`` is normalised so clients see one error type.
