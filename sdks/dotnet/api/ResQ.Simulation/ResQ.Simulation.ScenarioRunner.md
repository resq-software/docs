### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation')

## ScenarioRunner Class

Orchestrates simulation scenarios to stress\-test ResQ services\.

```csharp
public class ScenarioRunner
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; ScenarioRunner

| Constructors | |
| :--- | :--- |
| [ScenarioRunner\(CoordinationHceClient, InfrastructureApiClient\)](./ResQ.Simulation.ScenarioRunner.ctor.md#ResQ.Simulation.ScenarioRunner.ScenarioRunner(ResQ.Clients.CoordinationHceClient,ResQ.Clients.InfrastructureApiClient) 'ResQ\.Simulation\.ScenarioRunner\.ScenarioRunner\(ResQ\.Clients\.CoordinationHceClient, ResQ\.Clients\.InfrastructureApiClient\)') | Initializes a new instance of the [ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner') class\. |
| [ScenarioRunner\(string, string\)](./ResQ.Simulation.ScenarioRunner.ctor.md#ResQ.Simulation.ScenarioRunner.ScenarioRunner(string,string) 'ResQ\.Simulation\.ScenarioRunner\.ScenarioRunner\(string, string\)') | Initializes a new instance of the [ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner') class using service URLs\. |

| Methods | |
| :--- | :--- |
| [CheckServicesAsync\(CancellationToken\)](./ResQ.Simulation.ScenarioRunner.CheckServicesAsync(System.Threading.CancellationToken).md 'ResQ\.Simulation\.ScenarioRunner\.CheckServicesAsync\(System\.Threading\.CancellationToken\)') | Checks if services are healthy before running scenarios\. |
| [RunIncidentFloodAsync\(int\)](./ResQ.Simulation.ScenarioRunner.RunIncidentFloodAsync(int).md 'ResQ\.Simulation\.ScenarioRunner\.RunIncidentFloodAsync\(int\)') | Scenario 4: Incident flood \- all drones detect same incident \(30 seconds\)\. Tests spike handling when many drones report simultaneously\. |
| [RunSingleDroneSurveyAsync\(\)](./ResQ.Simulation.ScenarioRunner.RunSingleDroneSurveyAsync().md 'ResQ\.Simulation\.ScenarioRunner\.RunSingleDroneSurveyAsync\(\)') | Scenario 1: Single drone survey mission \(2 minutes\)\. Tests basic telemetry, detection, and blockchain recording\. |
| [RunStressTestAsync\(int, CancellationToken\)](./ResQ.Simulation.ScenarioRunner.RunStressTestAsync(int,System.Threading.CancellationToken).md 'ResQ\.Simulation\.ScenarioRunner\.RunStressTestAsync\(int, System\.Threading\.CancellationToken\)') | Scenario 3: Stress test with many drones \(3 minutes\)\. Tests system limits and concurrent load handling\. |
| [RunSwarmSurveyAsync\(int, CancellationToken\)](./ResQ.Simulation.ScenarioRunner.RunSwarmSurveyAsync(int,System.Threading.CancellationToken).md 'ResQ\.Simulation\.ScenarioRunner\.RunSwarmSurveyAsync\(int, System\.Threading\.CancellationToken\)') | Scenario 2: Swarm of N drones coordinated search \(5 minutes\)\. Tests coordination and concurrent telemetry\. |
