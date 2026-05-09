<a id="resq_mcp.models"></a>

# resq\_mcp.models

Domain models for the ResQ MCP server.

These Pydantic models define the core data contracts for the three main subsystems:
- PDIE (Predictive Disaster Intelligence Engine)
- DTSOP (Digital Twin Simulation & Optimization Platform)
- HCE (Hybrid Coordination Engine)

All datetime fields use timezone-aware UTC timestamps for consistency across
distributed systems and audit logging.

<a id="resq_mcp.models.annotations"></a>

## annotations

<a id="resq_mcp.models.UTC"></a>

## UTC

<a id="resq_mcp.models.datetime"></a>

## datetime

<a id="resq_mcp.models.Literal"></a>

## Literal

<a id="resq_mcp.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.models.Field"></a>

## Field

<a id="resq_mcp.models.Coordinates"></a>

## Coordinates Objects

```python
class Coordinates(BaseModel)
```

Geographic coordinates with status indicator.

Represents a geographic point in decimal degrees (WGS84 datum)
with an associated status flag for monitoring.

**Attributes**:

- `lat` - Latitude in decimal degrees (-90 to +90).
- `lng` - Longitude in decimal degrees (-180 to +180).
- `status` - Current status indicator (e.g., "clear", "critical").
  

**Example**:

  >>> coords = Coordinates(lat=37.3417, lng=-121.9751, status="clear")
  >>> print(f"Position: &#123;coords.lat&#125;, &#123;coords.lng&#125;")

<a id="resq_mcp.models.Coordinates.lat"></a>

#### lat

<a id="resq_mcp.models.Coordinates.lng"></a>

#### lng

<a id="resq_mcp.models.Coordinates.status"></a>

#### status

<a id="resq_mcp.models.Sector"></a>

## Sector Objects

```python
class Sector(BaseModel)
```

A monitored geographic sector in the drone surveillance network.

Sectors are predefined geographic zones monitored by the drone fleet
for disaster detection and response coordination.

**Attributes**:

- `id` - Unique sector identifier (e.g., "Sector-1").
- `coordinates` - Center point coordinates with status.

<a id="resq_mcp.models.Sector.id"></a>

#### id

<a id="resq_mcp.models.Sector.coordinates"></a>

#### coordinates

<a id="resq_mcp.models.DetectedObject"></a>

## DetectedObject Objects

```python
class DetectedObject(BaseModel)
```

An object detected by drone sensors during surveillance.

Represents the output of edge AI object detection running on drone
hardware or ground processing stations.

**Attributes**:

- `name` - Human-readable name of detected object (default: "None").
- `type` - Classification type (e.g., "fire", "vehicle", "person").
- `confidence` - Detection confidence score (0.0 to 1.0).
- `description` - Detailed description of the detection.

<a id="resq_mcp.models.DetectedObject.name"></a>

#### name

<a id="resq_mcp.models.DetectedObject.type"></a>

#### type

<a id="resq_mcp.models.DetectedObject.confidence"></a>

#### confidence

<a id="resq_mcp.models.DetectedObject.description"></a>

#### description

<a id="resq_mcp.models.DisasterScenario"></a>

## DisasterScenario Objects

```python
class DisasterScenario(BaseModel)
```

A disaster scenario template for simulation and detection.

Defines the characteristics of a disaster type that can be detected
by drone surveillance or used as input for digital twin simulations.

**Attributes**:

- `type` - Disaster category (e.g., "wildfire", "flood", "earthquake").
- `name` - Human-readable scenario name.
- `confidence` - Detection confidence or scenario likelihood (0.0 to 1.0).
- `description` - Detailed scenario description including characteristics.

<a id="resq_mcp.models.DisasterScenario.type"></a>

#### type

<a id="resq_mcp.models.DisasterScenario.name"></a>

#### name

<a id="resq_mcp.models.DisasterScenario.confidence"></a>

