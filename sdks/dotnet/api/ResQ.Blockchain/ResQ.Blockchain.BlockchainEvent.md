---
sidebarTitle: 'BlockchainEvent'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain')

## BlockchainEvent Class

Represents an event to be recorded on the blockchain for immutable logging\.

```csharp
public record BlockchainEvent : System.IEquatable<ResQ.Blockchain.BlockchainEvent>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → BlockchainEvent

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[BlockchainEvent](./ResQ.Blockchain.BlockchainEvent.md 'ResQ\.Blockchain\.BlockchainEvent')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var evt = new BlockchainEvent(
    EventId: "evt-001",
    EventType: "IncidentDetected",
    Payload: "{\"incidentId\":\"inc-001\",\"severity\":\"High\"}",
    IpfsCid: "Qmabc123...",
    Timestamp: DateTimeOffset.UtcNow
);

var result = await neoClient.RecordEventAsync(evt);
```

### Remarks
Blockchain events provide an immutable audit trail of critical system activities\.
Each event is assigned a unique ID and can optionally reference IPFS content
for additional evidence storage\.

| Constructors | |
| :--- | :--- |
| [BlockchainEvent\(string, string, string, string, DateTimeOffset\)](./ResQ.Blockchain.BlockchainEvent.BlockchainEvent(string,string,string,string,System.DateTimeOffset).md 'ResQ\.Blockchain\.BlockchainEvent\.BlockchainEvent\(string, string, string, string, System\.DateTimeOffset\)') | Represents an event to be recorded on the blockchain for immutable logging\. |

| Properties | |
| :--- | :--- |
| [EventId](./ResQ.Blockchain.BlockchainEvent.EventId.md 'ResQ\.Blockchain\.BlockchainEvent\.EventId') | Unique identifier for this event\. |
| [EventType](./ResQ.Blockchain.BlockchainEvent.EventType.md 'ResQ\.Blockchain\.BlockchainEvent\.EventType') | The type/category of the event\. |
| [IpfsCid](./ResQ.Blockchain.BlockchainEvent.IpfsCid.md 'ResQ\.Blockchain\.BlockchainEvent\.IpfsCid') | Optional IPFS Content Identifier for associated evidence\. |
| [Payload](./ResQ.Blockchain.BlockchainEvent.Payload.md 'ResQ\.Blockchain\.BlockchainEvent\.Payload') | JSON payload containing event\-specific data\. |
| [Timestamp](./ResQ.Blockchain.BlockchainEvent.Timestamp.md 'ResQ\.Blockchain\.BlockchainEvent\.Timestamp') | UTC timestamp when the event occurred\. |
