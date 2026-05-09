---
sidebarTitle: 'JwtToken'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataOptions](./ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')

## PinataOptions\.JwtToken Property

Gets or sets the Pinata JWT token for authentication\.

```csharp
public string? JwtToken { get; set; }
```

#### Property Value
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The JWT token string, or null if not using JWT authentication\.

### Example

```csharp
options.JwtToken = Environment.GetEnvironmentVariable("PINATA_JWT");
```

### Remarks
JWT authentication is the preferred method and provides full API access\.
Generate a JWT token from your Pinata account dashboard\. When provided,
this takes precedence over API key/secret authentication\.


Store this value securely (e.g., in environment variables) and never commit
it to source control.
