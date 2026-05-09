### [ResQ\.Clients](ResQ.Clients.md 'ResQ\.Clients').[CoordinationHceClient](ResQ.Clients.CoordinationHceClient.md 'ResQ\.Clients\.CoordinationHceClient')

## CoordinationHceClient\.SendTelemetryBatchAsync\(TelemetryBatchRequest, CancellationToken\) Method

Sends a batch of telemetry packets from a drone\.
Uses timeout and circuit\-breaker handling without replaying the mutation on failure\.

```csharp
public System.Threading.Tasks.Task SendTelemetryBatchAsync(ResQ.Clients.TelemetryBatchRequest batch, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.CoordinationHceClient.SendTelemetryBatchAsync(ResQ.Clients.TelemetryBatchRequest,System.Threading.CancellationToken).batch'></a>

`batch` [TelemetryBatchRequest](ResQ.Clients.TelemetryBatchRequest.md 'ResQ\.Clients\.TelemetryBatchRequest')

<a name='ResQ.Clients.CoordinationHceClient.SendTelemetryBatchAsync(ResQ.Clients.TelemetryBatchRequest,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task 'System\.Threading\.Tasks\.Task')
