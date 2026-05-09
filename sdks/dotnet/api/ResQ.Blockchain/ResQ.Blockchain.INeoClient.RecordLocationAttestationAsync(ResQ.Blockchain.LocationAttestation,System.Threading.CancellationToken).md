---
sidebarTitle: 'RecordLocationAttestationAsync(LocationAttestation, CancellationToken)'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[INeoClient](./ResQ.Blockchain.INeoClient.md 'ResQ\.Blockchain\.INeoClient')

## INeoClient\.RecordLocationAttestationAsync\(LocationAttestation, CancellationToken\) Method

Records a drone location attestation on the blockchain\.

```csharp
System.Threading.Tasks.Task<ResQ.Blockchain.TransactionResult> RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation attestation, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.INeoClient.RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).attestation'></a>

`attestation` [LocationAttestation](./ResQ.Blockchain.LocationAttestation.md 'ResQ\.Blockchain\.LocationAttestation')

The location attestation containing drone position and signature\.

<a name='ResQ.Blockchain.INeoClient.RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).cancellationToken'></a>

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
var attestation = new LocationAttestation(
    DroneId: "drn-001",
    Latitude: 37.7749,
    Longitude: -122.4194,
    Altitude: 100.0,
    Timestamp: DateTimeOffset.UtcNow,
    Signature: "0x..."
);

var result = await neoClient.RecordLocationAttestationAsync(attestation);
```

### Remarks
Location attestations provide cryptographic proof of a drone's position at a specific time\.
This is useful for compliance, incident reconstruction, and verification of mission execution\.
