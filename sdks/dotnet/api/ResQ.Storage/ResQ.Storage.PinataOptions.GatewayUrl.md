---
sidebarTitle: 'GatewayUrl'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataOptions](./ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')

## PinataOptions\.GatewayUrl Property

Gets or sets the IPFS gateway URL for retrieving content\.

```csharp
public string GatewayUrl { get; set; }
```

#### Property Value
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The gateway base URL\. Default is `https://gateway.pinata.cloud/ipfs`.

### Example

```csharp
// Use Pinata's dedicated gateway (requires paid plan)
options.GatewayUrl = "https://your-gateway.mypinata.cloud/ipfs";

// Use public IPFS gateway
options.GatewayUrl = "https://ipfs.io/ipfs";
```

### Remarks
This URL is used to construct public gateway URLs for uploaded content\.
The default uses Pinata's public gateway\. For production use with high traffic,
consider using a dedicated gateway or your own IPFS node\.
