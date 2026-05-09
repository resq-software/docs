### [ResQ\.Storage](ResQ.Storage.md 'ResQ\.Storage').[PinataClient](ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')

## PinataClient\.GetAsync\(string, CancellationToken\) Method

Retrieves file content by its IPFS CID\.

```csharp
public System.Threading.Tasks.Task<System.IO.Stream> GetAsync(string cid, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Storage.PinataClient.GetAsync(string,System.Threading.CancellationToken).cid'></a>

`cid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The IPFS Content Identifier of the file to retrieve\.

<a name='ResQ.Storage.PinataClient.GetAsync(string,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [GetAsync\(string, CancellationToken\)](ResQ.Storage.IStorageClient.GetAsync(string,System.Threading.CancellationToken).md 'ResQ\.Storage\.IStorageClient\.GetAsync\(string, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.IO\.Stream](https://learn.microsoft.com/en-us/dotnet/api/system.io.stream 'System\.IO\.Stream')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
A stream containing the file content\.

#### Exceptions

[System\.ArgumentNullException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentnullexception 'System\.ArgumentNullException')  
Thrown when cid is null or empty\.

[System\.InvalidOperationException](https://learn.microsoft.com/en-us/dotnet/api/system.invalidoperationexception 'System\.InvalidOperationException')  
Thrown when the file cannot be retrieved\.

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
using var stream = await storage.GetAsync("Qmabc123...");
using var fileStream = File.Create("downloaded.jpg");
await stream.CopyToAsync(fileStream);
```

### Remarks
The content is retrieved through the configured IPFS gateway\. The caller is responsible
for disposing the returned stream\. In mock mode, returns a mock stream\.
