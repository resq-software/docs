---
sidebarTitle: 'ValidateDroneCount(int, string)'
---

### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation').[ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner')

## ScenarioRunner\.ValidateDroneCount\(int, string\) Method

Validates drone count parameter is within safe bounds\.

```csharp
private static void ValidateDroneCount(int droneCount, string paramName);
```
#### Parameters

<a name='ResQ.Simulation.ScenarioRunner.ValidateDroneCount(int,string).droneCount'></a>

`droneCount` [System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')

The number of drones to validate\.

<a name='ResQ.Simulation.ScenarioRunner.ValidateDroneCount(int,string).paramName'></a>

`paramName` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Name of the parameter for error messages\.

#### Exceptions

[System\.ArgumentOutOfRangeException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentoutofrangeexception 'System\.ArgumentOutOfRangeException')  
Thrown when drone count is outside valid range\.
