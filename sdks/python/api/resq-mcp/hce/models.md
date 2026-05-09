<a id="resq_mcp.hce.models"></a>

# resq\_mcp.hce.models

HCE domain models for the ResQ MCP server.

<a id="resq_mcp.hce.models.annotations"></a>

## annotations

<a id="resq_mcp.hce.models.datetime"></a>

## datetime

<a id="resq_mcp.hce.models.Literal"></a>

## Literal

<a id="resq_mcp.hce.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.hce.models.Field"></a>

## Field

<a id="resq_mcp.hce.models.IncidentReport"></a>

## IncidentReport Objects

```python
class IncidentReport(BaseModel)
```

Initial incident report from Edge AI, human observers, or sensors.

Part of HCE (Hybrid Coordination Engine) system. Represents unvalidated
incident detection requiring cross-reference and validation before
triggering full response protocols.

**Attributes**:

- `incident_id` - Unique incident identifier.
- `source` - Detection source (edge_ai=onboard processing, human_report=operator,
  sensor_network=ground sensors).
- `sector_id` - Geographic sector of the incident.
- `detected_type` - Incident classification (e.g., "fire", "collision", "flooding").
- `confidence` - Detection confidence from source (0.0 to 1.0).
- `evidence_url` - Optional URL to evidence (video, photos) on IPFS/NeoFS.
- `timestamp` - UTC timestamp of detection (auto-generated).
  

**Notes**:

  High-confidence reports (>0.85) may auto-confirm. Lower confidence
  reports cross-referenced with PDIE predictions and other sources.

<a id="resq_mcp.hce.models.IncidentReport.incident_id"></a>

#### incident\_id

<a id="resq_mcp.hce.models.IncidentReport.source"></a>

#### source

<a id="resq_mcp.hce.models.IncidentReport.sector_id"></a>

#### sector\_id

<a id="resq_mcp.hce.models.IncidentReport.detected_type"></a>

#### detected\_type

<a id="resq_mcp.hce.models.IncidentReport.confidence"></a>

#### confidence

<a id="resq_mcp.hce.models.IncidentReport.evidence_url"></a>

#### evidence\_url

<a id="resq_mcp.hce.models.IncidentReport.timestamp"></a>

#### timestamp

<a id="resq_mcp.hce.models.IncidentValidation"></a>

## IncidentValidation Objects

```python
class IncidentValidation(BaseModel)
```

Validation result after cross-referencing an incident report.

Part of HCE system. Produced after comparing incident reports against
PDIE predictions, sensor networks, and historical data to confirm
authenticity and trigger appropriate response protocols.

**Attributes**:

- `incident_id` - ID of the incident being validated.
- `is_confirmed` - Whether the incident is confirmed as genuine.
- `validation_source` - System or agent that performed validation
  (e.g., "SpoonOS-HCE-Validator", "Human-Operator").
- `correlated_pre_alert_id` - Related PDIE pre-alert if correlation found.
- `notes` - Detailed validation reasoning and cross-reference results.
  

**Example**:

  >>> validation = IncidentValidation(
  ...     incident_id="INC-123",
  ...     is_confirmed=True,
  ...     validation_source="SpoonOS-HCE-Validator",
  ...     notes="Confirmed via PDIE correlation and sensor data"
  ... )

<a id="resq_mcp.hce.models.IncidentValidation.incident_id"></a>

#### incident\_id

<a id="resq_mcp.hce.models.IncidentValidation.is_confirmed"></a>

#### is\_confirmed

<a id="resq_mcp.hce.models.IncidentValidation.validation_source"></a>

#### validation\_source

e.g., "SpoonOS-Validator"

<a id="resq_mcp.hce.models.IncidentValidation.correlated_pre_alert_id"></a>

#### correlated\_pre\_alert\_id

<a id="resq_mcp.hce.models.IncidentValidation.notes"></a>

#### notes

<a id="resq_mcp.hce.models.MissionParameters"></a>

## MissionParameters Objects

```python
class MissionParameters(BaseModel)
```

Authorized mission parameters pushed to drone via HCE.

Part of HCE system. Defines the authorized action space and risk
parameters for autonomous drone operations. Includes blockchain hash
for immutable audit trail of mission authorizations.

**Attributes**:

- `mission_id` - Unique mission identifier (e.g., "MISS-A1B2C3D4").
- `target_sector` - Assigned operational sector.
- `authorized_actions` - List of permitted autonomous actions
  (e.g., ["autonomous_flight", "payload_release_authorized"]).
- `risk_tolerance` - Maximum acceptable risk level (0.0 to 1.0).
  Lower values restrict aggressive maneuvers.
- `strategy_hash` - Blockchain transaction hash linking to strategy record
  for immutable audit trail (format: "0xHEXDIGITS").
- `timestamp` - UTC timestamp of parameter push (auto-generated).
  
  Security Note:
  Authorized actions are validated against drone firmware capabilities.
  Unauthorized actions are rejected by ResQ-OS security layer.

<a id="resq_mcp.hce.models.MissionParameters.mission_id"></a>

#### mission\_id

<a id="resq_mcp.hce.models.MissionParameters.target_sector"></a>

#### target\_sector

<a id="resq_mcp.hce.models.MissionParameters.authorized_actions"></a>

#### authorized\_actions

<a id="resq_mcp.hce.models.MissionParameters.risk_tolerance"></a>

#### risk\_tolerance

<a id="resq_mcp.hce.models.MissionParameters.strategy_hash"></a>

#### strategy\_hash

blockchain link

<a id="resq_mcp.hce.models.MissionParameters.timestamp"></a>

#### timestamp
