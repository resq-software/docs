---
sidebarTitle: 'NeoConfig'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## NeoConfig Class

Configuration for Neo N3 blockchain connection\.

```csharp
public record NeoConfig : System.IEquatable<ResQ.Core.NeoConfig>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; NeoConfig

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[NeoConfig](./ResQ.Core.NeoConfig.md 'ResQ\.Core\.NeoConfig')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var config = new NeoConfig
{
    RpcUrl = "https://testnet1.neo.coz.io:443",
    ContractHash = "0x8d35a57f8c01156527c92ebbb4d772fa9574cbf4",
    NetworkMagic = 894710606,
    MockMode = false
};
```

### Remarks
Provides settings for connecting to the Neo N3 blockchain including
RPC endpoint, contract address, and network identification\.

| Properties | |
| :--- | :--- |
| [ContractHash](./ResQ.Core.NeoConfig.ContractHash.md 'ResQ\.Core\.NeoConfig\.ContractHash') | Smart contract script hash\. |
| [MockMode](./ResQ.Core.NeoConfig.MockMode.md 'ResQ\.Core\.NeoConfig\.MockMode') | Enable mock mode for testing\. |
| [NetworkMagic](./ResQ.Core.NeoConfig.NetworkMagic.md 'ResQ\.Core\.NeoConfig\.NetworkMagic') | Network magic number \(TestNet = 877933390\)\. |
| [RpcUrl](./ResQ.Core.NeoConfig.RpcUrl.md 'ResQ\.Core\.NeoConfig\.RpcUrl') | Neo RPC endpoint URL\. |
| [TimeoutSeconds](./ResQ.Core.NeoConfig.TimeoutSeconds.md 'ResQ\.Core\.NeoConfig\.TimeoutSeconds') | HTTP request timeout in seconds\. Defaults to 30\. |
