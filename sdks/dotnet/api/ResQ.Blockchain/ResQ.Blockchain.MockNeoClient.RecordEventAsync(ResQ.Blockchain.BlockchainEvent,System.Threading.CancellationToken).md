---
sidebarTitle: 'RecordEventAsync(BlockchainEvent, CancellationToken)'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\.RecordEventAsync\(BlockchainEvent, CancellationToken\) Method

Records a mock blockchain event in memory\.

```csharp
public System.Threading.Tasks.Task<ResQ.Blockchain.TransactionResult> RecordEventAsync(ResQ.Blockchain.BlockchainEvent evt, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.MockNeoClient.RecordEventAsync(ResQ.Blockchain.BlockchainEvent,System.Threading.CancellationToken).evt'></a>

`evt` [BlockchainEvent](./ResQ.Blockchain.BlockchainEvent.md 'ResQ\.Blockchain\.BlockchainEvent')

The blockchain event to record\.

<a name='ResQ.Blockchain.MockNeoClient.RecordEventAsync(ResQ.Blockchain.BlockchainEvent,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [RecordEventAsync\(BlockchainEvent, CancellationToken\)](./ResQ.Blockchain.INeoClient.RecordEventAsync(ResQ.Blockchain.BlockchainEvent,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.RecordEventAsync\(ResQ\.Blockchain\.BlockchainEvent, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[TransactionResult](./ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
A [TransactionResult](./ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult') with a generated transaction hash and confirmed status\.

### Example

```csharp
var evt = new BlockchainEvent(
    EventId: "evt-001",
    EventType: "IncidentDetected",
    Payload: "{\"incident\":\"inc-001\"}",
    IpfsCid: null,
    Timestamp: DateTimeOffset.UtcNow
);

var result = await mockClient.RecordEventAsync(evt);
// Logs: "MOCK: Recorded event evt-001 of type IncidentDetected, TxHash: 0x..."
```

### Remarks
This mock implementation:
- Generates a random transaction hash using cryptographic random bytes
- Increments the internal block height
- Stores the event in memory, indexed by incident ID if present in payload
- Logs the operation at Information level
