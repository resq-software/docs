---
sidebarTitle: 'RecordEventAsync(BlockchainEvent, CancellationToken)'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[INeoClient](./ResQ.Blockchain.INeoClient.md 'ResQ\.Blockchain\.INeoClient')

## INeoClient\.RecordEventAsync\(BlockchainEvent, CancellationToken\) Method

Records an event on the Neo N3 blockchain\.

```csharp
System.Threading.Tasks.Task<ResQ.Blockchain.TransactionResult> RecordEventAsync(ResQ.Blockchain.BlockchainEvent evt, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.INeoClient.RecordEventAsync(ResQ.Blockchain.BlockchainEvent,System.Threading.CancellationToken).evt'></a>

`evt` [BlockchainEvent](./ResQ.Blockchain.BlockchainEvent.md 'ResQ\.Blockchain\.BlockchainEvent')

The blockchain event to record\.

<a name='ResQ.Blockchain.INeoClient.RecordEventAsync(ResQ.Blockchain.BlockchainEvent,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[TransactionResult](./ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
A [TransactionResult](./ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult') containing the transaction hash and confirmation status\.

#### Exceptions

[System\.InvalidOperationException](https://learn.microsoft.com/en-us/dotnet/api/system.invalidoperationexception 'System\.InvalidOperationException')  
Thrown when the blockchain operation fails\.

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
var evt = new BlockchainEvent(
    EventId: "evt-001",
    EventType: "IncidentDetected",
    Payload: "{\"id\":\"inc-001\"}",
    IpfsCid: null,
    Timestamp: DateTimeOffset.UtcNow
);

var result = await neoClient.RecordEventAsync(evt);
Console.WriteLine($"Transaction: {result.TransactionHash}");
```

### Remarks
Events are permanently recorded on the blockchain and provide an immutable audit trail\.
The operation may take several seconds to complete as it waits for transaction confirmation\.
