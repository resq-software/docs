### [ResQ\.Core](ResQ.Core.md 'ResQ\.Core').[Location](ResQ.Core.Location.md 'ResQ\.Core\.Location')

## Location\(double, double, Nullable\<double\>\) Constructor

Represents a geographic location with latitude, longitude, and optional altitude\.

```csharp
public Location(double Latitude, double Longitude, System.Nullable<double> Altitude=null);
```
#### Parameters

<a name='ResQ.Core.Location.Location(double,double,System.Nullable_double_).Latitude'></a>

`Latitude` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Latitude in decimal degrees \(\-90 to 90\)\.

<a name='ResQ.Core.Location.Location(double,double,System.Nullable_double_).Longitude'></a>

`Longitude` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Longitude in decimal degrees \(\-180 to 180\)\.

<a name='ResQ.Core.Location.Location(double,double,System.Nullable_double_).Altitude'></a>

`Altitude` [System\.Nullable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1 'System\.Nullable\`1')[System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1 'System\.Nullable\`1')

Altitude in meters above sea level \(optional\)\.

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
