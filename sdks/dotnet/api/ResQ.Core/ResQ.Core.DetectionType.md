---
sidebarTitle: 'DetectionType'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## DetectionType Enum

Defines types of objects and phenomena detectable by AI systems\.

```csharp
public enum DetectionType
```
### Fields

<a name='ResQ.Core.DetectionType.None'></a>

`None` 0

No detection or unknown\.

<a name='ResQ.Core.DetectionType.Fire'></a>

`Fire` 1

Fire, flames, or smoke detected\.

<a name='ResQ.Core.DetectionType.Flood'></a>

`Flood` 2

Flood water detected\.

<a name='ResQ.Core.DetectionType.Person'></a>

`Person` 3

Human person detected\.

<a name='ResQ.Core.DetectionType.Vehicle'></a>

`Vehicle` 4

Vehicle detected\.

<a name='ResQ.Core.DetectionType.StructuralDamage'></a>

`StructuralDamage` 5

Structural damage detected\.

<a name='ResQ.Core.DetectionType.SmokePlume'></a>

`SmokePlume` 6

Smoke plume detected\.

<a name='ResQ.Core.DetectionType.WaterLevelRise'></a>

`WaterLevelRise` 7

Rising water level detected\.

### Example

```csharp
if (detection.Type == DetectionType.Fire && detection.Confidence > 0.9)
{
    await TriggerAlert(AlertSeverity.Critical, detection.Location);
}
```

### Remarks
These detection types represent what the ResQ AI vision systems can identify
from drone sensor data\. They are used for automated alerting and mission
prioritization\.
