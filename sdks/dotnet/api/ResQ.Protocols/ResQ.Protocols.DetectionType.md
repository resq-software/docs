---
sidebarTitle: 'DetectionType'
---

### [ResQ\.Protocols](./ResQ.Protocols.md 'ResQ\.Protocols')

## DetectionType Enum

Defines types of detections that can be identified by drone sensors and AI systems\.

```csharp
public enum DetectionType
```
### Fields

<a name='ResQ.Protocols.DetectionType.Unknown'></a>

`Unknown` 0

Unknown or unclassified detection\.

<a name='ResQ.Protocols.DetectionType.Person'></a>

`Person` 1

Human person detected\.

<a name='ResQ.Protocols.DetectionType.Vehicle'></a>

`Vehicle` 2

Vehicle \(car, truck, boat, etc\.\) detected\.

<a name='ResQ.Protocols.DetectionType.Fire'></a>

`Fire` 3

Fire or flames detected\.

<a name='ResQ.Protocols.DetectionType.Flood'></a>

`Flood` 4

Flood water or flooding detected\.

<a name='ResQ.Protocols.DetectionType.Debris'></a>

`Debris` 5

Debris or rubble detected\.

<a name='ResQ.Protocols.DetectionType.StructuralDamage'></a>

`StructuralDamage` 6

Structural damage to buildings or infrastructure\.

<a name='ResQ.Protocols.DetectionType.Survivor'></a>

`Survivor` 7

Survivor detected \(person in need of rescue\)\.

### Example

```csharp
// Check detection type
if (detection.Type == DetectionType.Person)
{
    await DispatchRescueTeam(detection.Location);
}
else if (detection.Type == DetectionType.Fire)
{
    await AlertFireDepartment(detection.Location);
}
```

### Remarks
These detection types represent the various objects, phenomena, and situations
that the ResQ AI detection system can identify from drone sensor data including
visual, thermal, and multi\-spectral imagery\.
