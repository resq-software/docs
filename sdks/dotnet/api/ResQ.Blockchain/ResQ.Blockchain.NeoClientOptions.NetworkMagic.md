### [ResQ\.Blockchain](ResQ.Blockchain.md 'ResQ\.Blockchain').[NeoClientOptions](ResQ.Blockchain.NeoClientOptions.md 'ResQ\.Blockchain\.NeoClientOptions')

## NeoClientOptions\.NetworkMagic Property

Gets or sets the network magic number for identifying the Neo network\.

```csharp
public uint NetworkMagic { get; set; }
```

#### Property Value
[System\.UInt32](https://learn.microsoft.com/en-us/dotnet/api/system.uint32 'System\.UInt32')  
The network magic number\. Default is 894710606 \(TestNet\)\.

### Example

```csharp
// MainNet
options.NetworkMagic = 860833102;

// TestNet (default)
options.NetworkMagic = 894710606;
```

### Remarks
The network magic is used to identify which Neo network to connect to:
- MainNet: 860833102
- TestNet: 894710606
- PrivateNet: Custom value
