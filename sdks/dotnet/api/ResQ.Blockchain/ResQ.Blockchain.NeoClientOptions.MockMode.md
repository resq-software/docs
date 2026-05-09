---
sidebarTitle: 'MockMode'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[NeoClientOptions](./ResQ.Blockchain.NeoClientOptions.md 'ResQ\.Blockchain\.NeoClientOptions')

## NeoClientOptions\.MockMode Property

Gets or sets a value indicating whether to use mock mode for testing\.

```csharp
public bool MockMode { get; set; }
```

#### Property Value
[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')  
True to use mock implementation; false to use real blockchain\. Default is false\.

### Example

```csharp
// Development/testing
options.MockMode = true;

// Production
options.MockMode = false;
```

### Remarks
When enabled, the client will use [MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient') instead of making real
blockchain calls\. This is useful for development and testing without requiring a live
blockchain connection\. Set to false for production deployments\.
