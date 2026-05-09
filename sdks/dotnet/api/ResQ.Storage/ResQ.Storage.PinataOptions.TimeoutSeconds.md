### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataOptions](./ResQ.Storage.PinataOptions.md 'ResQ\.Storage\.PinataOptions')

## PinataOptions\.TimeoutSeconds Property

Gets or sets the HTTP request timeout in seconds\.

```csharp
public int TimeoutSeconds { get; set; }
```

#### Property Value
[System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')  
Timeout duration in seconds\. Default is 60 seconds\.

### Example

```csharp
// Increase timeout for large uploads on slow connections
options.TimeoutSeconds = 120;

// Decrease for faster failure in responsive environments
options.TimeoutSeconds = 30;
```

### Remarks
This controls how long the HTTP client will wait for API responses\.
Increase this for slow networks or large file uploads\. Decrease for
faster failure detection in high\-availability scenarios\.
