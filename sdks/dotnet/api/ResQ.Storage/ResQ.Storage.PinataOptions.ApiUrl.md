---
sidebarTitle: 'ApiUrl'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataOptions](./ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')

## PinataOptions\.ApiUrl Property

Gets or sets the Pinata API endpoint URL\.

```csharp
public string ApiUrl { get; set; }
```

#### Property Value
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The API base URL\. Default is `https://api.pinata.cloud`.

### Example

```csharp
options.ApiUrl = "https://api.pinata.cloud";
```

### Remarks
This is the base URL for all Pinata API calls\. The default value points to
Pinata's production API\. Change this only if using a custom Pinata deployment
or proxy\.
