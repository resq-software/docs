---
sidebarTitle: 'PinataClient(HttpClient, PinataOptions_, PinataClient_)'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataClient](./ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')

## PinataClient\(HttpClient, IOptions\<PinataOptions\>, ILogger\<PinataClient\>\) Constructor

Initializes a new instance of the [PinataClient](./ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient') class\.

```csharp
public PinataClient(System.Net.Http.HttpClient httpClient, Microsoft.Extensions.Options.IOptions<ResQ.Storage.PinataOptions> options, Microsoft.Extensions.Logging.ILogger<ResQ.Storage.PinataClient> logger);
```
#### Parameters

<a name='ResQ.Storage.PinataClient.PinataClient(System.Net.Http.HttpClient,Microsoft.Extensions.Options.IOptions_ResQ.Storage.PinataOptions_,Microsoft.Extensions.Logging.ILogger_ResQ.Storage.PinataClient_).httpClient'></a>

`httpClient` [System\.Net\.Http\.HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient 'System\.Net\.Http\.HttpClient')

The HTTP client instance for making API requests\.

<a name='ResQ.Storage.PinataClient.PinataClient(System.Net.Http.HttpClient,Microsoft.Extensions.Options.IOptions_ResQ.Storage.PinataOptions_,Microsoft.Extensions.Logging.ILogger_ResQ.Storage.PinataClient_).options'></a>

`options` [Microsoft\.Extensions\.Options\.IOptions&lt;](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.ioptions-1 'Microsoft\.Extensions\.Options\.IOptions\`1')[PinataOptions](./ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.ioptions-1 'Microsoft\.Extensions\.Options\.IOptions\`1')

The Pinata configuration options\.

<a name='ResQ.Storage.PinataClient.PinataClient(System.Net.Http.HttpClient,Microsoft.Extensions.Options.IOptions_ResQ.Storage.PinataOptions_,Microsoft.Extensions.Logging.ILogger_ResQ.Storage.PinataClient_).logger'></a>

`logger` [Microsoft\.Extensions\.Logging\.ILogger&lt;](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1 'Microsoft\.Extensions\.Logging\.ILogger\`1')[PinataClient](./ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1 'Microsoft\.Extensions\.Logging\.ILogger\`1')

The logger instance for recording operations\.

### Example

```csharp
var httpClient = new HttpClient();
var options = Options.Create(new PinataOptions
{
    JwtToken = "your-jwt-token",
    ApiUrl = "https://api.pinata.cloud"
});
var logger = loggerFactory.CreateLogger<PinataClient>();

var client = new PinataClient(httpClient, options, logger);
```

### Remarks
The constructor configures the HTTP client with the base address, timeout,
and authentication headers based on the provided options\. JWT authentication
is preferred over API key/secret when both are provided\.
