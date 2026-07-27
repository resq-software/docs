<a id="resq_mcp.core.validation"></a>

# resq\_mcp.core.validation

Input bounding and identifier validation for ResQ MCP tools.

Implements the "Validate parameters" recommendation from NSA Cybersecurity
Information sheet *Model Context Protocol (MCP): Security Design Considerations*
(PP-26-1834, May 2026): every tool invocation should validate its inputs against
well-defined schemas, expected ranges, character allow-lists, and size bounds to
guard against malformed inputs, prompt-injection, and denial-of-service attempts.

These helpers are deliberately framework-agnostic and raise plain ``ValueError`` so
they compose with both Pydantic ``field_validator`` hooks (which convert
``ValueError`` into a clean ``ValidationError``) and direct calls from tool wrappers.

<a id="resq_mcp.core.validation.annotations"></a>

## annotations

<a id="resq_mcp.core.validation.re"></a>

## re

<a id="resq_mcp.core.validation.MAX_IDENTIFIER_LENGTH"></a>

#### MAX\_IDENTIFIER\_LENGTH

Maximum length for identifier-shaped fields (IDs, sector names, types).

<a id="resq_mcp.core.validation.MAX_TEXT_LENGTH"></a>

#### MAX\_TEXT\_LENGTH

Maximum length for free-text fields (notes, descriptions).

<a id="resq_mcp.core.validation.MAX_SOURCE_LENGTH"></a>

#### MAX\_SOURCE\_LENGTH

Maximum length for actor/source labels (e.g. ``validation_source``).

<a id="resq_mcp.core.validation.MAX_PARAMETERS"></a>

#### MAX\_PARAMETERS

Maximum number of entries allowed in a tool ``parameters`` mapping.

<a id="resq_mcp.core.validation.MAX_PARAM_KEY_LENGTH"></a>

#### MAX\_PARAM\_KEY\_LENGTH

Maximum length of a single ``parameters`` key.

<a id="resq_mcp.core.validation.MAX_PARAM_VALUE_LENGTH"></a>

#### MAX\_PARAM\_VALUE\_LENGTH

Maximum length of a single string ``parameters`` value.

<a id="resq_mcp.core.validation.validate_identifier"></a>

#### validate\_identifier

```python
def validate_identifier(value: str, *, field: str = "identifier") -> str
```

Validate that ``value`` is a safe, bounded identifier.

**Arguments**:

- `value` - The candidate identifier (e.g. ``"INC-123"``, ``"DRONE-Alpha"``).
- `field` - Human-readable field name used in error messages.
  

**Returns**:

  The validated value, unchanged (so it is usable inline).
  

**Raises**:

- `ValueError` - If the value is empty, too long, or contains characters
  outside the allow-list ``[A-Za-z0-9._:-]`` (must start alphanumeric).
  

**Example**:

  >>> validate_identifier("INC-123", field="incident_id")
  'INC-123'

<a id="resq_mcp.core.validation.validate_parameters"></a>

#### validate\_parameters

```python
def validate_parameters(
        params: dict[str, float | str]) -> dict[str, float | str]
```

Validate a tool ``parameters`` mapping for size and per-value bounds.

Caps the number of entries, the length of each key, and the length of each
string value. Numeric values are accepted as-is (range checks belong to the
domain layer), but unbounded strings — a vector for memory-exhaustion and
injection — are rejected.

**Arguments**:

- `params` - The parameters mapping to validate.
  

**Returns**:

  The validated mapping, unchanged.
  

**Raises**:

- `ValueError` - If the mapping exceeds ``MAX_PARAMETERS`` entries, a key
  exceeds ``MAX_PARAM_KEY_LENGTH``, or a string value exceeds
  ``MAX_PARAM_VALUE_LENGTH``.
