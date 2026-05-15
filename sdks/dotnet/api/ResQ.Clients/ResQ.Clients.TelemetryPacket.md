---
sidebarTitle: 'TelemetryPacket'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients')

## TelemetryPacket Class

A single telemetry packet from a drone\.

```csharp
public record TelemetryPacket : System.IEquatable<ResQ.Clients.TelemetryPacket>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → TelemetryPacket

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[TelemetryPacket](./ResQ.Clients.TelemetryPacket.md 'ResQ\.Clients\.TelemetryPacket')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

| Constructors | |
| :--- | :--- |
| [TelemetryPacket\(string, double, double, double, double, string, long\)](./ResQ.Clients.TelemetryPacket.TelemetryPacket(string,double,double,double,double,string,long).md 'ResQ\.Clients\.TelemetryPacket\.TelemetryPacket\(string, double, double, double, double, string, long\)') | A single telemetry packet from a drone\. |

| Properties | |
| :--- | :--- |
| [Altitude](./ResQ.Clients.TelemetryPacket.Altitude.md 'ResQ\.Clients\.TelemetryPacket\.Altitude') | Altitude in meters above sea level\. |
| [Battery](./ResQ.Clients.TelemetryPacket.Battery.md 'ResQ\.Clients\.TelemetryPacket\.Battery') | Battery percentage \(0\-100\)\. |
| [DroneId](./ResQ.Clients.TelemetryPacket.DroneId.md 'ResQ\.Clients\.TelemetryPacket\.DroneId') | Unique identifier of the drone \(required by HCE per\-packet schema\)\. |
| [FlightMode](./ResQ.Clients.TelemetryPacket.FlightMode.md 'ResQ\.Clients\.TelemetryPacket\.FlightMode') | Current flight mode \(e\.g\., "IDLE", "ARMED", "AUTO"\)\. |
| [Latitude](./ResQ.Clients.TelemetryPacket.Latitude.md 'ResQ\.Clients\.TelemetryPacket\.Latitude') | Latitude in decimal degrees\. |
| [Longitude](./ResQ.Clients.TelemetryPacket.Longitude.md 'ResQ\.Clients\.TelemetryPacket\.Longitude') | Longitude in decimal degrees\. |
| [Timestamp](./ResQ.Clients.TelemetryPacket.Timestamp.md 'ResQ\.Clients\.TelemetryPacket\.Timestamp') | Unix timestamp in seconds\. |
