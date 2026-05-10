## NoFlyZone

```cpp
#include <nfz.hpp>
```

No-Fly Zone polygon definition.

Represents a restricted airspace area as a polygon. Altitude bounds define the vertical extent of the restriction.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `std::string` | [`id`](#id)  | Unique identifier for the NFZ. |
| `NFZType` | [`type`](#type)  | Type of no-fly zone. |
| `std::vector< GeoPoint >` | [`vertices`](#vertices)  | Polygon vertices (lat, lon pairs) |
| `double` | [`min_altitude_m`](#min_altitude_m)  | Minimum altitude affected (meters MSL) |
| `double` | [`max_altitude_m`](#max_altitude_m)  | Maximum altitude affected (meters MSL) |

---

#### id

```cpp
std::string id
```

Unique identifier for the NFZ.

---

#### type

```cpp
NFZType type
```

Type of no-fly zone.

---

#### vertices

```cpp
std::vector< GeoPoint > vertices
```

Polygon vertices (lat, lon pairs)

---

#### min_altitude_m

```cpp
double min_altitude_m
```

Minimum altitude affected (meters MSL)

---

#### max_altitude_m

```cpp
double max_altitude_m
```

Maximum altitude affected (meters MSL)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`contains_point`](#contains_point) `const` `inline` | Check if a point is inside the NFZ polygon (horizontal) |
| `bool` | [`contains_altitude`](#contains_altitude) `const` `inline` | Check if an altitude is within the NFZ vertical bounds. |
| `bool` | [`contains`](#contains-3) `const` `inline` | Check if a point (including altitude) is in the NFZ. |

---

#### contains_point

`const` `inline`

```cpp
inline bool contains_point(const GeoPoint & point) const
```

Check if a point is inside the NFZ polygon (horizontal)

#### Parameters
* `point` The geographic point to check 

#### Returns
true if point is inside the polygon

---

#### contains_altitude

`const` `inline`

```cpp
inline bool contains_altitude(double altitude_m) const
```

Check if an altitude is within the NFZ vertical bounds.

#### Parameters
* `altitude_m` Altitude in meters 

#### Returns
true if altitude is within the NFZ vertical extent

---

#### contains

`const` `inline`

```cpp
inline bool contains(const GeoPoint & point) const
```

Check if a point (including altitude) is in the NFZ.

#### Parameters
* `point` The 3D geographic point 

#### Returns
true if point is within the NFZ

