<a id="resq_mcp.dtsop.tools"></a>

# resq\_mcp.dtsop.tools

MCP tool wrappers for DTSOP domain.

<a id="resq_mcp.dtsop.tools.logging"></a>

## logging

<a id="resq_mcp.dtsop.tools.UTC"></a>

## UTC

<a id="resq_mcp.dtsop.tools.datetime"></a>

## datetime

<a id="resq_mcp.dtsop.tools.Context"></a>

## Context

<a id="resq_mcp.dtsop.tools.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.dtsop.tools.OptimizationStrategy"></a>

## OptimizationStrategy

<a id="resq_mcp.dtsop.tools.SimulationRequest"></a>

## SimulationRequest

<a id="resq_mcp.dtsop.tools.get_optimization_strategy"></a>

## get\_optimization\_strategy

<a id="resq_mcp.dtsop.tools.trigger_sim"></a>

## trigger\_sim

<a id="resq_mcp.dtsop.tools.MAX_SIMULATIONS"></a>

## MAX\_SIMULATIONS

<a id="resq_mcp.dtsop.tools.incidents"></a>

## incidents

<a id="resq_mcp.dtsop.tools.mcp"></a>

## mcp

<a id="resq_mcp.dtsop.tools.simulations"></a>

## simulations

<a id="resq_mcp.dtsop.tools.logger"></a>

#### logger

<a id="resq_mcp.dtsop.tools.run_simulation"></a>

#### run\_simulation

```python
@mcp.tool()
async def run_simulation(request: SimulationRequest,
                         ctx: Context | None = None) -> str
```

Trigger a Digital Twin physics simulation for disaster scenario modeling.

Queues a high-fidelity simulation job and returns immediately with a
job ID. Clients should subscribe to the simulation resource URI for
real-time progress updates and result notification.

Workflow:
1. Validate simulation request parameters
2. Generate unique simulation ID
3. Queue job to DTSOP backend (Unity/Unreal Engine)
4. Store job metadata in simulation registry
5. Return simulation ID and subscription URI
6. Background processor updates status -> processing -> completed
7. Client fetches results from NeoFS when completed

**Arguments**:

- `request` - SimulationRequest with:
  - scenario_id: Unique scenario identifier
  - sector_id: Geographic sector to simulate
  - disaster_type: Physics model (flood/wildfire/earthquake)
  - parameters: Scenario params (wind_speed, water_level, etc.)
  - priority: "standard" or "urgent"
- `ctx` - Optional FastMCP context for logging.
  

**Returns**:

- `str` - Message with simulation ID and subscription instructions:
  "Simulation queued with ID: SIM-XXXXXXXX.
  Subscribe to resq://simulations/SIM-XXXXXXXX for updates."
  

**Example**:

  >>> from resq_mcp.dtsop.models import SimulationRequest
  >>> request = SimulationRequest(
  ...     scenario_id="flood-001",
  ...     sector_id="Sector-1",
  ...     disaster_type="flood",
  ...     parameters=&#123;"water_level": 2.5&#125;,
  ...     priority="urgent"
  ... )
  >>> result = await run_simulation(request)
  >>> print(result)  # "Simulation queued with ID: SIM-ABCD1234..."
  
  Integration:
  Production would:
  - Validate request against simulation templates
  - Check cluster capacity and queue position
  - Store job in Redis with priority
  - Submit to Unity/Unreal Engine processing cluster
  - Return estimated completion time

<a id="resq_mcp.dtsop.tools.get_deployment_strategy"></a>

#### get\_deployment\_strategy

```python
@mcp.tool()
async def get_deployment_strategy(incident_id: str) -> OptimizationStrategy
```

Generate an RL-optimized drone deployment and evacuation strategy.

Uses reinforcement learning models trained on thousands of simulated
disasters to recommend optimal resource allocation, routing, and
risk parameters for a specific incident or pre-alert.

**Arguments**:

- `incident_id` - Incident identifier (INC-XXX) or pre-alert ID (PRE-XXX)
  to generate strategy for.
  

**Returns**:

- `OptimizationStrategy` - Complete strategy recommendation with:
  - strategy_id: Unique identifier
  - related_alert_id: Original incident/alert ID
  - recommended_deployment: Drone type counts
  - evacuation_routes: Prioritized route list
  - estimated_success_rate: Predicted success (0.0-1.0)
  - simulation_proof_url: NeoFS evidence link
  

**Example**:

  >>> strategy = await get_deployment_strategy("PRE-ABC123")
  >>> print(strategy.strategy_id)
  >>> print(strategy.recommended_deployment)  # &#123;"surveillance": 2, ...&#125;
  >>> print(f"Success rate: &#123;strategy.estimated_success_rate:.0%&#125;")
  
  Use Cases:
  - Pre-positioning drones before predicted disasters (PDIE alerts)
  - Active response optimization for confirmed incidents
  - Multi-objective optimization (speed, safety, resource efficiency)
  - Scenario comparison and sensitivity analysis
  
  Integration:
  Strategy linked to blockchain for immutable audit trail.
  After approval, use update_mission_params to push to drones.
