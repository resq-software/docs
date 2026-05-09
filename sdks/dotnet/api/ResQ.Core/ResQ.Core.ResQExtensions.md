### [ResQ\.Core](ResQ.Core.md 'ResQ\.Core')

## ResQExtensions Class

Provides extension methods for ResQ domain types\.

```csharp
public static class ResQExtensions
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; ResQExtensions

### Example

```csharp
// Convert risk score to severity
double riskScore = 0.85;
var severity = riskScore.ToSeverity(); // AlertSeverity.High

// Check if detection is critical
if (detection.IsCritical())
{
    await TriggerImmediateResponse(detection);
}
```

### Remarks
Contains utility extension methods that simplify working with ResQ types,
including severity conversion and critical detection checks\.

| Methods | |
| :--- | :--- |
| [IsCritical\(this Detection\)](ResQ.Core.ResQExtensions.IsCritical(thisResQ.Core.Detection).md 'ResQ\.Core\.ResQExtensions\.IsCritical\(this ResQ\.Core\.Detection\)') | Determines if a detection is critical and requires immediate action\. |
| [ToSeverity\(this double\)](ResQ.Core.ResQExtensions.ToSeverity(thisdouble).md 'ResQ\.Core\.ResQExtensions\.ToSeverity\(this double\)') | Converts a risk score to an alert severity level\. |
