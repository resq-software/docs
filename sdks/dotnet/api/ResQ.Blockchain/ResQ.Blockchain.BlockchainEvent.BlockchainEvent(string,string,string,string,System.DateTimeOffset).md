### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[BlockchainEvent](./ResQ.Blockchain.BlockchainEvent.md 'ResQ\.Blockchain\.BlockchainEvent')

## BlockchainEvent\(string, string, string, string, DateTimeOffset\) Constructor

Represents an event to be recorded on the blockchain for immutable logging\.

```csharp
public BlockchainEvent(string EventId, string EventType, string Payload, string? IpfsCid, System.DateTimeOffset Timestamp);
```
#### Parameters

<a name='ResQ.Blockchain.BlockchainEvent.BlockchainEvent(string,string,string,string,System.DateTimeOffset).EventId'></a>

`EventId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Unique identifier for this event\.

<a name='ResQ.Blockchain.BlockchainEvent.BlockchainEvent(string,string,string,string,System.DateTimeOffset).EventType'></a>

`EventType` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The type/category of the event\.

<a name='ResQ.Blockchain.BlockchainEvent.BlockchainEvent(string,string,string,string,System.DateTimeOffset).Payload'></a>

`Payload` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

JSON payload containing event\-specific data\.

<a name='ResQ.Blockchain.BlockchainEvent.BlockchainEvent(string,string,string,string,System.DateTimeOffset).IpfsCid'></a>

`IpfsCid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Optional IPFS Content Identifier for associated evidence\.

<a name='ResQ.Blockchain.BlockchainEvent.BlockchainEvent(string,string,string,string,System.DateTimeOffset).Timestamp'></a>

`Timestamp` [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')

UTC timestamp when the event occurred\.

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