#### confidence

<a id="resq_mcp.models.DisasterScenario.description"></a>

#### description

<a id="resq_mcp.models.SectorAnalysis"></a>

## SectorAnalysis Objects

```python
class SectorAnalysis(BaseModel)
```

Complete analysis result from a sector surveillance scan.

Contains all detection data, evidence links, and recommended actions
from a drone sector scan. Used for incident reporting and blockchain
evidence submission.

**Attributes**:

- `sector_id` - Identifier of the scanned sector.
- `timestamp` - UTC timestamp of the analysis (auto-generated).
- `status` - Overall status (e.g., "clear", "CRITICAL_ALERT").
- `detected_object` - Primary object or hazard detected.
- `disaster_type` - Classified disaster type if applicable.
- `confidence` - Detection confidence score (0.0 to 1.0).
- `description` - Detailed analysis description.
- `coordinates` - Geographic coordinates of the detection.
- `video_proof_url` - NeoFS/IPFS URL for video evidence.
- `recommended_action` - Suggested next action (e.g., "IMMEDIATE_REPORT_TO_BLOCKCHAIN").

<a id="resq_mcp.models.SectorAnalysis.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.SectorAnalysis.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.SectorAnalysis.status"></a>

#### status

<a id="resq_mcp.models.SectorAnalysis.detected_object"></a>

#### detected\_object

<a id="resq_mcp.models.SectorAnalysis.disaster_type"></a>

#### disaster\_type

<a id="resq_mcp.models.SectorAnalysis.confidence"></a>

#### confidence

<a id="resq_mcp.models.SectorAnalysis.description"></a>

#### description

<a id="resq_mcp.models.SectorAnalysis.coordinates"></a>

#### coordinates

<a id="resq_mcp.models.SectorAnalysis.video_proof_url"></a>

#### video\_proof\_url

<a id="resq_mcp.models.SectorAnalysis.recommended_action"></a>

#### recommended\_action

<a id="resq_mcp.models.SectorStatusSummary"></a>

## SectorStatusSummary Objects

```python
class SectorStatusSummary(BaseModel)
```

Condensed status summary for network-wide sector monitoring.

Lightweight representation used in network status dashboards and
overview displays. Excludes detailed evidence and coordinates.

**Attributes**:

- `status` - Current sector status indicator.
- `detected_object` - Primary detected object or "None".
- `confidence` - Overall confidence score for the status.

<a id="resq_mcp.models.SectorStatusSummary.status"></a>

#### status

<a id="resq_mcp.models.SectorStatusSummary.detected_object"></a>

#### detected\_object

<a id="resq_mcp.models.SectorStatusSummary.confidence"></a>

#### confidence

<a id="resq_mcp.models.NetworkStatus"></a>

## NetworkStatus Objects

```python
class NetworkStatus(BaseModel)
```

Aggregate status of the entire drone surveillance network.

Provides a network-wide view of all monitored sectors and critical
alert counts for operator dashboards and system health monitoring.

**Attributes**:

- `timestamp` - UTC timestamp of the status snapshot (auto-generated).
- `total_sectors` - Total number of monitored sectors.
- `sectors` - Mapping of sector IDs to their status summaries.
- `critical_alerts` - Count of sectors with critical alerts active.

<a id="resq_mcp.models.NetworkStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.NetworkStatus.total_sectors"></a>

#### total\_sectors

<a id="resq_mcp.models.NetworkStatus.sectors"></a>

#### sectors

<a id="resq_mcp.models.NetworkStatus.critical_alerts"></a>

#### critical\_alerts

<a id="resq_mcp.models.SwarmStatus"></a>

## SwarmStatus Objects

```python
class SwarmStatus(BaseModel)
```

Real-time operational status of the drone swarm.

Aggregates health metrics across all drones in the fleet including
battery levels, connectivity status, and deployment state.

**Attributes**:

