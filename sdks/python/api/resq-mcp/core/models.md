<a id="resq_mcp.core.models"></a>

# resq\_mcp.core.models

Shared domain models for the ResQ MCP server.

These Pydantic models define the core data contracts shared across all subsystems.

<a id="resq_mcp.core.models.annotations"></a>

## annotations

<a id="resq_mcp.core.models.UTC"></a>

## UTC

<a id="resq_mcp.core.models.datetime"></a>

## datetime

<a id="resq_mcp.core.models.Literal"></a>

## Literal

<a id="resq_mcp.core.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.core.models.Coordinates"></a>

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

<a id="resq_mcp.core.models.Coordinates.lat"></a>

#### lat

<a id="resq_mcp.core.models.Coordinates.lng"></a>

#### lng

<a id="resq_mcp.core.models.Coordinates.status"></a>

#### status

<a id="resq_mcp.core.models.Sector"></a>

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

<a id="resq_mcp.core.models.Sector.id"></a>

#### id

<a id="resq_mcp.core.models.Sector.coordinates"></a>

#### coordinates

<a id="resq_mcp.core.models.DetectedObject"></a>

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

<a id="resq_mcp.core.models.DetectedObject.name"></a>

#### name

<a id="resq_mcp.core.models.DetectedObject.type"></a>

#### type

<a id="resq_mcp.core.models.DetectedObject.confidence"></a>

#### confidence

<a id="resq_mcp.core.models.DetectedObject.description"></a>

#### description

<a id="resq_mcp.core.models.DisasterScenario"></a>

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

<a id="resq_mcp.core.models.DisasterScenario.type"></a>

#### type

<a id="resq_mcp.core.models.DisasterScenario.name"></a>

#### name

<a id="resq_mcp.core.models.DisasterScenario.confidence"></a>

#### confidence

<a id="resq_mcp.core.models.DisasterScenario.description"></a>

#### description

<a id="resq_mcp.core.models.ErrorResponse"></a>

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

<a id="resq_mcp.core.models.ErrorResponse.status"></a>

#### status

<a id="resq_mcp.core.models.ErrorResponse.message"></a>

#### message
