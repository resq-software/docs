---
sidebarTitle: 'RecordEvidenceAsync(EvidenceRecord, CancellationToken)'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\.RecordEvidenceAsync\(EvidenceRecord, CancellationToken\) Method

Records mock evidence metadata in memory\.

```csharp
public System.Threading.Tasks.Task<ResQ.Blockchain.TransactionResult> RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord evidence, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.MockNeoClient.RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord,System.Threading.CancellationToken).evidence'></a>

`evidence` [EvidenceRecord](./ResQ.Blockchain.EvidenceRecord.md 'ResQ\.Blockchain\.EvidenceRecord')

The evidence record to record\.

<a name='ResQ.Blockchain.MockNeoClient.RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [RecordEvidenceAsync\(EvidenceRecord, CancellationToken\)](./ResQ.Blockchain.INeoClient.RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.RecordEvidenceAsync\(ResQ\.Blockchain\.EvidenceRecord, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[TransactionResult](./ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
A [TransactionResult](./ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult') with a generated transaction hash and confirmed status\.

### Example

```csharp
var evidence = new EvidenceRecord(
    IncidentId: "inc-001",
    IpfsCid: "Qmabc123...",
    ContentType: "image/jpeg",
    SizeBytes: 1024567,
    Hash: "sha256:..."
);

var result = await mockClient.RecordEvidenceAsync(evidence);
// Logs: "MOCK: Recorded evidence for incident inc-001, CID: Qmabc123..., TxHash: 0x..."
```

### Remarks
This mock implementation generates a transaction hash and logs the evidence
details including the incident ID and IPFS CID\.
