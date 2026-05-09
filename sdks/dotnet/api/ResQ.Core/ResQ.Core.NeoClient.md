### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## NeoClient Class

Client for interacting with the Neo N3 blockchain\.

```csharp
public sealed class NeoClient : System.IDisposable
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; NeoClient

Implements [System\.IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable 'System\.IDisposable')

### Example

```csharp
using var client = new NeoClient(new NeoConfig { MockMode = true });

var evt = new BlockchainEvent
{
    EventId = "evt-001",
    EventType = BlockchainEventType.IncidentDetected
};

var result = await client.RecordEventAsync(evt);
Console.WriteLine($"Transaction: {result.TxHash}");
```

### Remarks
Provides methods for recording events, verifying attestations, and querying
transaction status on the Neo N3 blockchain\. Supports both real blockchain
operations and mock mode for testing\.

| Constructors | |
| :--- | :--- |
| [NeoClient\(NeoConfig\)](./ResQ.Core.NeoClient.NeoClient(ResQ.Core.NeoConfig).md 'ResQ\.Core\.NeoClient\.NeoClient\(ResQ\.Core\.NeoConfig\)') | Initializes a new instance of the [NeoClient](./ResQ.Core.NeoClient.md 'ResQ\.Core\.NeoClient') class\. |

| Methods | |
| :--- | :--- |
| [GetTransactionStatusAsync\(string, CancellationToken\)](./ResQ.Core.NeoClient.GetTransactionStatusAsync(string,System.Threading.CancellationToken).md 'ResQ\.Core\.NeoClient\.GetTransactionStatusAsync\(string, System\.Threading\.CancellationToken\)') | Gets the status of a blockchain transaction\. |
| [RecordEventAsync\(BlockchainEvent, CancellationToken\)](./ResQ.Core.NeoClient.RecordEventAsync(ResQ.Core.BlockchainEvent,System.Threading.CancellationToken).md 'ResQ\.Core\.NeoClient\.RecordEventAsync\(ResQ\.Core\.BlockchainEvent, System\.Threading\.CancellationToken\)') | Records an event on the Neo N3 blockchain\. |
| [RecordEvidenceAsync\(string, string, string, CancellationToken\)](./ResQ.Core.NeoClient.RecordEvidenceAsync(string,string,string,System.Threading.CancellationToken).md 'ResQ\.Core\.NeoClient\.RecordEvidenceAsync\(string, string, string, System\.Threading\.CancellationToken\)') | Records evidence linked to an incident on the blockchain\. |
| [VerifyLocationAttestationAsync\(string, Location, DateTimeOffset, CancellationToken\)](./ResQ.Core.NeoClient.VerifyLocationAttestationAsync(string,ResQ.Core.Location,System.DateTimeOffset,System.Threading.CancellationToken).md 'ResQ\.Core\.NeoClient\.VerifyLocationAttestationAsync\(string, ResQ\.Core\.Location, System\.DateTimeOffset, System\.Threading\.CancellationToken\)') | Verifies a location attestation on the blockchain\. |
