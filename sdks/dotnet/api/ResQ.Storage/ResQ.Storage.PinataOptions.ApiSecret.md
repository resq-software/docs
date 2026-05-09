### [ResQ\.Storage](ResQ.Storage.md 'ResQ\.Storage').[PinataOptions](ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')

## PinataOptions\.ApiSecret Property

Gets or sets the Pinata API secret for authentication\.

```csharp
public string? ApiSecret { get; set; }
```

#### Property Value
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The API secret string, or null if not using API key authentication\.

### Example

```csharp
options.ApiKey = Environment.GetEnvironmentVariable("PINATA_API_KEY");
options.ApiSecret = Environment.GetEnvironmentVariable("PINATA_API_SECRET");
```

### Remarks
The API secret must be paired with [ApiKey](ResQ.Storage.PinataOptions.ApiKey.md 'ResQ\.Storage\.PinataOptions\.ApiKey') for authentication\.
This is used as an alternative to JWT tokens\. JWT authentication is preferred\.


Store this value securely and never commit it to source control.
