---
sidebarTitle: 'GetEventsByIncidentAsync(string, CancellationToken)'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\.GetEventsByIncidentAsync\(string, CancellationToken\) Method

Retrieves mock events by incident ID from the in\-memory store\.

```csharp
public System.Threading.Tasks.Task<System.Collections.Generic.IReadOnlyList<ResQ.Blockchain.BlockchainEvent>> GetEventsByIncidentAsync(string incidentId, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.MockNeoClient.GetEventsByIncidentAsync(string,System.Threading.CancellationToken).incidentId'></a>

`incidentId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The incident ID to query\.

<a name='ResQ.Blockchain.MockNeoClient.GetEventsByIncidentAsync(string,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [GetEventsByIncidentAsync\(string, CancellationToken\)](./ResQ.Blockchain.INeoClient.GetEventsByIncidentAsync(string,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.GetEventsByIncidentAsync\(string, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Collections\.Generic\.IReadOnlyList&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1 'System\.Collections\.Generic\.IReadOnlyList\`1')[BlockchainEvent](./ResQ.Blockchain.BlockchainEvent.md 'ResQ\.Blockchain\.BlockchainEvent')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1 'System\.Collections\.Generic\.IReadOnlyList\`1')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
A read\-only list of events associated with the incident, or an empty list if none exist\.

### Example

```csharp
// First record some events
var evt1 = new BlockchainEvent(..., Payload: "{\"incident\":\"inc-001\"}");
await mockClient.RecordEventAsync(evt1);

// Then retrieve them
var events = await mockClient.GetEventsByIncidentAsync("inc-001");
Console.WriteLine($"Found {events.Count} events");
```

### Remarks
Events are stored when recorded via [RecordEventAsync\(BlockchainEvent, CancellationToken\)](./ResQ.Blockchain.MockNeoClient.RecordEventAsync(ResQ.Blockchain.BlockchainEvent,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.MockNeoClient\.RecordEventAsync\(ResQ\.Blockchain\.BlockchainEvent, System\.Threading\.CancellationToken\)') if the payload
contains an "incident" field\. This method retrieves all events that were indexed
under the specified incident ID\.
