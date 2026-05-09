### [ResQ\.Core](ResQ.Core.md 'ResQ\.Core')

## BlockchainEvent Class

Represents a blockchain event for immutable logging\.

```csharp
public record BlockchainEvent : System.IEquatable<ResQ.Core.BlockchainEvent>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; BlockchainEvent

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[BlockchainEvent](ResQ.Core.BlockchainEvent.md 'ResQ\.Core\.BlockchainEvent')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var evt = new BlockchainEvent
{
    EventId = "evt-001",
    EventType = BlockchainEventType.IncidentDetected,
    Location = new Location(37.7749, -122.4194),
    EvidenceCid = "Qmabc123...",
    Metadata = new Dictionary<string, object>
    {
        ["incidentId"] = "inc-001",
        ["severity"] = "High"
    }
};
```

### Remarks
Blockchain events provide tamper\-proof records of system activities\.
They can include metadata and links to off\-chain evidence\.

| Properties | |
| :--- | :--- |
| [DroneId](ResQ.Core.BlockchainEvent.DroneId.md 'ResQ\.Core\.BlockchainEvent\.DroneId') | Drone ID associated with the event, if applicable\. |
| [EventId](ResQ.Core.BlockchainEvent.EventId.md 'ResQ\.Core\.BlockchainEvent\.EventId') | Unique identifier for this event\. |
| [EventType](ResQ.Core.BlockchainEvent.EventType.md 'ResQ\.Core\.BlockchainEvent\.EventType') | Type of blockchain event\. |
| [EvidenceCid](ResQ.Core.BlockchainEvent.EvidenceCid.md 'ResQ\.Core\.BlockchainEvent\.EvidenceCid') | IPFS CID of associated evidence, if any\. |
| [Location](ResQ.Core.BlockchainEvent.Location.md 'ResQ\.Core\.BlockchainEvent\.Location') | Geographic location associated with the event, if applicable\. |
| [Metadata](ResQ.Core.BlockchainEvent.Metadata.md 'ResQ\.Core\.BlockchainEvent\.Metadata') | Additional metadata as key\-value pairs\. |
| [Timestamp](ResQ.Core.BlockchainEvent.Timestamp.md 'ResQ\.Core\.BlockchainEvent\.Timestamp') | UTC timestamp when the event occurred\. |
