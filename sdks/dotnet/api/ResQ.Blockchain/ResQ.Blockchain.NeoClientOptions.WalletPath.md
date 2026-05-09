---
sidebarTitle: 'WalletPath'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[NeoClientOptions](./ResQ.Blockchain.NeoClientOptions.md 'ResQ\.Blockchain\.NeoClientOptions')

## NeoClientOptions\.WalletPath Property

Gets or sets the file path to the wallet for transaction signing\.

```csharp
public string? WalletPath { get; set; }
```

#### Property Value
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The absolute or relative path to the wallet file, or null if not using a wallet file\.

### Example

```csharp
options.WalletPath = "/secure/wallets/resq-wallet.json";
```

### Remarks
This should point to a Neo N3 compatible wallet file \(e\.g\., \.json or \.db3 format\)\.
The wallet will be used to sign transactions before submission to the blockchain\.
For security, ensure the wallet file has appropriate access restrictions\.
