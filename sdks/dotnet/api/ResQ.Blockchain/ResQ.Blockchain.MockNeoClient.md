### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain')

## MockNeoClient Class

Mock implementation of [INeoClient](./ResQ.Blockchain.INeoClient.md 'ResQ\.Blockchain\.INeoClient') for testing and development\.

```csharp
public class MockNeoClient : ResQ.Blockchain.INeoClient
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; MockNeoClient

Implements [INeoClient](./ResQ.Blockchain.INeoClient.md 'ResQ\.Blockchain\.INeoClient')

### Example

```csharp
// Registration with dependency injection
services.AddSingleton<INeoClient, MockNeoClient>();

// Direct usage
var mockClient = new MockNeoClient(logger);
var result = await mockClient.RecordEventAsync(evt);
Console.WriteLine($"Mock TX: {result.TransactionHash}");
```

### Remarks
This mock client provides an in\-memory implementation of the Neo N3 blockchain interface,
suitable for unit testing and local development without requiring a real blockchain connection\.
All operations succeed immediately and generate deterministic fake transaction hashes\.


Events are stored in memory and can be retrieved by incident ID. Block height increments
with each transaction. No actual blockchain transactions are performed.

| Constructors | |
| :--- | :--- |
| [MockNeoClient\(ILogger&lt;MockNeoClient&gt;\)](./ResQ.Blockchain.MockNeoClient.MockNeoClient(Microsoft.Extensions.Logging.ILogger_ResQ.Blockchain.MockNeoClient_).md 'ResQ\.Blockchain\.MockNeoClient\.MockNeoClient\(Microsoft\.Extensions\.Logging\.ILogger\<ResQ\.Blockchain\.MockNeoClient\>\)') | Initializes a new instance of the [MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient') class\. |

| Methods | |
| :--- | :--- |
| [GetBlockHeightAsync\(CancellationToken\)](./ResQ.Blockchain.MockNeoClient.GetBlockHeightAsync(System.Threading.CancellationToken).md 'ResQ\.Blockchain\.MockNeoClient\.GetBlockHeightAsync\(System\.Threading\.CancellationToken\)') | Gets the current mock block height\. |
| [GetEventsByIncidentAsync\(string, CancellationToken\)](./ResQ.Blockchain.MockNeoClient.GetEventsByIncidentAsync(string,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.MockNeoClient\.GetEventsByIncidentAsync\(string, System\.Threading\.CancellationToken\)') | Retrieves mock events by incident ID from the in\-memory store\. |
| [RecordEventAsync\(BlockchainEvent, CancellationToken\)](./ResQ.Blockchain.MockNeoClient.RecordEventAsync(ResQ.Blockchain.BlockchainEvent,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.MockNeoClient\.RecordEventAsync\(ResQ\.Blockchain\.BlockchainEvent, System\.Threading\.CancellationToken\)') | Records a mock blockchain event in memory\. |
| [RecordEvidenceAsync\(EvidenceRecord, CancellationToken\)](./ResQ.Blockchain.MockNeoClient.RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.MockNeoClient\.RecordEvidenceAsync\(ResQ\.Blockchain\.EvidenceRecord, System\.Threading\.CancellationToken\)') | Records mock evidence metadata in memory\. |
| [RecordLocationAttestationAsync\(LocationAttestation, CancellationToken\)](./ResQ.Blockchain.MockNeoClient.RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.MockNeoClient\.RecordLocationAttestationAsync\(ResQ\.Blockchain\.LocationAttestation, System\.Threading\.CancellationToken\)') | Records a mock location attestation in memory\. |
| [VerifyLocationAttestationAsync\(LocationAttestation, CancellationToken\)](./ResQ.Blockchain.MockNeoClient.VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.MockNeoClient\.VerifyLocationAttestationAsync\(ResQ\.Blockchain\.LocationAttestation, System\.Threading\.CancellationToken\)') | Verifies a location attestation in mock mode\. |