- `timestamp` - UTC timestamp of the status snapshot (auto-generated).
- `total_drones` - Total number of drones in the fleet.
- `active_drones` - Number of drones currently deployed and operational.
- `average_battery` - Fleet-wide average battery percentage (0-100).
- `network_status` - Overall network health (e.g., "operational", "degraded").
- `last_sync` - UTC timestamp of last successful sync with ground station.

<a id="resq_mcp.models.SwarmStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.SwarmStatus.total_drones"></a>

#### total\_drones

<a id="resq_mcp.models.SwarmStatus.active_drones"></a>

#### active\_drones

<a id="resq_mcp.models.SwarmStatus.average_battery"></a>

#### average\_battery

<a id="resq_mcp.models.SwarmStatus.network_status"></a>

#### network\_status

<a id="resq_mcp.models.SwarmStatus.last_sync"></a>

#### last\_sync

<a id="resq_mcp.models.DeploymentRequest"></a>

## DeploymentRequest Objects

```python
class DeploymentRequest(BaseModel)
```

Request for immediate drone deployment to a specific sector.

Used by operators or automated systems to request drone dispatch
to sectors requiring surveillance or emergency response.

**Attributes**:

- `sector_id` - Target sector identifier for deployment.
- `priority` - Deployment urgency level (low/medium/high/critical).
  Higher priority requests preempt lower priority missions.

<a id="resq_mcp.models.DeploymentRequest.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.DeploymentRequest.priority"></a>

#### priority

<a id="resq_mcp.models.DeploymentStatus"></a>

## DeploymentStatus Objects

```python
class DeploymentStatus(BaseModel)
```

Response status for a drone deployment request.

Provides confirmation and tracking information for a deployment request
including assigned drone and estimated arrival time.

**Attributes**:

- `status` - Deployment state (e.g., "deployed", "en_route", "completed").
- `sector_id` - Target sector identifier.
- `priority` - Assigned priority level.
- `drone_id` - Identifier of the assigned drone unit.
- `eta_seconds` - Estimated time to arrival in seconds.
- `timestamp` - UTC timestamp of the status update (auto-generated).

<a id="resq_mcp.models.DeploymentStatus.status"></a>

#### status

<a id="resq_mcp.models.DeploymentStatus.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.DeploymentStatus.priority"></a>

#### priority

<a id="resq_mcp.models.DeploymentStatus.drone_id"></a>

#### drone\_id

<a id="resq_mcp.models.DeploymentStatus.eta_seconds"></a>

#### eta\_seconds

<a id="resq_mcp.models.DeploymentStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.VulnerabilityMap"></a>

## VulnerabilityMap Objects

```python
class VulnerabilityMap(BaseModel)
```

Static vulnerability assessment data for a geographic sector.

Part of PDIE (Predictive Disaster Intelligence Engine) system.
Contains precomputed risk factors, infrastructure data, and population
metrics used for predictive disaster modeling and resource allocation.

**Attributes**:

- `sector_id` - Sector identifier this map applies to.
- `population_density` - Human population density category.
- `critical_infrastructure` - List of critical facilities (e.g., "hospital", "power-substation").
- `flood_risk` - Flood vulnerability score (0.0 to 1.0).
- `fire_risk` - Fire vulnerability score (0.0 to 1.0).
- `last_updated` - UTC timestamp of last data update (auto-generated).
  

**Notes**:

  Risk scores are precomputed from historical data, terrain analysis,
  and infrastructure density. Updated periodically via GIS integration.

<a id="resq_mcp.models.VulnerabilityMap.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.VulnerabilityMap.population_density"></a>

#### population\_density

<a id="resq_mcp.models.VulnerabilityMap.critical_infrastructure"></a>

#### critical\_infrastructure

<a id="resq_mcp.models.VulnerabilityMap.flood_risk"></a>

#### flood\_risk

