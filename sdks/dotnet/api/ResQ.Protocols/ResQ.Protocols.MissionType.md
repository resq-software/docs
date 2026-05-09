### [ResQ\.Protocols](ResQ.Protocols.md 'ResQ\.Protocols')

## MissionType Enum

Defines mission types for drone operations\.

```csharp
public enum MissionType
```
### Fields

<a name='ResQ.Protocols.MissionType.Survey'></a>

`Survey` 0

Survey mission \- mapping and general area assessment\.

<a name='ResQ.Protocols.MissionType.Delivery'></a>

`Delivery` 1

Delivery mission \- transporting supplies or equipment\.

<a name='ResQ.Protocols.MissionType.Search'></a>

`Search` 2

Search mission \- looking for persons or objects\.

<a name='ResQ.Protocols.MissionType.Rescue'></a>

`Rescue` 3

Rescue mission \- active rescue operations\.

<a name='ResQ.Protocols.MissionType.Assessment'></a>

`Assessment` 4

Assessment mission \- damage and situation evaluation\.

<a name='ResQ.Protocols.MissionType.ReturnToBase'></a>

`ReturnToBase` 5

Return to base mission \- autonomous return to home\.

### Example

```csharp
// Assign mission type
var mission = new Mission
{
    Type = MissionType.Search,
    TargetArea = disasterZone,
    Priority = AlertSeverity.High
};

// Route based on mission type
switch (mission.Type)
{
    case MissionType.Survey:
        return CreateSurveyPattern(mission.TargetArea);
    case MissionType.Search:
        return CreateSearchPattern(mission.TargetArea);
    case MissionType.Rescue:
        return CreateRescueRoute(mission.TargetArea);
}
```

### Remarks
These mission types categorize the various operations that drones can perform
in the ResQ system\. Each mission type has specific objectives, flight patterns,
and sensor requirements\.
