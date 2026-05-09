### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation').[ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner')

## ScenarioRunner\.RunIncidentFloodAsync\(int\) Method

Scenario 4: Incident flood \- all drones detect same incident \(30 seconds\)\.
Tests spike handling when many drones report simultaneously\.

```csharp
public System.Threading.Tasks.Task RunIncidentFloodAsync(int droneCount=20);
```
#### Parameters

<a name='ResQ.Simulation.ScenarioRunner.RunIncidentFloodAsync(int).droneCount'></a>

`droneCount` [System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')

Number of drones to simulate \(1\-10,000\)

#### Returns
[System\.Threading\.Tasks\.Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task 'System\.Threading\.Tasks\.Task')
