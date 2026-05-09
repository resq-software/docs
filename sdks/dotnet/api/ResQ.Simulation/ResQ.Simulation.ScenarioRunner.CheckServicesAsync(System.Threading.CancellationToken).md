### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation').[ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner')

## ScenarioRunner\.CheckServicesAsync\(CancellationToken\) Method

Checks if services are healthy before running scenarios\.

```csharp
public System.Threading.Tasks.Task<bool> CheckServicesAsync(System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Simulation.ScenarioRunner.CheckServicesAsync(System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
True if all services are healthy; false otherwise\.

### Remarks
Verifies connectivity to both coordination\-hce and infrastructure\-api services\.
Outputs health status to console\.
