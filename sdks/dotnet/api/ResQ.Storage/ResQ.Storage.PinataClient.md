### [ResQ\.Storage](ResQ.Storage.md 'ResQ\.Storage')

## PinataClient Class

Pinata IPFS client implementation of [IStorageClient](ResQ.Storage.IStorageClient.md 'ResQ\.Storage\.IStorageClient')\.

```csharp
public class PinataClient : ResQ.Storage.IStorageClient
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; PinataClient

Implements [IStorageClient](ResQ.Storage.IStorageClient.md 'ResQ\.Storage\.IStorageClient')

### Example

```csharp
// Dependency injection registration
services.AddHttpClient<IStorageClient, PinataClient>();
services.Configure<PinataOptions>(options =>
{
    options.JwtToken = Environment.GetEnvironmentVariable("PINATA_JWT");
    options.MockMode = false;
});

// Usage
public class EvidenceService
{
    private readonly IStorageClient _storage;

    public EvidenceService(IStorageClient storage)
    {
        _storage = storage;
    }

    public async Task<string> UploadEvidenceAsync(byte[] imageData)
    {
        var result = await _storage.UploadAsync(imageData, "evidence.jpg", "image/jpeg");
        return result.Cid;
    }
}
```

### Remarks
This client provides integration with the Pinata IPFS pinning service, allowing
files to be uploaded to IPFS and pinned for guaranteed availability\. The client
supports both JWT token and API key/secret authentication methods\.


When [MockMode](ResQ.Storage.PinataOptions.MockMode.md 'ResQ\.Storage\.PinataOptions\.MockMode') is enabled, the client generates fake CIDs
using SHA256 hashes of the content without making actual API calls. This is useful
for testing and development without consuming Pinata credits.

The client is designed to be used with dependency injection and requires an
[System\.Net\.Http\.HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient 'System\.Net\.Http\.HttpClient') configured with appropriate base address and authentication headers.

| Constructors | |
| :--- | :--- |
| [PinataClient\(HttpClient, IOptions&lt;PinataOptions&gt;, ILogger&lt;PinataClient&gt;\)](ResQ.Storage.PinataClient.PinataClient(System.Net.Http.HttpClient,Microsoft.Extensions.Options.IOptions_ResQ.Storage.PinataOptions_,Microsoft.Extensions.Logging.ILogger_ResQ.Storage.PinataClient_).md 'ResQ\.Storage\.PinataClient\.PinataClient\(System\.Net\.Http\.HttpClient, Microsoft\.Extensions\.Options\.IOptions\<ResQ\.Storage\.PinataOptions\>, Microsoft\.Extensions\.Logging\.ILogger\<ResQ\.Storage\.PinataClient\>\)') | Initializes a new instance of the [PinataClient](ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient') class\. |

| Methods | |
| :--- | :--- |
| [BuildResiliencePipeline\(\)](ResQ.Storage.PinataClient.BuildResiliencePipeline().md 'ResQ\.Storage\.PinataClient\.BuildResiliencePipeline\(\)') | Builds the resilience pipeline with circuit breaker and timeout policies\. |
| [ConfigureHttpClient\(\)](ResQ.Storage.PinataClient.ConfigureHttpClient().md 'ResQ\.Storage\.PinataClient\.ConfigureHttpClient\(\)') | Configures the HTTP client with base address, timeout, and authentication\. |
| [GetAsync\(string, CancellationToken\)](ResQ.Storage.PinataClient.GetAsync(string,System.Threading.CancellationToken).md 'ResQ\.Storage\.PinataClient\.GetAsync\(string, System\.Threading\.CancellationToken\)') | Retrieves file content by its IPFS CID\. |
| [GetGatewayUrl\(string\)](ResQ.Storage.PinataClient.GetGatewayUrl(string).md 'ResQ\.Storage\.PinataClient\.GetGatewayUrl\(string\)') | Gets the gateway URL for accessing content by CID\. |
| [IsPinnedAsync\(string, CancellationToken\)](ResQ.Storage.PinataClient.IsPinnedAsync(string,System.Threading.CancellationToken).md 'ResQ\.Storage\.PinataClient\.IsPinnedAsync\(string, System\.Threading\.CancellationToken\)') | Checks if a CID is currently pinned\. |
| [ListPinsAsync\(string, int, CancellationToken\)](ResQ.Storage.PinataClient.ListPinsAsync(string,int,System.Threading.CancellationToken).md 'ResQ\.Storage\.PinataClient\.ListPinsAsync\(string, int, System\.Threading\.CancellationToken\)') | Lists pinned files with optional name prefix filtering\. |
| [MockUploadAsync\(Stream, string, string, Dictionary&lt;string,string&gt;\)](ResQ.Storage.PinataClient.MockUploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_).md 'ResQ\.Storage\.PinataClient\.MockUploadAsync\(System\.IO\.Stream, string, string, System\.Collections\.Generic\.Dictionary\<string,string\>\)') | Generates a mock upload result with a fake CID for testing purposes\. |
| [UnpinAsync\(string, CancellationToken\)](ResQ.Storage.PinataClient.UnpinAsync(string,System.Threading.CancellationToken).md 'ResQ\.Storage\.PinataClient\.UnpinAsync\(string, System\.Threading\.CancellationToken\)') | Unpins a file from Pinata\. |
| [UploadAsync\(byte\[\], string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.PinataClient.UploadAsync.md#ResQ.Storage.PinataClient.UploadAsync(byte[],string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.PinataClient\.UploadAsync\(byte\[\], string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)') | Uploads binary data to IPFS and pins it\. |
| [UploadAsync\(Stream, string, string, Dictionary&lt;string,string&gt;, CancellationToken\)](./ResQ.Storage.PinataClient.UploadAsync.md#ResQ.Storage.PinataClient.UploadAsync(System.IO.Stream,string,string,System.Collections.Generic.Dictionary_string,string_,System.Threading.CancellationToken) 'ResQ\.Storage\.PinataClient\.UploadAsync\(System\.IO\.Stream, string, string, System\.Collections\.Generic\.Dictionary\<string,string\>, System\.Threading\.CancellationToken\)') | Uploads a file stream to IPFS and pins it\. |
