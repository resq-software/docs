<a id="resq_mcp.server"></a>

# resq\_mcp.server

ResQ MCP Server - Model Context Protocol server for disaster response coordination.

This module provides the main FastMCP server implementation for ResQ, offering:
- Simulation management via resources and tools
- Drone fleet status and deployment
- Incident validation and response planning

The server uses a lifespan context manager to manage background tasks for
simulation processing and notification delivery.

<a id="resq_mcp.server.asyncio"></a>

## asyncio

<a id="resq_mcp.server.contextlib"></a>

## contextlib

<a id="resq_mcp.server.logging"></a>

## logging

<a id="resq_mcp.server.time"></a>

## time

<a id="resq_mcp.server.asynccontextmanager"></a>

## asynccontextmanager

<a id="resq_mcp.server.TYPE_CHECKING"></a>

## TYPE\_CHECKING

<a id="resq_mcp.server.Any"></a>

## Any

<a id="resq_mcp.server.FastMCP"></a>

## FastMCP

<a id="resq_mcp.server.settings"></a>

## settings

<a id="resq_mcp.server.validate_environment"></a>

## validate\_environment

<a id="resq_mcp.server.setup_telemetry"></a>

## setup\_telemetry

<a id="resq_mcp.server.logger"></a>

#### logger

<a id="resq_mcp.server.MAX_SIMULATIONS"></a>

#### MAX\_SIMULATIONS

<a id="resq_mcp.server.MAX_INCIDENTS"></a>

#### MAX\_INCIDENTS

<a id="resq_mcp.server.MAX_MISSIONS"></a>

#### MAX\_MISSIONS

active missions per session

<a id="resq_mcp.server.COMPLETED_TTL_SECONDS"></a>

#### COMPLETED\_TTL\_SECONDS

evict completed sims after 5 minutes

<a id="resq_mcp.server.FAILED_TTL_SECONDS"></a>

#### FAILED\_TTL\_SECONDS

evict failed sims sooner

<a id="resq_mcp.server.INCIDENT_TTL_SECONDS"></a>

#### INCIDENT\_TTL\_SECONDS

evict rejected incident records after 1 hour

<a id="resq_mcp.server.CONFIRMED_INCIDENT_TTL_SECONDS"></a>

#### CONFIRMED\_INCIDENT\_TTL\_SECONDS

confirmed incidents retained for 24h

<a id="resq_mcp.server.MISSION_TTL_SECONDS"></a>

#### MISSION\_TTL\_SECONDS

evict stale mission records after 2h

<a id="resq_mcp.server.simulations"></a>

#### simulations

<a id="resq_mcp.server.incidents"></a>

#### incidents

<a id="resq_mcp.server.missions"></a>

#### missions

keyed by drone_id

<a id="resq_mcp.server.lifespan"></a>

#### lifespan

```python
@asynccontextmanager
async def lifespan(server: FastMCP) -> "AsyncGenerator[None, None]"
```

Lifespan context manager for the MCP server with background tasks.

Manages the lifecycle of background processing tasks that run for the
duration of the server. Ensures clean startup and shutdown with proper
task cancellation and resource cleanup.

Background Tasks Started:
- simulation_processor: Mock simulation state machine that transitions
simulations from pending -> processing -> completed and sends SSE
notifications to subscribed clients.

Lifecycle:
1. Startup: Log initialization, create background tasks
2. Running: Yield control to FastMCP server
3. Shutdown: Cancel tasks, suppress CancelledError, log shutdown

**Arguments**:

- `server` - The FastMCP server instance for notification dispatch.
  

**Yields**:

- `None` - Control returns to FastMCP for request handling.
  

**Notes**:

  In production, background tasks would interface with actual
  simulation clusters, message queues (Redis/RabbitMQ), and
  maintain persistent connections to drone telemetry streams.

<a id="resq_mcp.server.mcp"></a>

#### mcp

<a id="resq_mcp.server.simulation_processor"></a>

#### simulation\_processor

```python
async def simulation_processor(server: FastMCP) -> None
```

Background processor for simulation state transitions and notifications.

Polls for pending simulations every 2 s and spawns an independent async
task per simulation so that no single job's delay blocks the others.

State Machine:
pending    -> processing (immediate, 50% progress, task spawned)
processing -> completed  (after 3 s inside _process_simulation)
processing -> failed     (on server shutdown mid-run)

Notifications:
SSE resource update notifications are sent on each state transition.

**Notes**:

  Production would replace this with a real job queue integration
  (Celery / RQ) and Unity/Unreal Engine status polling.

<a id="resq_mcp.server.tools"></a>

## tools

<a id="resq_mcp.server.tools"></a>

## tools

<a id="resq_mcp.server.prompts"></a>

## prompts

<a id="resq_mcp.server.resources"></a>

## resources

<a id="resq_mcp.server.main"></a>

#### main

```python
def main() -> None
```

Console script entry point for the ResQ MCP server.
