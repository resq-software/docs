---
sidebarTitle: 'GetFleetStatusAsync(string, CancellationToken)'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[CoordinationHceClient](./ResQ.Clients.CoordinationHceClient.md 'ResQ\.Clients\.CoordinationHceClient')

## CoordinationHceClient\.GetFleetStatusAsync\(string, CancellationToken\) Method

Gets the status of a fleet\.
Includes retry logic for transient read failures\.

```csharp
public System.Threading.Tasks.Task<ResQ.Clients.FleetStatus> GetFleetStatusAsync(string fleetId, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.CoordinationHceClient.GetFleetStatusAsync(string,System.Threading.CancellationToken).fleetId'></a>

`fleetId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

<a name='ResQ.Clients.CoordinationHceClient.GetFleetStatusAsync(string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[FleetStatus](./ResQ.Clients.FleetStatus.md 'ResQ\.Clients\.FleetStatus')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
