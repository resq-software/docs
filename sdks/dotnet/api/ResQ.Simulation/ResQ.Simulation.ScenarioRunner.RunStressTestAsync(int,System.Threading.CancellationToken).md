### [ResQ\.Simulation](ResQ.Simulation.md 'ResQ\.Simulation').[ScenarioRunner](ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner')

## ScenarioRunner\.RunStressTestAsync\(int, CancellationToken\) Method

Scenario 3: Stress test with many drones \(3 minutes\)\.
Tests system limits and concurrent load handling\.

```csharp
public System.Threading.Tasks.Task RunStressTestAsync(int droneCount=100, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Simulation.ScenarioRunner.RunStressTestAsync(int,System.Threading.CancellationToken).droneCount'></a>

`droneCount` [System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')

Number of drones to simulate \(1\-10,000\)

<a name='ResQ.Simulation.ScenarioRunner.RunStressTestAsync(int,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task 'System\.Threading\.Tasks\.Task')
