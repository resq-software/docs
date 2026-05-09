<a id="resq_mcp.drone.models"></a>

# resq\_mcp.drone.models

Drone feed domain models for the ResQ MCP server.

<a id="resq_mcp.drone.models.annotations"></a>

## annotations

<a id="resq_mcp.drone.models.datetime"></a>

## datetime

<a id="resq_mcp.drone.models.Literal"></a>

## Literal

<a id="resq_mcp.drone.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.drone.models.Field"></a>

## Field

<a id="resq_mcp.drone.models.Coordinates"></a>

## Coordinates

<a id="resq_mcp.drone.models.SectorAnalysis"></a>

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

<a id="resq_mcp.drone.models.SectorAnalysis.sector_id"></a>

#### sector\_id

<a id="resq_mcp.drone.models.SectorAnalysis.timestamp"></a>

#### timestamp

<a id="resq_mcp.drone.models.SectorAnalysis.status"></a>

#### status

<a id="resq_mcp.drone.models.SectorAnalysis.detected_object"></a>

#### detected\_object

<a id="resq_mcp.drone.models.SectorAnalysis.disaster_type"></a>

#### disaster\_type

<a id="resq_mcp.drone.models.SectorAnalysis.confidence"></a>

#### confidence

<a id="resq_mcp.drone.models.SectorAnalysis.description"></a>

#### description

<a id="resq_mcp.drone.models.SectorAnalysis.coordinates"></a>

#### coordinates

<a id="resq_mcp.drone.models.SectorAnalysis.video_proof_url"></a>

#### video\_proof\_url

<a id="resq_mcp.drone.models.SectorAnalysis.recommended_action"></a>

#### recommended\_action

<a id="resq_mcp.drone.models.SectorStatusSummary"></a>

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

<a id="resq_mcp.drone.models.SectorStatusSummary.status"></a>

#### status

<a id="resq_mcp.drone.models.SectorStatusSummary.detected_object"></a>

#### detected\_object

<a id="resq_mcp.drone.models.SectorStatusSummary.confidence"></a>

#### confidence

<a id="resq_mcp.drone.models.NetworkStatus"></a>

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

<a id="resq_mcp.drone.models.NetworkStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.drone.models.NetworkStatus.total_sectors"></a>

#### total\_sectors

<a id="resq_mcp.drone.models.NetworkStatus.sectors"></a>

#### sectors

<a id="resq_mcp.drone.models.NetworkStatus.critical_alerts"></a>

#### critical\_alerts

<a id="resq_mcp.drone.models.SwarmStatus"></a>

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

<a id="resq_mcp.drone.models.SwarmStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.drone.models.SwarmStatus.total_drones"></a>

#### total\_drones

<a id="resq_mcp.drone.models.SwarmStatus.active_drones"></a>

#### active\_drones

<a id="resq_mcp.drone.models.SwarmStatus.average_battery"></a>

#### average\_battery

<a id="resq_mcp.drone.models.SwarmStatus.network_status"></a>

#### network\_status

<a id="resq_mcp.drone.models.SwarmStatus.last_sync"></a>

#### last\_sync

<a id="resq_mcp.drone.models.DeploymentRequest"></a>

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

<a id="resq_mcp.drone.models.DeploymentRequest.sector_id"></a>

#### sector\_id

<a id="resq_mcp.drone.models.DeploymentRequest.priority"></a>

#### priority

<a id="resq_mcp.drone.models.DeploymentStatus"></a>

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

<a id="resq_mcp.drone.models.DeploymentStatus.status"></a>

#### status

<a id="resq_mcp.drone.models.DeploymentStatus.sector_id"></a>

#### sector\_id

<a id="resq_mcp.drone.models.DeploymentStatus.priority"></a>

#### priority

<a id="resq_mcp.drone.models.DeploymentStatus.drone_id"></a>

#### drone\_id

<a id="resq_mcp.drone.models.DeploymentStatus.eta_seconds"></a>

#### eta\_seconds

<a id="resq_mcp.drone.models.DeploymentStatus.timestamp"></a>

#### timestamp
