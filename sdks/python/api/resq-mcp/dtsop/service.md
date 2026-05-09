<a id="resq_mcp.dtsop.service"></a>

# resq\_mcp.dtsop.service

DTSOP - Digital Twin Simulation & Optimization Platform.

This module provides simulation and optimization capabilities:
- High-fidelity physics simulation triggering (Unity/Unreal Engine integration)
- RL-optimized drone deployment strategies
- Evacuation route generation

The current implementation is stubbed for development and returns simulated data.

<a id="resq_mcp.dtsop.service.annotations"></a>

## annotations

<a id="resq_mcp.dtsop.service.random"></a>

## random

<a id="resq_mcp.dtsop.service.uuid"></a>

## uuid

<a id="resq_mcp.dtsop.service.Final"></a>

## Final

<a id="resq_mcp.dtsop.service.OptimizationStrategy"></a>

## OptimizationStrategy

<a id="resq_mcp.dtsop.service.SimulationRequest"></a>

## SimulationRequest

<a id="resq_mcp.dtsop.service.run_simulation"></a>

#### run\_simulation

```python
def run_simulation(request: SimulationRequest) -> str
```

Trigger a high-fidelity physics simulation in the digital twin.

Part of DTSOP (Digital Twin Simulation & Optimization Platform) system.
Queues a physics simulation job for async processing by Unity/Unreal
Engine with PX4 SITL and Gazebo integration.

Simulation Capabilities:
- Disaster propagation physics (flood spread, fire dynamics)
- Drone swarm dynamics and collision avoidance
- Communication link degradation under disaster conditions
- Infrastructure failure cascades
- Population movement and evacuation modeling

**Arguments**:

- `request` - Simulation parameters including:
  - scenario_id: Unique identifier for this simulation run
  - sector_id: Geographic area to simulate
  - disaster_type: Physics model to apply (flood/wildfire/earthquake)
  - parameters: Scenario-specific params (wind speed, water level, etc.)
  - priority: "standard" (queued) or "urgent" (fast-tracked)
  

**Returns**:

- `str` - Unique simulation job ID (format: "SIM-XXXXXXXX" where X is hex).
  Use this ID to monitor progress via resq://simulations/&#123;id&#125; resource.
  

**Example**:

  >>> from resq_mcp.dtsop.models import SimulationRequest
  >>> req = SimulationRequest(
  ...     scenario_id="flood-scenario-001",
  ...     sector_id="Sector-1",
  ...     disaster_type="flood",
  ...     parameters=&#123;"water_level": 2.5, "flow_rate": 1.2&#125;,
  ...     priority="urgent"
  ... )
  >>> sim_id = run_simulation(req)
  >>> print(f"Simulation queued: &#123;sim_id&#125;")
  
  Integration Note:
  Production implementation would:
  1. Validate request against available simulation templates
  2. Queue job to Unity/Unreal Engine processing cluster
  3. Store simulation state in Redis for progress tracking
  4. Send SSE notifications on status changes
  5. Store results (JSON + video) to NeoFS with CID

<a id="resq_mcp.dtsop.service.get_optimization_strategy"></a>

#### get\_optimization\_strategy

```python
def get_optimization_strategy(
        incident_or_alert_id: str) -> OptimizationStrategy
```

Generate RL-optimized deployment and evacuation strategy.

Part of DTSOP system. Uses reinforcement learning agents trained on
thousands of simulated scenarios to recommend optimal resource allocation
and routing under constraints (battery, weather, infrastructure damage).

Strategy Components:
- Recommended drone deployment mix (surveillance, payload, relay types)
- Evacuation route prioritization based on congestion and safety
- Success probability from Monte Carlo simulation ensemble
- Blockchain-linked proof for audit trail

RL Agent Training:
- Reward function: Lives saved + Response time + Resource efficiency
- State space: Disaster extent, infrastructure status, drone positions
- Action space: Deployment counts, waypoint routing, risk thresholds
- Training: PPO algorithm on 100k+ simulated disaster scenarios

**Arguments**:

- `incident_or_alert_id` - The incident ID (INC-XXX) or pre-alert ID (PRE-XXX)
  to optimize strategy for.
  

**Returns**:

- `OptimizationStrategy` - Complete strategy including:
  - strategy_id: Unique identifier for this strategy
  - recommended_deployment: Drone type to count mapping
  - evacuation_routes: Ordered list of recommended routes
  - estimated_success_rate: Predicted success (0.0-1.0)
  - simulation_proof_url: NeoFS link to simulation evidence
  

**Example**:

  >>> strategy = get_optimization_strategy("PRE-ABC123")
  >>> print(f"Strategy: &#123;strategy.strategy_id&#125;")
  >>> print(f"Deployment: &#123;strategy.recommended_deployment&#125;")
  >>> print(f"Success rate: &#123;strategy.estimated_success_rate:.0%&#125;")
  >>> for route in strategy.evacuation_routes:
  ...     print(f"Route: &#123;route&#125;")
  

**Notes**:

  Current implementation randomly selects from predefined templates.
  Production would invoke actual RL agent inference with real-time data.
