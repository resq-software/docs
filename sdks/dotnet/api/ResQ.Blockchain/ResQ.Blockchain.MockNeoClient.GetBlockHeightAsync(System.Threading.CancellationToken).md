### [ResQ\.Blockchain](ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\.GetBlockHeightAsync\(CancellationToken\) Method

Gets the current mock block height\.

```csharp
public System.Threading.Tasks.Task<ulong> GetBlockHeightAsync(System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.MockNeoClient.GetBlockHeightAsync(System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [GetBlockHeightAsync\(CancellationToken\)](ResQ.Blockchain.INeoClient.GetBlockHeightAsync(System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.GetBlockHeightAsync\(System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.UInt64](https://learn.microsoft.com/en-us/dotnet/api/system.uint64 'System\.UInt64')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
The current block height, starting at 1,000,000 and incrementing with each transaction\.

### Example

```csharp
var initialHeight = await mockClient.GetBlockHeightAsync();
// Returns: 1000000

await mockClient.RecordEventAsync(evt);

var newHeight = await mockClient.GetBlockHeightAsync();
// Returns: 1000001
```

### Remarks
The block height starts at 1,000,000 and increases by 1 for each recorded transaction\.
This simulates blockchain growth without requiring an actual network connection\.
