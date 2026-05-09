---
sidebarTitle: 'ValidateLocation(Location, string)'
---

### [ResQ\.Simulation](./ResQ.Simulation.md 'ResQ\.Simulation').[ScenarioRunner](./ResQ.Simulation.ScenarioRunner.md 'ResQ\.Simulation\.ScenarioRunner')

## ScenarioRunner\.ValidateLocation\(Location, string\) Method

Validates location coordinates are within valid GPS bounds\.

```csharp
private static void ValidateLocation(ResQ.Core.Location location, string paramName);
```
#### Parameters

<a name='ResQ.Simulation.ScenarioRunner.ValidateLocation(ResQ.Core.Location,string).location'></a>

`location` [ResQ\.Core\.Location](https://learn.microsoft.com/en-us/dotnet/api/resq.core.location 'ResQ\.Core\.Location')

The location to validate\.

<a name='ResQ.Simulation.ScenarioRunner.ValidateLocation(ResQ.Core.Location,string).paramName'></a>

`paramName` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Name of the parameter for error messages\.

#### Exceptions

[System\.ArgumentNullException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentnullexception 'System\.ArgumentNullException')  
Thrown when location is null\.

[System\.ArgumentOutOfRangeException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentoutofrangeexception 'System\.ArgumentOutOfRangeException')  
Thrown when coordinates are outside valid ranges\.
