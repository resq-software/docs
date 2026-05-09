### [ResQ\.Storage](ResQ.Storage.md 'ResQ\.Storage')

## IStorageClient Interface

Interface for IPFS storage operations via Pinata\.

```csharp
public interface IStorageClient
```

Derived  
&#8627; [PinataClient](ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')

### Example

```csharp
// Dependency injection registration
services.AddHttpClient<IStorageClient, PinataClient>();

// Usage
public class EvidenceService
{
    private readonly IStorageClient _storage;
    
    public EvidenceService(IStorageClient storage)
    {
        _storage = storage;
    }
    
    public async Task<string> StoreEvidenceAsync(byte[] imageData)
    {
        var result = await _storage.UploadAsync(
            imageData,
            "evidence.jpg",
            "image/jpeg",
            new Dictionary<string, string>
            {
                ["incidentId"] = "inc-001",
                ["droneId"] = "drn-001"
            });
        return result.Cid;
    }
}
```

### Remarks
This interface defines the contract for storing and retrieving files on IPFS
through the Pinata pinning service\. Implementations handle the HTTP communication
with Pinata's API, authentication, and error handling\.


Files uploaded through this interface are automatically pinned to ensure they
remain available on the IPFS network. The CID returned can be used to retrieve
the file from any IPFS gateway.

| Methods | |
| :--- | :--- |
| [GetAsync\(string, CancellationToken\)](ResQ.Storage.IStorageClient.GetAsync(string,System.Threading.CancellationToken).md 'ResQ\.Storage\.IStorageClient\.GetAsync\(string, System\.Threading\.CancellationToken\)') | Retrieves file content by its IPFS CID\. |
| [GetGatewayUrl\(string\)](ResQ.Storage.IStorageClient.GetGatewayUrl(string).md 'ResQ\.Storage\.IStorageClient\.GetGatewayUrl\(string\)') | Gets the gateway URL for accessing content by CID\. |
| [IsPinnedAsync\(string, CancellationToken\)](ResQ.Storage.IStorageClient.IsPinnedAsync(string,System.Threading.CancellationToken).md 'ResQ\.Storage\.IStorageClient\.IsPinnedAsync\(string, System\.Threading\.CancellationToken\)') | Checks if a CID is currently pinned\. |
| [ListPinsAsync\(string, int, CancellationToken\)](ResQ.Storage.IStorageClient.ListPinsAsync(string,int,System.Threading.CancellationToken).md 'ResQ\.Storage\.IStorageClient\.ListPinsAsync\(string, int, System\.Threading\.CancellationToken\)') | Lists pinned files with optional name prefix filtering\. |
| [UnpinAsync\(string, CancellationToken\)](ResQ.Storage.IStorageClient.UnpinAsync(string,System.Threading.CancellationToken).md 'ResQ\.Storage\.IStorageClient\.UnpinAsync\(string, System\.Threading\.CancellationToken\)') | Unpins a file from Pinata\. |
| [UploadAsync\(byte\[\], string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.IStorageClient.UploadAsync.md#ResQ.Storage.IStorageClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.IStorageClient\.UploadAsync\(byte\[\], string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)') | Uploads binary data to IPFS and pins it\. |
| [UploadAsync\(Stream, string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.IStorageClient.UploadAsync.md#ResQ.Storage.IStorageClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.IStorageClient\.UploadAsync\(System\.IO\.Stream, string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)') | Uploads a file stream to IPFS and pins it\. |
