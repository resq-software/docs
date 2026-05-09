---
sidebarTitle: 'RpcUrl'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[NeoClientOptions](./ResQ.Blockchain.NeoClientOptions.md 'ResQ\.Blockchain\.NeoClientOptions')

## NeoClientOptions\.RpcUrl Property

Gets or sets the Neo N3 RPC endpoint URL\.

```csharp
public string RpcUrl { get; set; }
```

#### Property Value
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The RPC endpoint URL\. Default is `"http://localhost:10332"`\.

### Example

```csharp
options.RpcUrl = "https://testnet1.neo.coz.io:443";
```

### Remarks
This should point to a Neo N3 RPC node\. For testnet, use a public endpoint like
`"https://testnet1.neo.coz.io:443"`\. For mainnet, use a reliable node provider\.
