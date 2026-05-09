### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[INeoClient](./ResQ.Blockchain.INeoClient.md 'ResQ\.Blockchain\.INeoClient')

## INeoClient\.GetBlockHeightAsync\(CancellationToken\) Method

Gets the current block height of the blockchain\.

```csharp
System.Threading.Tasks.Task<ulong> GetBlockHeightAsync(System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.INeoClient.GetBlockHeightAsync(System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.UInt64](https://learn.microsoft.com/en-us/dotnet/api/system.uint64 'System\.UInt64')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
The current block height as an unsigned 64\-bit integer\.

#### Exceptions

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
var height = await neoClient.GetBlockHeightAsync();
Console.WriteLine($"Current block: {height}");

// Check if a transaction is confirmed (6+ blocks past its inclusion).
// Use addition rather than subtraction: both operands are ulong, so
// `height - txBlockHeight` underflows to ~ulong.MaxValue when height
// briefly trails (stale RPC, reorgs) and falsely reports finalized.
ulong txBlockHeight = 12345; // captured from a prior RecordEventAsync
if (height >= txBlockHeight + 6)
{
    Console.WriteLine("Transaction is finalized");
}
```

### Remarks
The block height represents the number of blocks in the blockchain and increases
approximately every 15 seconds on Neo N3\. This can be used to estimate confirmation
times and determine if transactions have been finalized\.
