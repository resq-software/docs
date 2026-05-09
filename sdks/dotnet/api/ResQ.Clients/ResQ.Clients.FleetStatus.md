---
sidebarTitle: 'FleetStatus'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients')

## FleetStatus Class

Status response for a fleet of drones\.

```csharp
public record FleetStatus : System.IEquatable<ResQ.Clients.FleetStatus>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; FleetStatus

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[FleetStatus](./ResQ.Clients.FleetStatus.md 'ResQ\.Clients\.FleetStatus')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

| Constructors | |
| :--- | :--- |
| [FleetStatus\(string, int, int\)](./ResQ.Clients.FleetStatus.FleetStatus(string,int,int).md 'ResQ\.Clients\.FleetStatus\.FleetStatus\(string, int, int\)') | Status response for a fleet of drones\. |

| Properties | |
| :--- | :--- |
| [ActiveDrones](./ResQ.Clients.FleetStatus.ActiveDrones.md 'ResQ\.Clients\.FleetStatus\.ActiveDrones') | Number of currently active drones in the fleet\. |
| [FleetId](./ResQ.Clients.FleetStatus.FleetId.md 'ResQ\.Clients\.FleetStatus\.FleetId') | Unique identifier for the fleet\. |
| [TotalMissions](./ResQ.Clients.FleetStatus.TotalMissions.md 'ResQ\.Clients\.FleetStatus\.TotalMissions') | Total number of missions completed by the fleet\. |
