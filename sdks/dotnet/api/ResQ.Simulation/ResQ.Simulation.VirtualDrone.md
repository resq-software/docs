---
sidebarTitle: 'VirtualDrone'
---

### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation')

## VirtualDrone Class

Simulates a virtual drone that sends telemetry to HCE and reports detections\.

```csharp
public class VirtualDrone
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → VirtualDrone

| Constructors | |
| :--- | :--- |
| [VirtualDrone\(string, Location, CoordinationHceClient, InfrastructureApiClient\)](./ResQ.Simulation.VirtualDrone.VirtualDrone(string,ResQ.Core.Location,ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient).md 'ResQ\.Simulation\.VirtualDrone\.VirtualDrone\(string, ResQ\.Core\.Location, ResQ\.Clients\.CoordinationHceClient, ResQ\.Clients\.InfrastructureApiClient\)') | Initializes a new instance of the [VirtualDrone](./ResQ.Simulation.VirtualDrone.md 'ResQ\.Simulation\.VirtualDrone') class\. |

| Methods | |
| :--- | :--- |
| [StartAsync\(CancellationToken\)](./ResQ.Simulation.VirtualDrone.StartAsync(System.Threading.CancellationToken).md 'ResQ\.Simulation\.VirtualDrone\.StartAsync\(System\.Threading\.CancellationToken\)') | Starts the drone's telemetry loop \(sends data every 1 second\)\. |
| [Stop\(\)](./ResQ.Simulation.VirtualDrone.Stop().md 'ResQ\.Simulation\.VirtualDrone\.Stop\(\)') | Stops the drone's telemetry loop\. |
