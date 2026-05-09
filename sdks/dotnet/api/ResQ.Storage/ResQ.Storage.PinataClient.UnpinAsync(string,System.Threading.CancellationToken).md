### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataClient](./ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')

## PinataClient\.UnpinAsync\(string, CancellationToken\) Method

Unpins a file from Pinata\.

```csharp
public System.Threading.Tasks.Task<bool> UnpinAsync(string cid, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Storage.PinataClient.UnpinAsync(string,System.Threading.CancellationToken).cid'></a>

`cid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The IPFS Content Identifier to unpin\.

<a name='ResQ.Storage.PinataClient.UnpinAsync(string,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [UnpinAsync\(string, CancellationToken\)](./ResQ.Storage.IStorageClient.UnpinAsync(string,System.Threading.CancellationToken).md 'ResQ\.Storage\.IStorageClient\.UnpinAsync\(string, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
True if the file was successfully unpinned; false otherwise\.

#### Exceptions

[System\.ArgumentNullException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentnullexception 'System\.ArgumentNullException')  
Thrown when cid is null or empty\.

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
bool success = await storage.UnpinAsync("Qmabc123...");
if (success)
{
    Console.WriteLine("File unpinned successfully");
}
```

### Remarks
Unpinning removes the file from your Pinata account but does not remove it from
the IPFS network\. The content may still be available if other nodes have pinned it
or if it has been cached\. Use this to manage storage costs by removing unneeded pins\.
