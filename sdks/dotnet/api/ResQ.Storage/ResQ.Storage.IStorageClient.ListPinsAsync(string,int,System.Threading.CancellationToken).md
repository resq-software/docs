### [ResQ\.Storage](ResQ.Storage.md 'ResQ\.Storage').[IStorageClient](ResQ.Storage.IStorageClient.md 'ResQ\.Storage\.IStorageClient')

## IStorageClient\.ListPinsAsync\(string, int, CancellationToken\) Method

Lists pinned files with optional name prefix filtering\.

```csharp
System.Threading.Tasks.Task<System.Collections.Generic.IReadOnlyList<ResQ.Storage.PinMetadata>> ListPinsAsync(string? namePrefix=null, int limit=100, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Storage.IStorageClient.ListPinsAsync(string,int,System.Threading.CancellationToken).namePrefix'></a>

`namePrefix` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Optional prefix to filter pins by name\. If null or empty, returns all pins\.

<a name='ResQ.Storage.IStorageClient.ListPinsAsync(string,int,System.Threading.CancellationToken).limit'></a>

`limit` [System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')

Maximum number of results to return \(default 100\)\.

<a name='ResQ.Storage.IStorageClient.ListPinsAsync(string,int,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Collections\.Generic\.IReadOnlyList&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1 'System\.Collections\.Generic\.IReadOnlyList\`1')[PinMetadata](ResQ.Storage.PinMetadata.md 'ResQ\.Storage\.PinMetadata')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1 'System\.Collections\.Generic\.IReadOnlyList\`1')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
A read\-only list of pin metadata matching the filter criteria\.

#### Exceptions

[System\.ArgumentOutOfRangeException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentoutofrangeexception 'System\.ArgumentOutOfRangeException')  
Thrown when limit is less than 1\.

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
// List all pins
var allPins = await storage.ListPinsAsync();

// List pins with specific prefix
var evidencePins = await storage.ListPinsAsync("evidence-", limit: 50);
foreach (var pin in evidencePins)
{
    Console.WriteLine($"{pin.Name}: {pin.Cid}");
}
```

### Remarks
This method queries the Pinata API for pinned content\. Results include metadata
about each pin including CID, name, size, and custom key\-value pairs\.
