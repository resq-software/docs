---
sidebarTitle: 'HceClient'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## HceClient Class

Client for the HCE \(Human\-Centric Emergency\) coordination layer\.

```csharp
public sealed class HceClient : System.IDisposable
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → HceClient

Implements [System\.IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable 'System\.IDisposable')

### Example

```csharp
var client = new HceClient("http://localhost:3000");

var success = await client.SendTelemetryAsync(telemetryPacket);
if (success)
{
    Console.WriteLine("Telemetry sent successfully");
}
```

### Remarks
Provides methods for sending telemetry and reporting detections to the
HCE coordination service\.

| Constructors | |
| :--- | :--- |
| [HceClient\(string\)](./ResQ.Core.HceClient.HceClient(string).md 'ResQ\.Core\.HceClient\.HceClient\(string\)') | Initializes a new instance of the [HceClient](./ResQ.Core.HceClient.md 'ResQ\.Core\.HceClient') class\. |

| Methods | |
| :--- | :--- |
| [ReportDetectionAsync\(Detection, string, CancellationToken\)](./ResQ.Core.HceClient.ReportDetectionAsync(ResQ.Core.Detection,string,System.Threading.CancellationToken).md 'ResQ\.Core\.HceClient\.ReportDetectionAsync\(ResQ\.Core\.Detection, string, System\.Threading\.CancellationToken\)') | Reports a critical detection to the HCE service\. |
| [SendTelemetryAsync\(TelemetryPacket, CancellationToken\)](./ResQ.Core.HceClient.SendTelemetryAsync(ResQ.Core.TelemetryPacket,System.Threading.CancellationToken).md 'ResQ\.Core\.HceClient\.SendTelemetryAsync\(ResQ\.Core\.TelemetryPacket, System\.Threading\.CancellationToken\)') | Sends telemetry data from a drone to the HCE service\. |
