### [ResQ\.Storage](ResQ.Storage.md 'ResQ\.Storage')

## PinataOptions Class

Configuration options for the Pinata IPFS client\.

```csharp
public class PinataOptions
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; PinataOptions

### Example

```csharp
// Configuration in appsettings.json
{
  "PinataOptions": {
    "ApiUrl": "https://api.pinata.cloud",
    "GatewayUrl": "https://gateway.pinata.cloud/ipfs",
    "JwtToken": "${PINATA_JWT}",
    "MockMode": false,
    "MaxFileSizeBytes": 104857600,
    "TimeoutSeconds": 60
  }
}

// Registration with dependency injection
services.Configure<PinataOptions>(configuration.GetSection("PinataOptions"));

// Or configure in code
services.Configure<PinataOptions>(options =>
{
    options.JwtToken = Environment.GetEnvironmentVariable("PINATA_JWT");
    options.MockMode = false;
});
```

### Remarks
This class provides configuration settings for the Pinata IPFS pinning service,
including API endpoints, authentication credentials, and operational parameters\.


Authentication can be configured using either a JWT token (preferred) or API key/secret pair.
If both are provided, the JWT token takes precedence. For development and testing,
set [MockMode](ResQ.Storage.PinataOptions.MockMode.md 'ResQ\.Storage\.PinataOptions\.MockMode') to true to avoid making actual API calls.

Configuration can be loaded from appsettings.json, environment variables, or code.
Sensitive values like JWT tokens and API secrets should be stored securely
(e.g., in environment variables or secret managers) and not committed to source control.

| Properties | |
| :--- | :--- |
| [ApiKey](ResQ.Storage.PinataOptions.ApiKey.md 'ResQ\.Storage\.PinataOptions\.ApiKey') | Gets or sets the Pinata API key for authentication\. |
| [ApiSecret](ResQ.Storage.PinataOptions.ApiSecret.md 'ResQ\.Storage\.PinataOptions\.ApiSecret') | Gets or sets the Pinata API secret for authentication\. |
| [ApiUrl](ResQ.Storage.PinataOptions.ApiUrl.md 'ResQ\.Storage\.PinataOptions\.ApiUrl') | Gets or sets the Pinata API endpoint URL\. |
| [GatewayUrl](ResQ.Storage.PinataOptions.GatewayUrl.md 'ResQ\.Storage\.PinataOptions\.GatewayUrl') | Gets or sets the IPFS gateway URL for retrieving content\. |
| [JwtToken](ResQ.Storage.PinataOptions.JwtToken.md 'ResQ\.Storage\.PinataOptions\.JwtToken') | Gets or sets the Pinata JWT token for authentication\. |
| [MaxFileSizeBytes](ResQ.Storage.PinataOptions.MaxFileSizeBytes.md 'ResQ\.Storage\.PinataOptions\.MaxFileSizeBytes') | Gets or sets the maximum file size allowed for uploads\. |
| [MockMode](ResQ.Storage.PinataOptions.MockMode.md 'ResQ\.Storage\.PinataOptions\.MockMode') | Gets or sets a value indicating whether to use mock mode for testing\. |
| [TimeoutSeconds](ResQ.Storage.PinataOptions.TimeoutSeconds.md 'ResQ\.Storage\.PinataOptions\.TimeoutSeconds') | Gets or sets the HTTP request timeout in seconds\. |
