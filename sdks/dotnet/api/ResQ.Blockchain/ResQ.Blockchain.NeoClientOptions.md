---
sidebarTitle: 'NeoClientOptions'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain')

## NeoClientOptions Class

Configuration options for the Neo N3 blockchain client\.

```csharp
public class NeoClientOptions
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → NeoClientOptions

### Example

```csharp
// Configuration in appsettings.json
{
  "NeoClientOptions": {
    "RpcUrl": "https://testnet1.neo.coz.io:443",
    "NetworkMagic": 894710606,
    "ContractHash": "0x8d35a57f8c01156527c92ebbb4d772fa9574cbf4",
    "MockMode": false,
    "ConfirmationTimeoutSeconds": 30,
    "MaxRetryAttempts": 3
  }
}

// Registration with dependency injection
services.Configure<NeoClientOptions>(configuration.GetSection("NeoClientOptions"));

// Usage in a service
public class MyService
{
    private readonly NeoClientOptions _options;
    
    public MyService(IOptions<NeoClientOptions> options)
    {
        _options = options.Value;
    }
}
```

### Remarks
This class provides configuration settings for connecting to the Neo N3 blockchain,
including RPC endpoint, network identification, contract addresses, and operational
parameters such as timeouts and retry logic\.


For development and testing, set [MockMode](./ResQ.Blockchain.NeoClientOptions.MockMode.md 'ResQ\.Blockchain\.NeoClientOptions\.MockMode') to true to use the mock
client implementation. For production, configure the [RpcUrl](./ResQ.Blockchain.NeoClientOptions.RpcUrl.md 'ResQ\.Blockchain\.NeoClientOptions\.RpcUrl') to point
to a reliable Neo N3 RPC endpoint and provide the wallet path for transaction signing.

| Properties | |
| :--- | :--- |
| [ConfirmationTimeoutSeconds](./ResQ.Blockchain.NeoClientOptions.ConfirmationTimeoutSeconds.md 'ResQ\.Blockchain\.NeoClientOptions\.ConfirmationTimeoutSeconds') | Gets or sets the timeout for waiting for transaction confirmation\. |
| [ContractHash](./ResQ.Blockchain.NeoClientOptions.ContractHash.md 'ResQ\.Blockchain\.NeoClientOptions\.ContractHash') | Gets or sets the smart contract script hash for ResQ event recording\. |
| [MaxRetryAttempts](./ResQ.Blockchain.NeoClientOptions.MaxRetryAttempts.md 'ResQ\.Blockchain\.NeoClientOptions\.MaxRetryAttempts') | Gets or sets the maximum number of retry attempts for failed transactions\. |
| [MockMode](./ResQ.Blockchain.NeoClientOptions.MockMode.md 'ResQ\.Blockchain\.NeoClientOptions\.MockMode') | Gets or sets a value indicating whether to use mock mode for testing\. |
| [NetworkMagic](./ResQ.Blockchain.NeoClientOptions.NetworkMagic.md 'ResQ\.Blockchain\.NeoClientOptions\.NetworkMagic') | Gets or sets the network magic number for identifying the Neo network\. |
| [RpcUrl](./ResQ.Blockchain.NeoClientOptions.RpcUrl.md 'ResQ\.Blockchain\.NeoClientOptions\.RpcUrl') | Gets or sets the Neo N3 RPC endpoint URL\. |
| [WalletPath](./ResQ.Blockchain.NeoClientOptions.WalletPath.md 'ResQ\.Blockchain\.NeoClientOptions\.WalletPath') | Gets or sets the file path to the wallet for transaction signing\. |
