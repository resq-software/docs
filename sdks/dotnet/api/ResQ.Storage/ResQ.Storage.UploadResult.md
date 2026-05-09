### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage')

## UploadResult Class

Represents the result of a file upload operation to IPFS\.

```csharp
public record UploadResult : System.IEquatable<ResQ.Storage.UploadResult>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; UploadResult

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[UploadResult](./ResQ.Storage.UploadResult.md 'ResQ\.Storage\.UploadResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

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

| Constructors | |
| :--- | :--- |
| [UploadResult\(string, string, long, string, bool, DateTimeOffset\)](./ResQ.Storage.UploadResult.UploadResult(string,string,long,string,bool,System.DateTimeOffset).md 'ResQ\.Storage\.UploadResult\.UploadResult\(string, string, long, string, bool, System\.DateTimeOffset\)') | Represents the result of a file upload operation to IPFS\. |

| Properties | |
| :--- | :--- |
| [Cid](./ResQ.Storage.UploadResult.Cid.md 'ResQ\.Storage\.UploadResult\.Cid') | The IPFS Content Identifier \(CID\) for the uploaded file\. |
| [ContentType](./ResQ.Storage.UploadResult.ContentType.md 'ResQ\.Storage\.UploadResult\.ContentType') | The MIME type of the file \(e\.g\., "image/jpeg", "video/mp4"\)\. |
| [FileName](./ResQ.Storage.UploadResult.FileName.md 'ResQ\.Storage\.UploadResult\.FileName') | The original filename of the uploaded content\. |
| [IsPinned](./ResQ.Storage.UploadResult.IsPinned.md 'ResQ\.Storage\.UploadResult\.IsPinned') | True if the file has been pinned to ensure persistence\. |
| [SizeBytes](./ResQ.Storage.UploadResult.SizeBytes.md 'ResQ\.Storage\.UploadResult\.SizeBytes') | The size of the file in bytes\. |
| [Timestamp](./ResQ.Storage.UploadResult.Timestamp.md 'ResQ\.Storage\.UploadResult\.Timestamp') | UTC timestamp when the upload completed\. |
