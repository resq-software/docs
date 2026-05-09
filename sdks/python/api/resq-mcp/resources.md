<a id="resq_mcp.resources"></a>

# resq\_mcp.resources

MCP resource endpoints for the ResQ server.

<a id="resq_mcp.resources.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.resources.mcp"></a>

## mcp

<a id="resq_mcp.resources.simulations"></a>

## simulations

<a id="resq_mcp.resources.get_simulation_status"></a>

#### get\_simulation\_status

```python
@mcp.resource("resq://simulations/{sim_id}")
async def get_simulation_status(sim_id: str) -> str
```

Get the current status of a physics simulation job.

Resource endpoint that provides real-time simulation progress and results.
Supports SSE subscriptions for push notifications on state changes.

URI Pattern:
resq://simulations/&#123;sim_id&#125;

Subscription Behavior:
Clients can subscribe to this resource to receive automatic updates
when simulation state transitions (pending -> processing -> completed).
Server sends resource_updated notifications via SSE.

**Arguments**:

- `sim_id` - Unique simulation job identifier (e.g., "SIM-A1B2C3D4").
  

**Returns**:

- `str` - Formatted string with simulation details:
  - Simulation ID
  - Current status (pending/processing/completed)
  - Progress percentage (0-100%)
  - Result URL (NeoFS CID) when completed
  - Original request parameters
  

**Raises**:

- `FastMCPError` - If sim_id not found in simulation registry.
  

**Example**:

  Client workflow:
  1. Call run_simulation tool -> get sim_id
  2. Subscribe to resq://simulations/&#123;sim_id&#125;
  3. Receive updates as simulation progresses
  4. Fetch result_url when status=completed
  
  Response Format:
  Simulation ID: SIM-A1B2C3D4
- `Status` - processing
- `Progress` - 50%
- `Result` - N/A (or neofs://sim_results/SIM-xxx.json)
- `Parameters` - &#123;scenario_id: ..., sector_id: ..., ...&#125;

<a id="resq_mcp.resources.list_active_drones"></a>

#### list\_active\_drones

```python
@mcp.resource("resq://drones/active")
def list_active_drones() -> str
```

List currently deployed drones in the active fleet.

Resource endpoint providing real-time fleet status for operator awareness.
Shows current deployment locations, battery levels, and operational modes.

URI Pattern:
resq://drones/active

**Returns**:

- `str` - Formatted string with active drone details:
  - Drone identifier
  - Drone type/capability (Surveillance/Payload/Relay)
  - Operational status (ACTIVE/RETURNING/CHARGING)
  - Battery percentage
  - Current sector assignment
  
  Example Response:
  [Active Fleet Status]
  - DRONE-Alpha (Surveillance): ACTIVE | Battery 78% | Sector 4
  - DRONE-Beta (Payload): RETURNING | Battery 12% | Sector 2
  - DRONE-Gamma (Relay): ACTIVE | Battery 92% | Sector 4
  
  Use Cases:
  - Operator dashboard fleet overview
  - Resource availability checking before deployment
  - Low battery alert monitoring
  - Sector coverage assessment
  

**Notes**:

  Current implementation returns static mock data. Production would
  query live telemetry from MCP drone feed server and aggregate
  real-time positions, battery, and mission status.
