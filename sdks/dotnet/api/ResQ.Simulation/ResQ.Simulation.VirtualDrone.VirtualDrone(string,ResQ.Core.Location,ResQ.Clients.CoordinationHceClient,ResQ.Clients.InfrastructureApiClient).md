---
sidebarTitle: 'VirtualDrone(string, Location, CoordinationHceClient, InfrastructureApiClient)'
---

### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation').[VirtualDrone](./ResQ.Simulation.VirtualDrone.md 'ResQ\.Simulation\.VirtualDrone')

## VirtualDrone\(string, Location, CoordinationHceClient, InfrastructureApiClient\) Constructor

Initializes a new instance of the [VirtualDrone](./ResQ.Simulation.VirtualDrone.md 'ResQ\.Simulation\.VirtualDrone') class\.

```csharp
public VirtualDrone(string droneId, ResQ.Core.Location startLocation, ResQ.Clients.CoordinationHceClient hce, ResQ.Clients.InfrastructureApiClient infra);
```
#### Parameters

<a name='ResQ.Simulation.VirtualDrone.VirtualDrone(string,ResQ.Core.Location,ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient).droneId'></a>

`droneId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Unique identifier for this drone\.

<a name='ResQ.Simulation.VirtualDrone.VirtualDrone(string,ResQ.Core.Location,ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient).startLocation'></a>

`startLocation` [ResQ\.Core\.Location](https://learn.microsoft.com/en-us/dotnet/api/resq.core.location 'ResQ\.Core\.Location')

Initial geographic position of the drone\.

<a name='ResQ.Simulation.VirtualDrone.VirtualDrone(string,ResQ.Core.Location,ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient).hce'></a>

`hce` [ResQ\.Clients\.CoordinationHceClient](https://learn.microsoft.com/en-us/dotnet/api/resq.clients.coordinationhceclient 'ResQ\.Clients\.CoordinationHceClient')

Client for the coordination\-hce service\.

<a name='ResQ.Simulation.VirtualDrone.VirtualDrone(string,ResQ.Core.Location,ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient).infra'></a>

`infra` [ResQ\.Clients\.InfrastructureApiClient](https://learn.microsoft.com/en-us/dotnet/api/resq.clients.infrastructureapiclient 'ResQ\.Clients\.InfrastructureApiClient')

Client for the infrastructure\-api service\.

#### Exceptions

[System\.ArgumentException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentexception 'System\.ArgumentException')  
Thrown when droneId is empty\.

[System\.ArgumentOutOfRangeException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentoutofrangeexception 'System\.ArgumentOutOfRangeException')  
Thrown when coordinates or altitude are invalid\.
