---
sidebarTitle: 'SendTelemetryAsync(TelemetryPacket, CancellationToken)'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[HceClient](./ResQ.Core.HceClient.md 'ResQ\.Core\.HceClient')

## HceClient\.SendTelemetryAsync\(TelemetryPacket, CancellationToken\) Method

Sends telemetry data from a drone to the HCE service\.

```csharp
public System.Threading.Tasks.Task<bool> SendTelemetryAsync(ResQ.Core.TelemetryPacket packet, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Core.HceClient.SendTelemetryAsync(ResQ.Core.TelemetryPacket,System.Threading.CancellationToken).packet'></a>

`packet` [TelemetryPacket](./ResQ.Core.TelemetryPacket.md 'ResQ\.Core\.TelemetryPacket')

The telemetry packet to send\.

<a name='ResQ.Core.HceClient.SendTelemetryAsync(ResQ.Core.TelemetryPacket,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
True if the telemetry was accepted\.
