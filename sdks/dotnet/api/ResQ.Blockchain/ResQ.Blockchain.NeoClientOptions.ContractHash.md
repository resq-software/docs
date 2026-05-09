### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[NeoClientOptions](./ResQ.Blockchain.NeoClientOptions.md 'ResQ\.Blockchain\.NeoClientOptions')

## NeoClientOptions\.ContractHash Property

Gets or sets the smart contract script hash for ResQ event recording\.

```csharp
public string ContractHash { get; set; }
```

#### Property Value
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The 40\-character hexadecimal contract script hash\.

### Example

```csharp
options.ContractHash = "0x8d35a57f8c01156527c92ebbb4d772fa9574cbf4";
```

### Remarks
This is the hash of the deployed smart contract that handles ResQ events\.
It must be set to a valid contract hash for blockchain operations to succeed\.
