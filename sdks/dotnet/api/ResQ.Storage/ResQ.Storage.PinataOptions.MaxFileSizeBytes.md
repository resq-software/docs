### [ResQ\.Storage](ResQ.Storage.md 'ResQ\.Storage').[PinataOptions](ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')

## PinataOptions\.MaxFileSizeBytes Property

Gets or sets the maximum file size allowed for uploads\.

```csharp
public long MaxFileSizeBytes { get; set; }
```

#### Property Value
[System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')  
Maximum file size in bytes\. Default is 100MB \(104,857,600 bytes\)\.

### Example

```csharp
// Allow files up to 500MB
options.MaxFileSizeBytes = 500 * 1024 * 1024;

// Limit to 10MB for stricter control
options.MaxFileSizeBytes = 10 * 1024 * 1024;
```

### Remarks
Files larger than this limit will be rejected before uploading\.
The default is 100MB which is suitable for most use cases\.
Increase this if you need to upload larger files \(e\.g\., high\-resolution videos\)\.


Note: Pinata's free tier has its own upload limits. Check your Pinata plan
for actual limits regardless of this setting.
