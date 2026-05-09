---
sidebarTitle: 'PdieClient'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## PdieClient Class

Client for the PDIE \(Predictive Disaster Intelligence Engine\) service\.

```csharp
public sealed class PdieClient : System.IDisposable
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; PdieClient

Implements [System\.IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable 'System\.IDisposable')

### Example

```csharp
var client = new PdieClient("http://localhost:8000");

var alerts = await client.GetPreAlertsAsync("sector-7");
foreach (var alert in alerts)
{
    Console.WriteLine($"Alert: {alert.PredictedDisasterType} ({alert.Probability:P})");
}
```

### Remarks
Provides access to predictive alerts and risk assessments from the
intelligence layer\.

| Constructors | |
| :--- | :--- |
| [PdieClient\(string\)](./ResQ.Core.PdieClient.PdieClient(string).md 'ResQ\.Core\.PdieClient\.PdieClient\(string\)') | Initializes a new instance of the [PdieClient](./ResQ.Core.PdieClient.md 'ResQ\.Core\.PdieClient') class\. |

| Methods | |
| :--- | :--- |
| [GetPreAlertsAsync\(string, CancellationToken\)](./ResQ.Core.PdieClient.GetPreAlertsAsync(string,System.Threading.CancellationToken).md 'ResQ\.Core\.PdieClient\.GetPreAlertsAsync\(string, System\.Threading\.CancellationToken\)') | Gets current pre\-alerts, optionally filtered by sector\. |
