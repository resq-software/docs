---
sidebarTitle: 'DtsopClient'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## DtsopClient Class

Client for the DTSOP \(Drone Tactical Strategy Optimization\) service\.

```csharp
public sealed class DtsopClient : System.IDisposable
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → DtsopClient

Implements [System\.IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable 'System\.IDisposable')

### Example

```csharp
var client = new DtsopClient("http://localhost:9000");

var strategy = await client.RequestStrategyAsync("scenario-001");
Console.WriteLine($"Coverage: {strategy.EstimatedCoveragePercent:F1}%");
```

### Remarks
Provides access to optimization strategies and deployment recommendations
from the simulation layer\.

| Constructors | |
| :--- | :--- |
| [DtsopClient\(string\)](./ResQ.Core.DtsopClient.DtsopClient(string).md 'ResQ\.Core\.DtsopClient\.DtsopClient\(string\)') | Initializes a new instance of the [DtsopClient](./ResQ.Core.DtsopClient.md 'ResQ\.Core\.DtsopClient') class\. |

| Methods | |
| :--- | :--- |
| [RequestStrategyAsync\(string, CancellationToken\)](./ResQ.Core.DtsopClient.RequestStrategyAsync(string,System.Threading.CancellationToken).md 'ResQ\.Core\.DtsopClient\.RequestStrategyAsync\(string, System\.Threading\.CancellationToken\)') | Requests an optimization strategy for a scenario\. |
