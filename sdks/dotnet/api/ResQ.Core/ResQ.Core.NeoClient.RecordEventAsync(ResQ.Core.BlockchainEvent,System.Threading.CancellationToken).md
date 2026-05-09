---
sidebarTitle: 'RecordEventAsync(BlockchainEvent, CancellationToken)'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[NeoClient](./ResQ.Core.NeoClient.md 'ResQ\.Core\.NeoClient')

## NeoClient\.RecordEventAsync\(BlockchainEvent, CancellationToken\) Method

Records an event on the Neo N3 blockchain\.

```csharp
public System.Threading.Tasks.Task<ResQ.Core.TransactionResult> RecordEventAsync(ResQ.Core.BlockchainEvent evt, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Core.NeoClient.RecordEventAsync(ResQ.Core.BlockchainEvent,System.Threading.CancellationToken).evt'></a>

`evt` [BlockchainEvent](./ResQ.Core.BlockchainEvent.md 'ResQ\.Core\.BlockchainEvent')

The event to record\.

<a name='ResQ.Core.NeoClient.RecordEventAsync(ResQ.Core.BlockchainEvent,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[TransactionResult](./ResQ.Core.TransactionResult.md 'ResQ\.Core\.TransactionResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
Transaction result including hash and status\.
