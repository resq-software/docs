<a id="resq_mcp.tools"></a>

# resq\_mcp.tools

Drone feed tools for the ResQ MCP server.

This module provides simulated drone feed functionality for development and testing.
It generates pseudo-random telemetry and analysis data for drone network sectors.

The simulation includes:
- 4 monitored sectors with predefined coordinates
- Random disaster scenario detection (fire, flood, medical, debris)
- Swarm status with variable battery and connectivity
- Drone deployment request handling

<a id="resq_mcp.tools.annotations"></a>

## annotations

<a id="resq_mcp.tools.random"></a>

## random

<a id="resq_mcp.tools.UTC"></a>

## UTC

<a id="resq_mcp.tools.datetime"></a>

## datetime

<a id="resq_mcp.tools.Final"></a>

## Final

<a id="resq_mcp.tools.Coordinates"></a>

## Coordinates

<a id="resq_mcp.tools.DeploymentStatus"></a>

## DeploymentStatus

<a id="resq_mcp.tools.DisasterScenario"></a>

## DisasterScenario

<a id="resq_mcp.tools.ErrorResponse"></a>

## ErrorResponse

<a id="resq_mcp.tools.NetworkStatus"></a>

## NetworkStatus

<a id="resq_mcp.tools.SectorAnalysis"></a>

## SectorAnalysis

<a id="resq_mcp.tools.SectorStatusSummary"></a>

## SectorStatusSummary

<a id="resq_mcp.tools.SwarmStatus"></a>

## SwarmStatus

<a id="resq_mcp.tools.DRONE_SECTORS"></a>

#### DRONE\_SECTORS

<a id="resq_mcp.tools.DISASTER_SCENARIOS"></a>

#### DISASTER\_SCENARIOS

<a id="resq_mcp.tools.scan_current_sector"></a>

#### scan\_current\_sector

```python
def scan_current_sector(
        sector_id: str = "Sector-1") -> SectorAnalysis | ErrorResponse
```

Scan a specific sector for anomalies using simulated drone sensors.

Simulates drone-based surveillance with probabilistic disaster detection.
In production, this would integrate with actual drone telemetry and
edge AI processing results from the MCP drone feed server.

Detection Logic:
- 30% probability of detecting a disaster scenario per scan
- Randomly selects from predefined disaster templates
- Generates NeoFS evidence URL for blockchain submission
- Returns "clear" status if no anomalies detected

**Arguments**:

- `sector_id` - The sector to scan ("Sector-1" through "Sector-4").
  Default is "Sector-1".
  

**Returns**:

- `SectorAnalysis` - Complete scan results with detection data and
  recommended actions if sector exists.
- `ErrorResponse` - Error message if sector_id is invalid.
  

**Example**:

  >>> result = scan_current_sector("Sector-2")
  >>> if isinstance(result, SectorAnalysis):
  ...     if result.status == "CRITICAL_ALERT":
  ...         print(f"Alert: &#123;result.detected_object&#125;")
  ...         print(f"Action: &#123;result.recommended_action&#125;")
  

**Notes**:

  This is a simulation function. Production deployment would replace
  random detection with actual ML model inference on drone imagery.

<a id="resq_mcp.tools.get_all_sectors_status"></a>

#### get\_all\_sectors\_status

```python
def get_all_sectors_status() -> NetworkStatus
```

Get the status of all monitored sectors in the surveillance network.

Aggregates scan results across all configured sectors to provide
network-wide situational awareness for operator dashboards.

**Returns**:

- `NetworkStatus` - Complete network status including:
  - Total sector count
  - Per-sector status summaries (detected objects, confidence)
  - Critical alert count for priority filtering
  - Timestamp of status generation
  

**Example**:

  >>> status = get_all_sectors_status()
  >>> print(f"Network: &#123;status.total_sectors&#125; sectors")
  >>> print(f"Critical Alerts: &#123;status.critical_alerts&#125;")
  >>> for sector_id, summary in status.sectors.items():
  ...     if summary.status == "CRITICAL_ALERT":
  ...         print(f"&#123;sector_id&#125;: &#123;summary.detected_object&#125;")
  

**Notes**:

  Calls scan_current_sector() for each sector, so inherits its
  simulation behavior (random detection).

<a id="resq_mcp.tools.get_drone_swarm_status"></a>

#### get\_drone\_swarm\_status

```python
def get_drone_swarm_status() -> SwarmStatus
```

Get the overall operational status of the drone swarm.

Provides fleet-wide health metrics for monitoring drone readiness
and availability. Used by operators to assess deployment capacity.

Simulation Behavior:
- Total drones: Fixed at 3 for development
- Active drones: Random 2-3 (some may be charging/maintenance)
- Average battery: Random 60-100% (simulated degradation)
- Network status: Always "operational" in dev mode

**Returns**:

- `SwarmStatus` - Fleet metrics including:
  - Total and active drone counts
  - Fleet-wide average battery percentage
  - Network connectivity status
  - Last sync timestamp (auto-generated)
  

**Example**:

  >>> swarm = get_drone_swarm_status()
  >>> if swarm.average_battery &lt; 30:
  ...     print("WARNING: Low fleet battery")
  >>> print(f"&#123;swarm.active_drones&#125;/&#123;swarm.total_drones&#125; drones active")
  

**Notes**:

  Production would aggregate real telemetry from the MCP drone feed
  server, reporting actual battery, GPS lock, and link quality.

<a id="resq_mcp.tools.request_drone_deployment"></a>

#### request\_drone\_deployment

```python
def request_drone_deployment(
        sector_id: str,
        priority: str = "high") -> DeploymentStatus | ErrorResponse
```

Request deployment of a drone to a specific sector.

Simulates drone dispatch request handling with immediate assignment.
In production, this would interface with the drone control module
and mission planning system to allocate resources.

Simulation Behavior:
- Assigns random drone unit (UNIT-001 through UNIT-003)
- Generates random ETA (30-120 seconds)
- Always returns "deployed" status if sector valid

**Arguments**:

- `sector_id` - The target sector for deployment (e.g., "Sector-1").
- `priority` - Deployment urgency level. Higher priority missions
  preempt lower priority tasks. Valid values:
  - "low": Routine surveillance
  - "medium": Follow-up investigation
  - "high" (default): Active incident response
  - "critical": Immediate life-threatening situation
  

**Returns**:

- `DeploymentStatus` - Confirmation with assigned drone and ETA if
  sector is valid.
- `ErrorResponse` - Error message if sector_id is invalid.
  

**Example**:

  >>> status = request_drone_deployment("Sector-3", priority="critical")
  >>> if isinstance(status, DeploymentStatus):
  ...     print(f"Drone &#123;status.drone_id&#125; dispatched")
  ...     print(f"ETA: &#123;status.eta_seconds&#125; seconds")
  

**Notes**:

  Production would check drone availability, battery levels, and
  weather conditions before confirming deployment.
