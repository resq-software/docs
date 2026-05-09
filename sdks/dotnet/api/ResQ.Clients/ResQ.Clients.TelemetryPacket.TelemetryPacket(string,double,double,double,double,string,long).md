### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[TelemetryPacket](./ResQ.Clients.TelemetryPacket.md 'ResQ\.Clients\.TelemetryPacket')

## TelemetryPacket\(string, double, double, double, double, string, long\) Constructor

A single telemetry packet from a drone\.

```csharp
public TelemetryPacket(string DroneId, double Latitude, double Longitude, double Altitude, double Battery, string FlightMode, long Timestamp);
```
#### Parameters

<a name='ResQ.Clients.TelemetryPacket.TelemetryPacket(string,double,double,double,double,string,long).DroneId'></a>

`DroneId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Unique identifier of the drone \(required by HCE per\-packet schema\)\.

<a name='ResQ.Clients.TelemetryPacket.TelemetryPacket(string,double,double,double,double,string,long).Latitude'></a>

`Latitude` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Latitude in decimal degrees\.

<a name='ResQ.Clients.TelemetryPacket.TelemetryPacket(string,double,double,double,double,string,long).Longitude'></a>

`Longitude` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Longitude in decimal degrees\.

<a name='ResQ.Clients.TelemetryPacket.TelemetryPacket(string,double,double,double,double,string,long).Altitude'></a>

`Altitude` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Altitude in meters above sea level\.

<a name='ResQ.Clients.TelemetryPacket.TelemetryPacket(string,double,double,double,double,string,long).Battery'></a>

`Battery` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Battery percentage \(0\-100\)\.

<a name='ResQ.Clients.TelemetryPacket.TelemetryPacket(string,double,double,double,double,string,long).FlightMode'></a>

`FlightMode` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Current flight mode \(e\.g\., "IDLE", "ARMED", "AUTO"\)\.

<a name='ResQ.Clients.TelemetryPacket.TelemetryPacket(string,double,double,double,double,string,long).Timestamp'></a>

`Timestamp` [System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')

Unix timestamp in seconds\.
