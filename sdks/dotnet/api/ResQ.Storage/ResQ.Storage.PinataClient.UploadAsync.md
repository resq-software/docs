---
sidebarTitle: 'UploadAsync'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataClient](./ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')

## PinataClient\.UploadAsync Method

| Overloads | |
| :--- | :--- |
| [UploadAsync\(byte\[\], string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.PinataClient.UploadAsync.md#ResQ.Storage.PinataClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.PinataClient\.UploadAsync\(byte\[\], string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)') | Uploads binary data to IPFS and pins it\. |
| [UploadAsync\(Stream, string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.PinataClient.UploadAsync.md#ResQ.Storage.PinataClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.PinataClient\.UploadAsync\(System\.IO\.Stream, string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)') | Uploads a file stream to IPFS and pins it\. |

<a name='ResQ.Storage.PinataClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken)'></a>

## PinataClient\.UploadAsync\(byte\[\], string, string, Dictionary\<string,string\>, CancellationToken\) Method

Uploads binary data to IPFS and pins it\.

```csharp
public System.Threading.Tasks.Task<ResQ.Storage.UploadResult> UploadAsync(byte[] data, string fileName, string contentType, System.Collections.Generic.Dictionary<string,string>? metadata=null, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Storage.PinataClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).data'></a>

`data` [System\.Byte](https://learn.microsoft.com/en-us/dotnet/api/system.byte 'System\.Byte')[\[\]](https://learn.microsoft.com/en-us/dotnet/api/system.array 'System\.Array')

The file content as a byte array\.

<a name='ResQ.Storage.PinataClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).fileName'></a>

`fileName` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The desired filename for the uploaded content\.

<a name='ResQ.Storage.PinataClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).contentType'></a>

`contentType` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The MIME type of the content\.

<a name='ResQ.Storage.PinataClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).metadata'></a>

`metadata` [System\.Collections\.Generic\.Dictionary&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')[,](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')

Optional dictionary of custom metadata key\-value pairs\.

<a name='ResQ.Storage.PinataClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [UploadAsync\(byte\[\], string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.IStorageClient.UploadAsync.md#ResQ.Storage.IStorageClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.IStorageClient\.UploadAsync\(byte\[\], string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[UploadResult](./ResQ.Storage.UploadResult.md 'ResQ\.Storage\.UploadResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
An [UploadResult](./ResQ.Storage.UploadResult.md 'ResQ\.Storage\.UploadResult') containing the CID and upload metadata\.

#### Exceptions

[System\.ArgumentNullException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentnullexception 'System\.ArgumentNullException')  
Thrown when data, fileName, or contentType is null\.

[System\.InvalidOperationException](https://learn.microsoft.com/en-us/dotnet/api/system.invalidoperationexception 'System\.InvalidOperationException')  
Thrown when the upload fails\.

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
byte[] imageBytes = await File.ReadAllBytesAsync("photo.jpg");
var result = await storage.UploadAsync(
    imageBytes,
    "photo.jpg",
    "image/jpeg");
```

### Remarks
This is a convenience overload that wraps the byte array in a MemoryStream
and calls [UploadAsync\(Stream, string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.IStorageClient.UploadAsync.md#ResQ.Storage.IStorageClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.IStorageClient\.UploadAsync\(System\.IO\.Stream, string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)')\.

<a name='ResQ.Storage.PinataClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken)'></a>

## PinataClient\.UploadAsync\(Stream, string, string, Dictionary\<string,string\>, CancellationToken\) Method

Uploads a file stream to IPFS and pins it\.

```csharp
public System.Threading.Tasks.Task<ResQ.Storage.UploadResult> UploadAsync(System.IO.Stream content, string fileName, string contentType, System.Collections.Generic.Dictionary<string,string>? metadata=null, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Storage.PinataClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).content'></a>

`content` [System\.IO\.Stream](https://learn.microsoft.com/en-us/dotnet/api/system.io.stream 'System\.IO\.Stream')

The file content as a stream\. The stream will be read to completion\.

<a name='ResQ.Storage.PinataClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).fileName'></a>

`fileName` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The desired filename for the uploaded content\.

<a name='ResQ.Storage.PinataClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).contentType'></a>

`contentType` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The MIME type of the content \(e\.g\., "image/jpeg", "application/pdf"\)\.

<a name='ResQ.Storage.PinataClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).metadata'></a>

`metadata` [System\.Collections\.Generic\.Dictionary&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')[,](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')

Optional dictionary of custom metadata key\-value pairs to attach to the pin\.

<a name='ResQ.Storage.PinataClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [UploadAsync\(Stream, string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.IStorageClient.UploadAsync.md#ResQ.Storage.IStorageClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.IStorageClient\.UploadAsync\(System\.IO\.Stream, string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[UploadResult](./ResQ.Storage.UploadResult.md 'ResQ\.Storage\.UploadResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
An [UploadResult](./ResQ.Storage.UploadResult.md 'ResQ\.Storage\.UploadResult') containing the CID and upload metadata\.

#### Exceptions

[System\.ArgumentNullException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentnullexception 'System\.ArgumentNullException')  
Thrown when content, fileName, or contentType is null\.

[System\.InvalidOperationException](https://learn.microsoft.com/en-us/dotnet/api/system.invalidoperationexception 'System\.InvalidOperationException')  
Thrown when the upload fails\.

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
using var stream = File.OpenRead("photo.jpg");
var result = await storage.UploadAsync(
    stream,
    "photo.jpg",
    "image/jpeg",
    new Dictionary<string, string> { ["source"] = "drone-001" });
Console.WriteLine($"Uploaded: {result.Cid}");
```

### Remarks
The stream will be read and the content uploaded to IPFS via Pinata\.
Once uploaded, the content is automatically pinned to ensure persistence\.
The returned CID can be used to retrieve the content from any IPFS gateway\.
