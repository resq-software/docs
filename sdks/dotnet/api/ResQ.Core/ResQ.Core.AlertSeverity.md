### [ResQ\.Core](ResQ.Core.md 'ResQ\.Core')

## AlertSeverity Enum

Defines alert severity levels for prioritization\.

```csharp
public enum AlertSeverity
```
### Fields

<a name='ResQ.Core.AlertSeverity.Low'></a>

`Low` 0

Low priority \- routine information\.

<a name='ResQ.Core.AlertSeverity.Medium'></a>

`Medium` 1

Medium priority \- notable event\.

<a name='ResQ.Core.AlertSeverity.High'></a>

`High` 2

High priority \- significant issue\.

<a name='ResQ.Core.AlertSeverity.Critical'></a>

`Critical` 3

Critical priority \- immediate action required\.

### Example

```csharp
// Convert confidence to severity
var severity = detection.Confidence switch
{
    >= 0.95 => AlertSeverity.Critical,
    >= 0.85 => AlertSeverity.High,
    >= 0.70 => AlertSeverity.Medium,
    _ => AlertSeverity.Low
};
```

### Remarks
Severity levels determine response urgency and notification routing\.
They can be derived from confidence scores or risk assessments\.