<a id="resq_mcp.models.VulnerabilityMap.fire_risk"></a>

#### fire\_risk

<a id="resq_mcp.models.VulnerabilityMap.last_updated"></a>

#### last\_updated

<a id="resq_mcp.models.PreAlert"></a>

## PreAlert Objects

```python
class PreAlert(BaseModel)
```

Probabilistic disaster forecast from LSTM/GNN predictive models.

Part of PDIE system. Generated by machine learning models that analyze
weather patterns, sensor data, and historical trends to predict potential
disasters before they occur. Enables proactive resource positioning.

**Attributes**:

- `alert_id` - Unique alert identifier (e.g., "PRE-A1B2C3D4").
- `sector_id` - Target sector for the prediction.
- `predicted_disaster_type` - Expected disaster type (e.g., "wildfire", "flood").
- `probability` - Forecast confidence (0.0 to 1.0).
- `forecast_horizon_hours` - Time until predicted event (hours from now).
- `vulnerability_context` - Associated sector vulnerability data.
- `generated_at` - UTC timestamp of forecast generation (auto-generated).
  

**Example**:

  >>> alert = PreAlert(
  ...     alert_id="PRE-123ABC",
  ...     sector_id="Sector-1",
  ...     predicted_disaster_type="wildfire",
  ...     probability=0.85,
  ...     forecast_horizon_hours=12,
  ...     vulnerability_context=vuln_map
  ... )

<a id="resq_mcp.models.PreAlert.alert_id"></a>

#### alert\_id

<a id="resq_mcp.models.PreAlert.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.PreAlert.predicted_disaster_type"></a>

#### predicted\_disaster\_type

<a id="resq_mcp.models.PreAlert.probability"></a>

#### probability

<a id="resq_mcp.models.PreAlert.forecast_horizon_hours"></a>

#### forecast\_horizon\_hours

<a id="resq_mcp.models.PreAlert.vulnerability_context"></a>

#### vulnerability\_context

<a id="resq_mcp.models.PreAlert.generated_at"></a>

#### generated\_at

<a id="resq_mcp.models.SimulationRequest"></a>

## SimulationRequest Objects

```python
class SimulationRequest(BaseModel)
```

Request for high-fidelity physics simulation in digital twin.

Part of DTSOP system. Triggers physics-based simulation in Unity/Unreal
Engine for accurate disaster propagation modeling and strategy validation.

**Attributes**:

