---
sidebarTitle: 'ApiKey'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataOptions](./ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')

## PinataOptions\.ApiKey Property

Gets or sets the Pinata API key for authentication\.

```csharp
public string? ApiKey { get; set; }
```

#### Property Value
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The API key string, or null if not using API key authentication\.

### Example

```csharp
options.ApiKey = Environment.GetEnvironmentVariable("PINATA_API_KEY");
options.ApiSecret = Environment.GetEnvironmentVariable("PINATA_API_SECRET");
```

### Remarks
API key authentication is an alternative to JWT tokens\. When using API keys,
both [ApiKey](./ResQ.Storage.PinataOptions.ApiKey.md 'ResQ\.Storage\.PinataOptions\.ApiKey') and [ApiSecret](./ResQ.Storage.PinataOptions.ApiSecret.md 'ResQ\.Storage\.PinataOptions\.ApiSecret') must be provided\.
JWT authentication is preferred when available\.


Store this value securely and never commit it to source control.
