---
sidebarTitle: 'BlockchainEventType'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## BlockchainEventType Enum

Defines types of blockchain events for immutable logging\.

```csharp
public enum BlockchainEventType
```
### Fields

<a name='ResQ.Core.BlockchainEventType.Unspecified'></a>

`Unspecified` 0

Unspecified or unknown event type\.

<a name='ResQ.Core.BlockchainEventType.IncidentDetected'></a>

`IncidentDetected` 1

New incident detected by sensors or AI\.

<a name='ResQ.Core.BlockchainEventType.IncidentVerified'></a>

`IncidentVerified` 2

Incident has been verified by human operators\.

<a name='ResQ.Core.BlockchainEventType.MissionStarted'></a>

`MissionStarted` 3

Drone mission has started\.

<a name='ResQ.Core.BlockchainEventType.MissionCompleted'></a>

`MissionCompleted` 4

Drone mission has completed\.

<a name='ResQ.Core.BlockchainEventType.DeliveryConfirmed'></a>

`DeliveryConfirmed` 5

Supply delivery has been confirmed\.

<a name='ResQ.Core.BlockchainEventType.LocationAttestation'></a>

`LocationAttestation` 6

Drone location has been attested on blockchain\.

<a name='ResQ.Core.BlockchainEventType.EvidenceSubmitted'></a>

`EvidenceSubmitted` 7

Evidence has been submitted to storage and blockchain\.

<a name='ResQ.Core.BlockchainEventType.PreAlertIssued'></a>

`PreAlertIssued` 8

Pre\-alert issued by predictive system\.

<a name='ResQ.Core.BlockchainEventType.SwarmDeployment'></a>

`SwarmDeployment` 9

Drone swarm has been deployed\.

### Example

```csharp
var evt = new BlockchainEvent
{
    EventType = BlockchainEventType.IncidentDetected,
    Timestamp = DateTimeOffset.UtcNow,
    Location = incident.Location
};
await neoClient.RecordEventAsync(evt);
```

### Remarks
These event types categorize the various events that are recorded on the
Neo N3 blockchain for audit trails and verification\.
