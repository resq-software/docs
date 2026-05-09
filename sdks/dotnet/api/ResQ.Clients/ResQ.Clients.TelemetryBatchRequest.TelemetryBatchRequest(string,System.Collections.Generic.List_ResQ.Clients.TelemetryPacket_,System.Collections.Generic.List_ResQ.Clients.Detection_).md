---
sidebarTitle: 'TelemetryBatchRequest(string, TelemetryPacket_, Detection_)'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[TelemetryBatchRequest](./ResQ.Clients.TelemetryBatchRequest.md 'ResQ\.Clients\.TelemetryBatchRequest')

## TelemetryBatchRequest\(string, List\<TelemetryPacket\>, List\<Detection\>\) Constructor

Request containing a batch of telemetry packets from a drone\.

```csharp
public TelemetryBatchRequest(string DroneId, System.Collections.Generic.List<ResQ.Clients.TelemetryPacket> Packets, System.Collections.Generic.List<ResQ.Clients.Detection>? Detections=null);
```
#### Parameters

<a name='ResQ.Clients.TelemetryBatchRequest.TelemetryBatchRequest(string,System.Collections.Generic.List_ResQ.Clients.TelemetryPacket_,System.Collections.Generic.List_ResQ.Clients.Detection_).DroneId'></a>

`DroneId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The unique identifier of the drone\.

<a name='ResQ.Clients.TelemetryBatchRequest.TelemetryBatchRequest(string,System.Collections.Generic.List_ResQ.Clients.TelemetryPacket_,System.Collections.Generic.List_ResQ.Clients.Detection_).Packets'></a>

`Packets` [System\.Collections\.Generic\.List&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1 'System\.Collections\.Generic\.List\`1')[TelemetryPacket](./ResQ.Clients.TelemetryPacket.md 'ResQ\.Clients\.TelemetryPacket')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1 'System\.Collections\.Generic\.List\`1')

List of telemetry packets in this batch\.

<a name='ResQ.Clients.TelemetryBatchRequest.TelemetryBatchRequest(string,System.Collections.Generic.List_ResQ.Clients.TelemetryPacket_,System.Collections.Generic.List_ResQ.Clients.Detection_).Detections'></a>

`Detections` [System\.Collections\.Generic\.List&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1 'System\.Collections\.Generic\.List\`1')[Detection](./ResQ.Clients.Detection.md 'ResQ\.Clients\.Detection')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1 'System\.Collections\.Generic\.List\`1')

Optional list of AI detections from this batch\.
