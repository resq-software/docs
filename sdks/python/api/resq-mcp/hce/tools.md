<a id="resq_mcp.hce.tools"></a>

# resq\_mcp.hce.tools

MCP tool wrappers for HCE domain.

<a id="resq_mcp.hce.tools.logging"></a>

## logging

<a id="resq_mcp.hce.tools.time"></a>

## time

<a id="resq_mcp.hce.tools.UTC"></a>

## UTC

<a id="resq_mcp.hce.tools.datetime"></a>

## datetime

<a id="resq_mcp.hce.tools.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.hce.tools.audit_log"></a>

## audit\_log

<a id="resq_mcp.hce.tools.preflight"></a>

## preflight

<a id="resq_mcp.hce.tools.IncidentValidation"></a>

## IncidentValidation

<a id="resq_mcp.hce.tools.MissionParameters"></a>

## MissionParameters

<a id="resq_mcp.hce.tools.MAX_INCIDENTS"></a>

## MAX\_INCIDENTS

<a id="resq_mcp.hce.tools.MAX_MISSIONS"></a>

## MAX\_MISSIONS

<a id="resq_mcp.hce.tools.incidents"></a>

## incidents

<a id="resq_mcp.hce.tools.mcp"></a>

## mcp

<a id="resq_mcp.hce.tools.missions"></a>

## missions

<a id="resq_mcp.hce.tools.logger"></a>

#### logger

<a id="resq_mcp.hce.tools.validate_incident"></a>

#### validate\_incident

```python
@mcp.tool()
async def validate_incident(val: IncidentValidation) -> str
```

Submit validation result for an incident report.

Used by human operators or automated validation systems (HCE) to
confirm or reject incident reports before triggering full response.

**Arguments**:

- `val` - IncidentValidation with:
  - incident_id: ID of incident being validated
  - is_confirmed: True=confirmed, False=rejected/false positive
  - validation_source: Who/what validated (e.g., "Human-Operator")
  - correlated_pre_alert_id: Optional linked PDIE alert
  - notes: Validation reasoning and evidence
  

**Returns**:

- `str` - Confirmation message indicating action taken:
  "Incident &#123;id&#125; successfully CONFIRMED." or
  "Incident &#123;id&#125; successfully REJECTED."
  

**Example**:

  >>> from resq_mcp.hce.models import IncidentValidation
  >>> validation = IncidentValidation(
  ...     incident_id="INC-123",
  ...     is_confirmed=True,
  ...     validation_source="Human-Operator-Alice",
  ...     notes="Confirmed via video evidence and ground reports"
  ... )
  >>> result = await validate_incident(validation)
  >>> print(result)  # "Incident INC-123 successfully CONFIRMED."
  
  Workflow:
  1. Edge AI detects incident (low confidence)
  2. HCE cross-references with PDIE/sensors
  3. If ambiguous -> human review required
  4. Operator submits validation via this tool
  5. If confirmed -> trigger response strategy
  6. If rejected -> log as false positive, update ML model
  
  Audit Trail:
  All validations logged with timestamp, source, and reasoning
  for post-incident analysis and ML model refinement.

<a id="resq_mcp.hce.tools.update_mission_params"></a>

#### update\_mission\_params

```python
@mcp.tool()
async def update_mission_params(drone_id: str,
                                strategy_id: str,
                                is_urgent: bool = False) -> MissionParameters
```

Push authorized mission parameters to a drone for an approved strategy.

Completes the deployment workflow after a strategy has been approved:
get_deployment_strategy -> (human approval) -> update_mission_params -> drone executes.

**Arguments**:

- `drone_id` - Target drone identifier (e.g., "DRONE-Alpha").
- `strategy_id` - Approved strategy ID from get_deployment_strategy (e.g., "STRAT-X1Y2Z3").
- `is_urgent` - If True, sets risk_tolerance=0.9 (aggressive routing) instead of the
  default 0.5. Must be explicitly set — urgency is never derived from the
  strategy_id string to prevent injection attacks.
  

**Returns**:

- `MissionParameters` - Authorized parameter set including mission ID, allowed actions,
  risk tolerance, and a deterministic blockchain-anchored strategy hash.
  

**Raises**:

- `FastMCPError` - If the drone already has an active mission for a different strategy
  (conflict guard), or if the mission store is at capacity.
  

**Example**:

  >>> params = await update_mission_params("DRONE-Alpha", "STRAT-ABCD1234", is_urgent=True)
  >>> print(params.authorized_actions)
  >>> print(params.strategy_hash)  # 0xSHA256(strategy_id:mission_id)
