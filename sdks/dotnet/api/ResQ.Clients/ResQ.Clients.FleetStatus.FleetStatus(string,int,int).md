---
sidebarTitle: 'FleetStatus(string, int, int)'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[FleetStatus](./ResQ.Clients.FleetStatus.md 'ResQ\.Clients\.FleetStatus')

## FleetStatus\(string, int, int\) Constructor

Status response for a fleet of drones\.

```csharp
public FleetStatus(string FleetId, int ActiveDrones, int TotalMissions);
```
#### Parameters

<a name='ResQ.Clients.FleetStatus.FleetStatus(string,int,int).FleetId'></a>

`FleetId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Unique identifier for the fleet\.

<a name='ResQ.Clients.FleetStatus.FleetStatus(string,int,int).ActiveDrones'></a>

`ActiveDrones` [System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')

Number of currently active drones in the fleet\.

<a name='ResQ.Clients.FleetStatus.FleetStatus(string,int,int).TotalMissions'></a>

`TotalMissions` [System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')

Total number of missions completed by the fleet\.
