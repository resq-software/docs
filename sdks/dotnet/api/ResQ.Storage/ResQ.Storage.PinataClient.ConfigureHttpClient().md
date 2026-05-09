### [ResQ\.Storage](ResQ.Storage.md 'ResQ\.Storage').[PinataClient](ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')

## PinataClient\.ConfigureHttpClient\(\) Method

Configures the HTTP client with base address, timeout, and authentication\.

```csharp
private void ConfigureHttpClient();
```

### Remarks
This method sets up the HTTP client with:
- Base address from [ApiUrl](ResQ.Storage.PinataOptions.ApiUrl.md 'ResQ\.Storage\.PinataOptions\.ApiUrl')
- Timeout from [TimeoutSeconds](ResQ.Storage.PinataOptions.TimeoutSeconds.md 'ResQ\.Storage\.PinataOptions\.TimeoutSeconds')
- JWT Bearer authentication if JWT token is provided
- API key/secret headers if no JWT token is provided
