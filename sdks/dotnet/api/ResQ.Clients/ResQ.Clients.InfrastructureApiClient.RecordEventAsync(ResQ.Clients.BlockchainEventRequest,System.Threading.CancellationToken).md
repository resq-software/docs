### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[InfrastructureApiClient](./ResQ.Clients.InfrastructureApiClient.md 'ResQ\.Clients\.InfrastructureApiClient')

## InfrastructureApiClient\.RecordEventAsync\(BlockchainEventRequest, CancellationToken\) Method

Records a blockchain event via infrastructure\-api Neo N3 adapter\.
Uses timeout and circuit\-breaker handling without replaying the mutation on failure\.

```csharp
public System.Threading.Tasks.Task<ResQ.Clients.BlockchainEventResponse> RecordEventAsync(ResQ.Clients.BlockchainEventRequest evt, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.InfrastructureApiClient.RecordEventAsync(ResQ.Clients.BlockchainEventRequest,System.Threading.CancellationToken).evt'></a>

`evt` [BlockchainEventRequest](./ResQ.Clients.BlockchainEventRequest.md 'ResQ\.Clients\.BlockchainEventRequest')

<a name='ResQ.Clients.InfrastructureApiClient.RecordEventAsync(ResQ.Clients.BlockchainEventRequest,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[BlockchainEventResponse](./ResQ.Clients.BlockchainEventResponse.md 'ResQ\.Clients\.BlockchainEventResponse')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
