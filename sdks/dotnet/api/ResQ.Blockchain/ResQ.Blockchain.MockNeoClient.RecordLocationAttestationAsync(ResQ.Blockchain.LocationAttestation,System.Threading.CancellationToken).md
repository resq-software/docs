### [ResQ\.Blockchain](ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\.RecordLocationAttestationAsync\(LocationAttestation, CancellationToken\) Method

Records a mock location attestation in memory\.

```csharp
public System.Threading.Tasks.Task<ResQ.Blockchain.TransactionResult> RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation attestation, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.MockNeoClient.RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).attestation'></a>

`attestation` [LocationAttestation](ResQ.Blockchain.LocationAttestation.md 'ResQ\.Blockchain\.LocationAttestation')

The location attestation to record\.

<a name='ResQ.Blockchain.MockNeoClient.RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [RecordLocationAttestationAsync\(LocationAttestation, CancellationToken\)](ResQ.Blockchain.INeoClient.RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.RecordLocationAttestationAsync\(ResQ\.Blockchain\.LocationAttestation, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[TransactionResult](ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
A [TransactionResult](ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult') with a generated transaction hash and confirmed status\.

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

var result = await mockClient.RecordLocationAttestationAsync(attestation);
// Logs: "MOCK: Recorded location attestation for drn-001 at (37.7749, -122.4194), TxHash: 0x..."
```

### Remarks
This mock implementation generates a transaction hash and increments the block height,
logging the attestation details including drone ID and coordinates\.
