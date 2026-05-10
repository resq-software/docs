# geo

### Classes

| Name | Description |
|------|-------------|
| [`GeoPoint`](resq-common-geo-GeoPoint.md#geopoint) | Geographic point with latitude, longitude, and altitude. |
| [`GeoSegment`](resq-common-geo-GeoSegment.md#geosegment) | Line segment in geographic coordinates. |
| [`NoFlyZone`](resq-common-geo-NoFlyZone.md#noflyzone) | No-Fly Zone polygon definition. |

### Enumerations

| Name | Description |
|------|-------------|
| [`NFZType`](#nfztype)  | Type of no-fly zone. |

---

#### NFZType

```cpp
enum NFZType
```

Type of no-fly zone.

| Value | Description |
|-------|-------------|
| `AIRPORT` | FAA restricted airspace around airports. |
| `TEMPORARY` | Temporary flight restrictions (TFR) |
| `MILITARY` | Military restricted zones. |
| `NATIONAL_PARK` | National park no-drone zones. |
| `PRISON` | Correctional facility airspace. |
| `HOSPITAL` | Hospital/helipad emergency zones. |
| `CUSTOM` | Custom user-defined zone. |

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `double` | [`haversine_distance_meters`](#haversine_distance_meters) `inline` | Calculate Haversine distance between two geographic points. |
| `bool` | [`is_point_in_polygon`](#is_point_in_polygon) `inline` | Check if a point is inside a polygon using ray casting. |
| `bool` | [`segment_intersects_polygon`](#segment_intersects_polygon) `inline` | Check if a line segment intersects a polygon (bounding box check) |
| `std::optional< std::reference_wrapper< const NoFlyZone > >` | [`path_intersects_nfz`](#path_intersects_nfz) `inline` | Check if a flight path (waypoint to waypoint) intersects any NFZ. |
| `std::optional< std::reference_wrapper< const NoFlyZone > >` | [`path_intersects_nfz`](#path_intersects_nfz-1) `inline` | Check if any point in a path intersects NFZ. |

---

#### haversine_distance_meters

`inline`

```cpp
inline double haversine_distance_meters(const GeoPoint & p1, const GeoPoint & p2)
```

Calculate Haversine distance between two geographic points.

Computes the great-circle distance between two points on Earth's surface using the Haversine formula. This provides accurate results for most navigation purposes, though for survey-grade precision consider Vincenty's formulae.

#### Parameters
* `p1` First geographic point 

* `p2` Second geographic point 

#### Returns
Distance in meters between the two points

Returns 0.0 if both points are identical 

Returns approximately 20,000,000 meters for antipodal points

:::note
Uses Earth radius of 6,371,000 meters (mean radius) 

:::

:::note
Accuracy degrades for very large distances due to Earth's ellipsoidal shape

:::

## Example:

```cpp
[GeoPoint](resq-common-geo-GeoPoint.md#geopoint) base{40.7128, -74.0060, 0.0};  // New York
GeoPoint target{34.0522, -118.2437, 0.0}; // Los Angeles
double distance = [haversine_distance_meters](#haversine_distance_meters)(base, target);
// distance ≈ 3,944,000 meters
```

---

#### is_point_in_polygon

`inline`

```cpp
inline bool is_point_in_polygon(const GeoPoint & point, const std::vector< GeoPoint > & vertices)
```

Check if a point is inside a polygon using ray casting.

Uses the even-odd rule (ray casting algorithm).

#### Parameters
* `point` The point to check 

* `vertices` Polygon vertices 

#### Returns
true if point is inside the polygon

---

#### segment_intersects_polygon

`inline`

```cpp
inline bool segment_intersects_polygon(const GeoSegment & segment, const std::vector< GeoPoint > & polygon)
```

Check if a line segment intersects a polygon (bounding box check)

This is a simplified check using bounding boxes. For more accurate results, consider great circle paths.

#### Parameters
* `segment` The line segment 

* `polygon` The polygon vertices 

#### Returns
true if segment might intersect polygon

---

#### path_intersects_nfz

`inline`

```cpp
inline std::optional< std::reference_wrapper< const NoFlyZone > > path_intersects_nfz(const GeoPoint & from, const GeoPoint & to, const std::vector< NoFlyZone > & nfz_list)
```

Check if a flight path (waypoint to waypoint) intersects any NFZ.

#### Parameters
* `from` Starting point 

* `to` Ending point 

* `nfz_list` List of no-fly zones to check against 

#### Returns
Pointer to the NFZ that the path intersects, or nullopt if clear

---

#### path_intersects_nfz

`inline`

```cpp
inline std::optional< std::reference_wrapper< const NoFlyZone > > path_intersects_nfz(const std::vector< GeoPoint > & waypoints, const std::vector< NoFlyZone > & nfz_list)
```

Check if any point in a path intersects NFZ.

#### Parameters
* `waypoints` List of waypoints defining the path 

* `nfz_list` List of no-fly zones 

#### Returns
Pointer to first intersecting NFZ, or nullopt if clear

### Variables

| Return | Name | Description |
|--------|------|-------------|
| `constexpr double` | [`kPi`](#kpi)  |  |

---

#### kPi

```cpp
constexpr double kPi = 3.14159265358979323846
```

