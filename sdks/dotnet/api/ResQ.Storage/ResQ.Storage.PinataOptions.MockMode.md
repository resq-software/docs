---
sidebarTitle: 'MockMode'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataOptions](./ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')

## PinataOptions\.MockMode Property

Gets or sets a value indicating whether to use mock mode for testing\.

```csharp
public bool MockMode { get; set; }
```

#### Property Value
[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')  
True to use mock implementation; false to use real Pinata API\. Default is false\.

### Example

```csharp
// Development/testing
options.MockMode = true;

// Production
options.MockMode = false;
```

### Remarks
When enabled, the client will generate fake CIDs and not make actual API calls\.
This is useful for development and testing without consuming Pinata credits
or requiring network access\. Set to false for production deployments\.


Mock mode generates deterministic CIDs using SHA256 hashes of the content,
allowing for consistent testing scenarios.
