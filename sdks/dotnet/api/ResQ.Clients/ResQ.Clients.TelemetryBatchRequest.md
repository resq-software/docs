### [ResQ\.Clients](ResQ.Clients.md 'ResQ\.Clients')

## TelemetryBatchRequest Class

Request containing a batch of telemetry packets from a drone\.

```csharp
public record TelemetryBatchRequest : System.IEquatable<ResQ.Clients.TelemetryBatchRequest>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; TelemetryBatchRequest

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[TelemetryBatchRequest](ResQ.Clients.TelemetryBatchRequest.md 'ResQ\.Clients\.TelemetryBatchRequest')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

| Constructors | |
| :--- | :--- |
| [TelemetryBatchRequest\(string, List&lt;TelemetryPacket&gt;, List&lt;Detection&gt;\)](ResQ.Clients.TelemetryBatchRequest.TelemetryBatchRequest(string,System.Collections.Generic.List_ResQ.Clients.TelemetryPacket_,System.Collections.Generic.List_ResQ.Clients.Detection_).md 'ResQ\.Clients\.TelemetryBatchRequest\.TelemetryBatchRequest\(string, System\.Collections\.Generic\.List\<ResQ\.Clients\.TelemetryPacket\>, System\.Collections\.Generic\.List\<ResQ\.Clients\.Detection\>\)') | Request containing a batch of telemetry packets from a drone\. |

| Properties | |
| :--- | :--- |
| [Detections](ResQ.Clients.TelemetryBatchRequest.Detections.md 'ResQ\.Clients\.TelemetryBatchRequest\.Detections') | Optional list of AI detections from this batch\. |
| [DroneId](ResQ.Clients.TelemetryBatchRequest.DroneId.md 'ResQ\.Clients\.TelemetryBatchRequest\.DroneId') | The unique identifier of the drone\. |
| [Packets](ResQ.Clients.TelemetryBatchRequest.Packets.md 'ResQ\.Clients\.TelemetryBatchRequest\.Packets') | List of telemetry packets in this batch\. |
