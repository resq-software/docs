---
sidebarTitle: 'RecordEvidenceAsync(EvidenceRecord, CancellationToken)'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[INeoClient](./ResQ.Blockchain.INeoClient.md 'ResQ\.Blockchain\.INeoClient')

## INeoClient\.RecordEvidenceAsync\(EvidenceRecord, CancellationToken\) Method

Records evidence metadata on the blockchain with a reference to IPFS storage\.

```csharp
System.Threading.Tasks.Task<ResQ.Blockchain.TransactionResult> RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord evidence, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.INeoClient.RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord,System.Threading.CancellationToken).evidence'></a>

`evidence` [EvidenceRecord](./ResQ.Blockchain.EvidenceRecord.md 'ResQ\.Blockchain\.EvidenceRecord')

The evidence record containing IPFS CID and metadata\.

<a name='ResQ.Blockchain.INeoClient.RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord,System.Threading.CancellationToken).cancellationToken'></a>

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
var evidence = new EvidenceRecord(
    IncidentId: "inc-001",
    IpfsCid: "Qmabc123...",
    ContentType: "image/jpeg",
    SizeBytes: 1024567,
    Hash: "sha256:..."
);

var result = await neoClient.RecordEvidenceAsync(evidence);
Console.WriteLine($"Evidence recorded: {result.TransactionHash}");
```

### Remarks
Evidence is stored on IPFS for decentralized storage, while the blockchain records
a permanent, immutable reference to the evidence along with its hash for integrity verification\.
