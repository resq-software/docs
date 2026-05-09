---
sidebarTitle: 'GetEventsByIncidentAsync(string, CancellationToken)'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[INeoClient](./ResQ.Blockchain.INeoClient.md 'ResQ\.Blockchain\.INeoClient')

## INeoClient\.GetEventsByIncidentAsync\(string, CancellationToken\) Method

Retrieves all blockchain events associated with a specific incident\.

```csharp
System.Threading.Tasks.Task<System.Collections.Generic.IReadOnlyList<ResQ.Blockchain.BlockchainEvent>> GetEventsByIncidentAsync(string incidentId, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.INeoClient.GetEventsByIncidentAsync(string,System.Threading.CancellationToken).incidentId'></a>

`incidentId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The unique identifier of the incident\.

<a name='ResQ.Blockchain.INeoClient.GetEventsByIncidentAsync(string,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Collections\.Generic\.IReadOnlyList&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1 'System\.Collections\.Generic\.IReadOnlyList\`1')[BlockchainEvent](./ResQ.Blockchain.BlockchainEvent.md 'ResQ\.Blockchain\.BlockchainEvent')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1 'System\.Collections\.Generic\.IReadOnlyList\`1')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
A read\-only list of [BlockchainEvent](./ResQ.Blockchain.BlockchainEvent.md 'ResQ\.Blockchain\.BlockchainEvent') records associated with the incident\.
Returns an empty list if no events are found\.

#### Exceptions

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
var events = await neoClient.GetEventsByIncidentAsync("inc-001");
foreach (var evt in events)
{
    Console.WriteLine($"{evt.Timestamp}: {evt.EventType}");
}
```

### Remarks
This method queries the blockchain for all events that reference the specified incident\.
Events are returned in chronological order based on their block height\.
