---
sidebarTitle: 'DistanceTo(Location)'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[Location](./ResQ.Core.Location.md 'ResQ\.Core\.Location')

## Location\.DistanceTo\(Location\) Method

Calculates the great\-circle distance to another location using the Haversine formula\.

```csharp
public double DistanceTo(ResQ.Core.Location other);
```
#### Parameters

<a name='ResQ.Core.Location.DistanceTo(ResQ.Core.Location).other'></a>

`other` [Location](./ResQ.Core.Location.md 'ResQ\.Core\.Location')

The target location to calculate distance to\.

#### Returns
[System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')  
The distance in kilometers between this location and the target\.

### Example

```csharp
var point1 = new Location(37.7749, -122.4194); // San Francisco
var point2 = new Location(34.0522, -118.2437); // Los Angeles

double distance = point1.DistanceTo(point2);
Console.WriteLine($"Distance: {distance:F2} km"); // Distance: 559.12 km
```

### Remarks
This method uses the Haversine formula to calculate the shortest distance over
the earth's surface, giving an "as\-the\-crow\-flies" distance between the points
\(ignoring any hills, valleys, or other obstacles\)\. The calculation assumes
a spherical earth with a radius of 6,371 kilometers\.
