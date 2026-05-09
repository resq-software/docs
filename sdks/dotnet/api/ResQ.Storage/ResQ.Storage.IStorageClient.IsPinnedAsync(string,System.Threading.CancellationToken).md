---
sidebarTitle: 'IsPinnedAsync(string, CancellationToken)'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[IStorageClient](./ResQ.Storage.IStorageClient.md 'ResQ\.Storage\.IStorageClient')

## IStorageClient\.IsPinnedAsync\(string, CancellationToken\) Method

Checks if a CID is currently pinned\.

```csharp
System.Threading.Tasks.Task<bool> IsPinnedAsync(string cid, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Storage.IStorageClient.IsPinnedAsync(string,System.Threading.CancellationToken).cid'></a>

`cid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The IPFS Content Identifier to check\.

<a name='ResQ.Storage.IStorageClient.IsPinnedAsync(string,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
True if the CID is pinned; false otherwise\.

#### Exceptions

[System\.ArgumentNullException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentnullexception 'System\.ArgumentNullException')  
Thrown when cid is null or empty\.

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
bool isPinned = await storage.IsPinnedAsync("Qmabc123...");
if (!isPinned)
{
    Console.WriteLine("Warning: Content may not be persisted");
}
```

### Remarks
A pinned CID is guaranteed to remain available on the IPFS network\.
Unpinned content may be garbage collected by IPFS nodes\.
