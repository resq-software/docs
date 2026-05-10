<a id="resq_mcp"></a>

# resq\_mcp

ResQ MCP - Model Context Protocol server for disaster response coordination.

This package provides:
- PDIE (Predictive Disaster Intelligence Engine)
- DTSOP (Digital Twin Simulation & Optimization Platform)
- HCE (Hybrid Coordination Engine)

**Example**:

  from resq_mcp import mcp
  mcp.run()

## API

- `annotations`
- [Settings](./core/config#settings-objects)
- [settings](./core/config#settings)
- [Coordinates](./models#coordinates-objects)
- [DetectedObject](./models#detectedobject-objects)
- [DisasterScenario](./models#disasterscenario-objects)
- [ErrorResponse](./models#errorresponse-objects)
- [Sector](./models#sector-objects)
- [DeploymentRequest](./models#deploymentrequest-objects)
- [DeploymentStatus](./models#deploymentstatus-objects)
- [NetworkStatus](./models#networkstatus-objects)
- [SectorAnalysis](./models#sectoranalysis-objects)
- [SectorStatusSummary](./models#sectorstatussummary-objects)
- [SwarmStatus](./models#swarmstatus-objects)
- [get_all_sectors_status](./tools#get_all_sectors_status)
- [get_drone_swarm_status](./tools#get_drone_swarm_status)
- [request_drone_deployment](./tools#request_drone_deployment)
- [scan_current_sector](./tools#scan_current_sector)
- [OptimizationStrategy](./models#optimizationstrategy-objects)
- [SimulationRequest](./models#simulationrequest-objects)
- [get_optimization_strategy](./dtsop/service#get_optimization_strategy)
- [run_simulation](./dtsop/tools#run_simulation)
- [IncidentReport](./models#incidentreport-objects)
- [IncidentValidation](./models#incidentvalidation-objects)
- [MissionParameters](./models#missionparameters-objects)
- [update_mission_params](./hce/tools#update_mission_params)
- [validate_incident](./hce/tools#validate_incident)
- [PreAlert](./models#prealert-objects)
- [VulnerabilityMap](./models#vulnerabilitymap-objects)
- [get_predictive_alerts](./pdie/service#get_predictive_alerts)
- [get_vulnerability_map](./pdie/service#get_vulnerability_map)
- [mcp](./server#mcp)
