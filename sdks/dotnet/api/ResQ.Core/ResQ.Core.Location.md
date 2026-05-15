---
sidebarTitle: 'Location'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## Location Class

Represents a geographic location with latitude, longitude, and optional altitude\.

```csharp
public record Location : System.IEquatable<ResQ.Core.Location>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → Location

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[Location](./ResQ.Core.Location.md 'ResQ\.Core\.Location')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var location = new Location(37.7749, -122.4194); // San Francisco
var locationWithAlt = new Location(37.7749, -122.4194, 100.5);

// Calculate distance between two locations
var sf = new Location(37.7749, -122.4194);
var la = new Location(34.0522, -118.2437);
double distanceKm = sf.DistanceTo(la); // ~559 km
```

### Remarks
This record provides a standard way to represent geographic coordinates throughout
the ResQ system\. It includes a method to calculate distance between locations
using the Haversine formula for great\-circle distance\.

| Constructors | |
| :--- | :--- |
| [Location\(double, double, Nullable&lt;double&gt;\)](./ResQ.Core.Location.Location(double,double,System.Nullable_double_).md 'ResQ\.Core\.Location\.Location\(double, double, System\.Nullable\<double\>\)') | Represents a geographic location with latitude, longitude, and optional altitude\. |

| Properties | |
| :--- | :--- |
| [Altitude](./ResQ.Core.Location.Altitude.md 'ResQ\.Core\.Location\.Altitude') | Altitude in meters above sea level \(optional\)\. |
| [Latitude](./ResQ.Core.Location.Latitude.md 'ResQ\.Core\.Location\.Latitude') | Latitude in decimal degrees \(\-90 to 90\)\. |
| [Longitude](./ResQ.Core.Location.Longitude.md 'ResQ\.Core\.Location\.Longitude') | Longitude in decimal degrees \(\-180 to 180\)\. |

| Methods | |
| :--- | :--- |
| [DistanceTo\(Location\)](./ResQ.Core.Location.DistanceTo(ResQ.Core.Location).md 'ResQ\.Core\.Location\.DistanceTo\(ResQ\.Core\.Location\)') | Calculates the great\-circle distance to another location using the Haversine formula\. |
