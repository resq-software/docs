### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## DisasterType Enum

Defines types of disasters and emergencies the ResQ system can respond to\.

```csharp
public enum DisasterType
```
### Fields

<a name='ResQ.Core.DisasterType.None'></a>

`None` 0

No disaster or not classified\.

<a name='ResQ.Core.DisasterType.Flood'></a>

`Flood` 1

Flooding or flash flood event\.

<a name='ResQ.Core.DisasterType.Wildfire'></a>

`Wildfire` 2

Wildfire or forest fire\.

<a name='ResQ.Core.DisasterType.Earthquake'></a>

`Earthquake` 3

Earthquake or seismic event\.

<a name='ResQ.Core.DisasterType.Hurricane'></a>

`Hurricane` 4

Hurricane, typhoon, or tropical cyclone\.

<a name='ResQ.Core.DisasterType.Tsunami'></a>

`Tsunami` 5

Tsunami or tidal wave\.

<a name='ResQ.Core.DisasterType.StructuralCollapse'></a>

`StructuralCollapse` 6

Structural collapse of buildings or infrastructure\.

<a name='ResQ.Core.DisasterType.ChemicalSpill'></a>

`ChemicalSpill` 7

Chemical spill or hazardous material release\.

### Example

```csharp
switch (incident.DisasterType)
{
    case DisasterType.Wildfire:
        await DeployFireSuppressionDrones(incident.Location);
        break;
    case DisasterType.Flood:
        await DeploySearchAndRescueDrones(incident.Location);
        break;
}
```

### Remarks
These disaster types are used to categorize incidents, trigger appropriate
response protocols, and route alerts to specialized response teams\.
