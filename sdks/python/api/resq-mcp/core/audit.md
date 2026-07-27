<a id="resq_mcp.core.audit"></a>

# resq\_mcp.core.audit

Structured audit logging with hashed payloads for ResQ MCP tool invocations.

Implements the "Instrument for logging and detection" recommendation from NSA
PP-26-1834 (May 2026): all tool and model invocations should be logged with the
exact parameters, identities involved, and — where feasible — cryptographic
hashes of results or output, forming the backbone of forensic response.

Records are emitted as single-line JSON on the dedicated ``resq-mcp.audit`` logger
so they can be routed to a SIEM independently of operational logs. Raw parameter
and result payloads are *hashed* (SHA-256) rather than logged verbatim, which
limits raw-data retention and lets a record confirm whether a payload matches a
known reference. The digest is unsalted and deterministic, so it is **not** a
confidentiality control: low-entropy or guessable values (a short id, an enum, a
known URL) can still be recovered by brute force or by matching against candidates.
Do not treat hashing as licence to pass arbitrary secrets through
``parameters``/``result``.

Payload hashing is a content-integrity aid, not a tamper-evident log: on its own
it does not stop an attacker with log access from deleting, reordering, or forging
records, and it does not bind records into a verifiable chain. For tamper
resistance, route the ``resq-mcp.audit`` stream to immutable, access-controlled
storage — WORM or a retention-locked/immutable SIEM index; a generic SIEM sink is
not append-only by default.

<a id="resq_mcp.core.audit.annotations"></a>

## annotations

<a id="resq_mcp.core.audit.hashlib"></a>

## hashlib

<a id="resq_mcp.core.audit.json"></a>

## json

<a id="resq_mcp.core.audit.logging"></a>

## logging

<a id="resq_mcp.core.audit.Any"></a>

## Any

<a id="resq_mcp.core.audit.settings"></a>

## settings

<a id="resq_mcp.core.audit.audit_logger"></a>

#### audit\_logger

<a id="resq_mcp.core.audit.hash_payload"></a>

#### hash\_payload

```python
def hash_payload(payload: Any) -> str
```

Return a stable SHA-256 hex digest of a JSON-serialisable payload.

Keys are sorted so the digest is deterministic regardless of dict ordering,
sets are sorted, and any other non-serialisable value falls back to ``str``
so hashing never raises.

**Arguments**:

- `payload` - Any JSON-serialisable object (dict, list, scalar).
  

**Returns**:

  The 64-character hex SHA-256 digest of the canonical JSON encoding.

<a id="resq_mcp.core.audit.audit_log"></a>

#### audit\_log

```python
def audit_log(action: str,
              *,
              status: str,
              actor: str | None = None,
              parameters: Any | None = None,
              result: Any | None = None,
              **extra: Any) -> None
```

Emit a structured audit record for a tool invocation.

No-op when ``RESQ_AUDIT_ENABLED`` is false. Parameter and result payloads are
recorded only as SHA-256 digests; pass small, non-sensitive identifiers via
``**extra`` when they should appear in clear text for correlation.

**Arguments**:

- `action` - The tool or operation name (e.g. ``"run_simulation"``).
- `status` - Outcome marker (e.g. ``"accepted"``, ``"denied"``, ``"error"``).
- `actor` - Identity that triggered the call, when known.
- `parameters` - Input payload to hash into ``parameters_hash``.
- `result` - Output payload to hash into ``result_hash``.
- `**extra` - Additional fields merged into the record **verbatim, in clear
  text**. Unlike ``parameters``/``result``, these are not hashed, so
  pass only small non-sensitive correlation identifiers (e.g.
  ``incident_id="INC-123"``) — never PII, credentials, tokens, or
  evidence URLs. Keys that collide with reserved audit fields are
  dropped so extras cannot overwrite the canonical fields of that
  record — this guards a single record's shape, not the trail as a
  whole.
