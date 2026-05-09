---
sidebarTitle: 'UploadResult(string, string, long, string, bool, DateTimeOffset)'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[UploadResult](./ResQ.Storage.UploadResult.md 'ResQ\.Storage\.UploadResult')

## UploadResult\(string, string, long, string, bool, DateTimeOffset\) Constructor

Represents the result of a file upload operation to IPFS\.

```csharp
public UploadResult(string Cid, string FileName, long SizeBytes, string ContentType, bool IsPinned, System.DateTimeOffset Timestamp);
```
#### Parameters

<a name='ResQ.Storage.UploadResult.UploadResult(string,string,long,string,bool,System.DateTimeOffset).Cid'></a>

`Cid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The IPFS Content Identifier \(CID\) for the uploaded file\.

<a name='ResQ.Storage.UploadResult.UploadResult(string,string,long,string,bool,System.DateTimeOffset).FileName'></a>

`FileName` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The original filename of the uploaded content\.

<a name='ResQ.Storage.UploadResult.UploadResult(string,string,long,string,bool,System.DateTimeOffset).SizeBytes'></a>

`SizeBytes` [System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')

The size of the file in bytes\.

<a name='ResQ.Storage.UploadResult.UploadResult(string,string,long,string,bool,System.DateTimeOffset).ContentType'></a>

`ContentType` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The MIME type of the file \(e\.g\., "image/jpeg", "video/mp4"\)\.

<a name='ResQ.Storage.UploadResult.UploadResult(string,string,long,string,bool,System.DateTimeOffset).IsPinned'></a>

`IsPinned` [System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')

True if the file has been pinned to ensure persistence\.

<a name='ResQ.Storage.UploadResult.UploadResult(string,string,long,string,bool,System.DateTimeOffset).Timestamp'></a>

`Timestamp` [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')

UTC timestamp when the upload completed\.

### Example

```csharp
var result = await storageClient.UploadAsync(stream, "evidence.jpg", "image/jpeg");
Console.WriteLine($"Uploaded to: {result.Cid}");
Console.WriteLine($"Size: {result.SizeBytes} bytes");
Console.WriteLine($"URL: {storageClient.GetGatewayUrl(result.Cid)}");
```

### Remarks
This record contains all relevant information about an uploaded file,
including its Content Identifier \(CID\), metadata, and pin status\.
The CID is the permanent address of the file on the IPFS network\.
