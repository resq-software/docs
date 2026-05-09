### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## PreAlert Class

Represents a pre\-alert from the PDIE \(Predictive Disaster Intelligence Engine\)\.

```csharp
public record PreAlert : System.IEquatable<ResQ.Core.PreAlert>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; PreAlert

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[PreAlert](./ResQ.Core.PreAlert.md 'ResQ\.Core\.PreAlert')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var alert = new PreAlert
{
    AlertId = "pa-001",
    SectorId = "sector-7",
    PredictedDisasterType = DisasterType.Wildfire,
    Probability = 0.85f,
    ForecastHorizonHours = 24,
    Severity = AlertSeverity.High
};
```

### Remarks
Pre\-alerts are predictions of potential disasters before they occur, allowing
for proactive response preparation\. They include probability, timing, and
severity estimates\.

| Properties | |
| :--- | :--- |
| [AlertId](./ResQ.Core.PreAlert.AlertId.md 'ResQ\.Core\.PreAlert\.AlertId') | Unique identifier for this pre\-alert\. |
| [CreatedAt](./ResQ.Core.PreAlert.CreatedAt.md 'ResQ\.Core\.PreAlert\.CreatedAt') | UTC timestamp when the pre\-alert was created\. |
| [ForecastHorizonHours](./ResQ.Core.PreAlert.ForecastHorizonHours.md 'ResQ\.Core\.PreAlert\.ForecastHorizonHours') | Forecast time horizon in hours\. |
| [PredictedDisasterType](./ResQ.Core.PreAlert.PredictedDisasterType.md 'ResQ\.Core\.PreAlert\.PredictedDisasterType') | Predicted type of disaster\. |
| [Probability](./ResQ.Core.PreAlert.Probability.md 'ResQ\.Core\.PreAlert\.Probability') | Probability of the disaster occurring \(0\.0 to 1\.0\)\. |
| [SectorId](./ResQ.Core.PreAlert.SectorId.md 'ResQ\.Core\.PreAlert\.SectorId') | Geographic sector this alert applies to\. |
| [Severity](./ResQ.Core.PreAlert.Severity.md 'ResQ\.Core\.PreAlert\.Severity') | Severity level of the predicted disaster\. |
