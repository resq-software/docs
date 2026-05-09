---
sidebarTitle: 'RunSwarmSurveyAsync(int, CancellationToken)'
---

### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation').[ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner')

## ScenarioRunner\.RunSwarmSurveyAsync\(int, CancellationToken\) Method

Scenario 2: Swarm of N drones coordinated search \(5 minutes\)\.
Tests coordination and concurrent telemetry\.

```csharp
public System.Threading.Tasks.Task RunSwarmSurveyAsync(int droneCount=10, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Simulation.ScenarioRunner.RunSwarmSurveyAsync(int,System.Threading.CancellationToken).droneCount'></a>

`droneCount` [System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')

Number of drones to simulate \(1\-10,000\)

<a name='ResQ.Simulation.ScenarioRunner.RunSwarmSurveyAsync(int,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task 'System\.Threading\.Tasks\.Task')