- `scenario_id` - Unique scenario identifier for this simulation.
- `sector_id` - Geographic sector to simulate.
- `disaster_type` - Type of disaster to model (e.g., "flood", "wildfire").
- `parameters` - Simulation parameters (e.g., &#123;"wind_speed": 15.5, "water_level": 2.3&#125;).
- `priority` - Processing priority (standard queued, urgent fast-tracked).
  

**Notes**:

  Simulations run asynchronously. Monitor progress via the returned
  simulation ID and resource subscription (resq://simulations/&#123;id&#125;).

<a id="resq_mcp.models.SimulationRequest.scenario_id"></a>

#### scenario\_id

<a id="resq_mcp.models.SimulationRequest.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.SimulationRequest.disaster_type"></a>

#### disaster\_type

<a id="resq_mcp.models.SimulationRequest.parameters"></a>

#### parameters

e.g., wind_speed, water_level

<a id="resq_mcp.models.SimulationRequest.priority"></a>

#### priority

<a id="resq_mcp.models.OptimizationStrategy"></a>

## OptimizationStrategy Objects

```python
class OptimizationStrategy(BaseModel)
```

Reinforcement learning-optimized deployment and evacuation strategy.

Part of DTSOP system. Generated by RL agents trained on thousands of
simulated disaster scenarios to optimize resource allocation and
evacuation routing under various constraints.

**Attributes**:

- `strategy_id` - Unique strategy identifier (e.g., "STRAT-X1Y2Z3W4").
- `related_alert_id` - Pre-alert or incident ID this strategy addresses.
- `recommended_deployment` - Mapping of drone types to recommended counts
  (e.g., &#123;"surveillance": 2, "payload": 1&#125;).
- `evacuation_routes` - Ordered list of recommended evacuation routes.
- `estimated_success_rate` - Predicted success probability (0.0 to 1.0)
  based on simulation outcomes.
- `simulation_proof_url` - NeoFS/IPFS URL for simulation evidence and logs.
  

**Notes**:

  Success rate derived from Monte Carlo simulations across varying
  disaster intensities and communication scenarios.

<a id="resq_mcp.models.OptimizationStrategy.strategy_id"></a>

#### strategy\_id

<a id="resq_mcp.models.OptimizationStrategy.related_alert_id"></a>

#### related\_alert\_id

<a id="resq_mcp.models.OptimizationStrategy.recommended_deployment"></a>

#### recommended\_deployment

drone_type -> count

<a id="resq_mcp.models.OptimizationStrategy.evacuation_routes"></a>

#### evacuation\_routes

<a id="resq_mcp.models.OptimizationStrategy.estimated_success_rate"></a>

#### estimated\_success\_rate

<a id="resq_mcp.models.OptimizationStrategy.simulation_proof_url"></a>

#### simulation\_proof\_url

<a id="resq_mcp.models.IncidentReport"></a>

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

<a id="resq_mcp.models.IncidentReport.incident_id"></a>

#### incident\_id

<a id="resq_mcp.models.IncidentReport.source"></a>

#### source

<a id="resq_mcp.models.IncidentReport.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.IncidentReport.detected_type"></a>

#### detected\_type

<a id="resq_mcp.models.IncidentReport.confidence"></a>

#### confidence

<a id="resq_mcp.models.IncidentReport.evidence_url"></a>

#### evidence\_url

<a id="resq_mcp.models.IncidentReport.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.IncidentValidation"></a>

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

<a id="resq_mcp.models.IncidentValidation.incident_id"></a>

#### incident\_id

<a id="resq_mcp.models.IncidentValidation.is_confirmed"></a>

#### is\_confirmed

<a id="resq_mcp.models.IncidentValidation.validation_source"></a>

#### validation\_source

e.g., "SpoonOS-Validator"

<a id="resq_mcp.models.IncidentValidation.correlated_pre_alert_id"></a>

#### correlated\_pre\_alert\_id

<a id="resq_mcp.models.IncidentValidation.notes"></a>

#### notes

<a id="resq_mcp.models.MissionParameters"></a>

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

<a id="resq_mcp.models.MissionParameters.mission_id"></a>

#### mission\_id

<a id="resq_mcp.models.MissionParameters.target_sector"></a>

#### target\_sector

<a id="resq_mcp.models.MissionParameters.authorized_actions"></a>

#### authorized\_actions

<a id="resq_mcp.models.MissionParameters.risk_tolerance"></a>

#### risk\_tolerance

<a id="resq_mcp.models.MissionParameters.strategy_hash"></a>

#### strategy\_hash

blockchain link

<a id="resq_mcp.models.MissionParameters.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.ErrorResponse"></a>

## ErrorResponse Objects

```python
class ErrorResponse(BaseModel)
```

Standard error response for failed operations.

Used across all subsystems to provide consistent error messaging.
Returned instead of raising exceptions for expected error conditions
(e.g., invalid sector ID, missing data).

**Attributes**:

- `status` - Always "error" to distinguish from success responses.
- `message` - Human-readable error description.
  

**Example**:

  >>> error = ErrorResponse(message="Sector not found")
  >>> if isinstance(result, ErrorResponse):
  ...     print(f"Error: &#123;result.message&#125;")

<a id="resq_mcp.models.ErrorResponse.status"></a>

#### status

<a id="resq_mcp.models.ErrorResponse.message"></a>

#### message
