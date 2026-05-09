### [ResQ\.Blockchain](ResQ.Blockchain.md 'ResQ\.Blockchain')

## INeoClient Interface

Interface for Neo N3 blockchain operations\.

```csharp
public interface INeoClient
```

Derived  
&#8627; [MockNeoClient](ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

### Example

```csharp
// Dependency injection registration
services.AddSingleton<INeoClient, MockNeoClient>();

// Usage
public class IncidentService
{
    private readonly INeoClient _neoClient;
    
    public IncidentService(INeoClient neoClient)
    {
        _neoClient = neoClient;
    }
    
    public async Task RecordIncidentAsync(BlockchainEvent evt)
    {
        var result = await _neoClient.RecordEventAsync(evt);
        if (result.IsConfirmed)
        {
            Console.WriteLine($"Recorded: {result.TransactionHash}");
        }
    }
}
```

### Remarks
This interface defines the contract for interacting with the Neo N3 blockchain\.
Implementations provide methods for recording events, verifying attestations,
and querying blockchain state\. Use [MockNeoClient](ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient') for testing
and development without a real blockchain connection\.

| Methods | |
| :--- | :--- |
| [GetBlockHeightAsync\(CancellationToken\)](ResQ.Blockchain.INeoClient.GetBlockHeightAsync(System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.GetBlockHeightAsync\(System\.Threading\.CancellationToken\)') | Gets the current block height of the blockchain\. |
| [GetEventsByIncidentAsync\(string, CancellationToken\)](ResQ.Blockchain.INeoClient.GetEventsByIncidentAsync(string,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.GetEventsByIncidentAsync\(string, System\.Threading\.CancellationToken\)') | Retrieves all blockchain events associated with a specific incident\. |
| [RecordEventAsync\(BlockchainEvent, CancellationToken\)](ResQ.Blockchain.INeoClient.RecordEventAsync(ResQ.Blockchain.BlockchainEvent,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.RecordEventAsync\(ResQ\.Blockchain\.BlockchainEvent, System\.Threading\.CancellationToken\)') | Records an event on the Neo N3 blockchain\. |
| [RecordEvidenceAsync\(EvidenceRecord, CancellationToken\)](ResQ.Blockchain.INeoClient.RecordEvidenceAsync(ResQ.Blockchain.EvidenceRecord,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.RecordEvidenceAsync\(ResQ\.Blockchain\.EvidenceRecord, System\.Threading\.CancellationToken\)') | Records evidence metadata on the blockchain with a reference to IPFS storage\. |
| [RecordLocationAttestationAsync\(LocationAttestation, CancellationToken\)](ResQ.Blockchain.INeoClient.RecordLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.RecordLocationAttestationAsync\(ResQ\.Blockchain\.LocationAttestation, System\.Threading\.CancellationToken\)') | Records a drone location attestation on the blockchain\. |
| [VerifyLocationAttestationAsync\(LocationAttestation, CancellationToken\)](ResQ.Blockchain.INeoClient.VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.VerifyLocationAttestationAsync\(ResQ\.Blockchain\.LocationAttestation, System\.Threading\.CancellationToken\)') | Verifies a location attestation signature on the blockchain\. |
