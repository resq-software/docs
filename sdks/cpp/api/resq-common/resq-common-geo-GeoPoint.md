## GeoPoint

```cpp
#include <geo.hpp>
```

Geographic point with latitude, longitude, and altitude.

Represents a 3D position on Earth's surface using the WGS84 ellipsoid. Latitude and longitude are in degrees, altitude in meters above sea level.

latitude must be in range [-90, 90] 

longitude must be in range [-180, 180]

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `double` | [`latitude`](#latitude)  | Latitude in degrees (-90 to 90) |
| `double` | [`longitude`](#longitude)  | Longitude in degrees (-180 to 180) |
| `double` | [`altitude`](#altitude)  | Altitude in meters above sea level. |

---

#### latitude

```cpp
double latitude
```

Latitude in degrees (-90 to 90)

---

#### longitude

```cpp
double longitude
```

Longitude in degrees (-180 to 180)

---

#### altitude

```cpp
double altitude
```

Altitude in meters above sea level.

