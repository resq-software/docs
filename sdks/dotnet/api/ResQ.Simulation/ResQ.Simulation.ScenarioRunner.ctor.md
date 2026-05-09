### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation').[ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner')

## ScenarioRunner Constructors

| Overloads | |
| :--- | :--- |
| [ScenarioRunner\(CoordinationHceClient, InfrastructureApiClient\)](./ResQ.Simulation.ScenarioRunner.ctor.md#ResQ.Simulation.ScenarioRunner.ScenarioRunner(ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient) 'ResQ\.Simulation\.ScenarioRunner\.ScenarioRunner\(ResQ\.Clients\.CoordinationHceClient, ResQ\.Clients\.InfrastructureApiClient\)') | Initializes a new instance of the [ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner') class\. |
| [ScenarioRunner\(string, string\)](./ResQ.Simulation.ScenarioRunner.ctor.md#ResQ.Simulation.ScenarioRunner.ScenarioRunner(string,string) 'ResQ\.Simulation\.ScenarioRunner\.ScenarioRunner\(string, string\)') | Initializes a new instance of the [ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner') class using service URLs\. |

<a name='ResQ.Simulation.ScenarioRunner.ScenarioRunner(ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient)'></a>

## ScenarioRunner\(CoordinationHceClient, InfrastructureApiClient\) Constructor

Initializes a new instance of the [ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner') class\.

```csharp
public ScenarioRunner(ResQ.Clients.CoordinationHceClient hce, ResQ.Clients.InfrastructureApiClient infra);
```
#### Parameters

<a name='ResQ.Simulation.ScenarioRunner.ScenarioRunner(ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient).hce'></a>

`hce` [ResQ\.Clients\.CoordinationHceClient](https://learn.microsoft.com/en-us/dotnet/api/resq.clients.coordinationhceclient 'ResQ\.Clients\.CoordinationHceClient')

Client for the coordination\-hce service\.

<a name='ResQ.Simulation.ScenarioRunner.ScenarioRunner(ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient).infra'></a>

`infra` [ResQ\.Clients\.InfrastructureApiClient](https://learn.microsoft.com/en-us/dotnet/api/resq.clients.infrastructureapiclient 'ResQ\.Clients\.InfrastructureApiClient')

Client for the infrastructure\-api service\.

<a name='ResQ.Simulation.ScenarioRunner.ScenarioRunner(string,string)'></a>

## ScenarioRunner\(string, string\) Constructor

Initializes a new instance of the [ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner') class using service URLs\.

```csharp
public ScenarioRunner(string hceUrl="http://localhost:3000", string infraUrl="http://localhost:5000");
```
#### Parameters

<a name='ResQ.Simulation.ScenarioRunner.ScenarioRunner(string,string).hceUrl'></a>

`hceUrl` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Base URL of the coordination\-hce service\.

<a name='ResQ.Simulation.ScenarioRunner.ScenarioRunner(string,string).infraUrl'></a>

`infraUrl` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Base URL of the infrastructure\-api service\.
