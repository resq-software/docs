### [ResQ\.Core](ResQ.Core.md 'ResQ\.Core').[ResQExtensions](ResQ.Core.ResQExtensions.md 'ResQ\.Core\.ResQExtensions')

## ResQExtensions\.ToSeverity\(this double\) Method

Converts a risk score to an alert severity level\.

```csharp
public static ResQ.Core.AlertSeverity ToSeverity(this double riskScore);
```
#### Parameters

<a name='ResQ.Core.ResQExtensions.ToSeverity(thisdouble).riskScore'></a>

`riskScore` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

The risk score \(0\.0 to 1\.0\)\.

#### Returns
[AlertSeverity](ResQ.Core.AlertSeverity.md 'ResQ\.Core\.AlertSeverity')  
The corresponding alert severity\.

### Remarks
Risk score thresholds:
- Critical: >= 0.9
- High: >= 0.75
- Medium: >= 0.6
- Low: < 0.6
