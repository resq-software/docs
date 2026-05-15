---
sidebarTitle: 'TransactionResult'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## TransactionResult Class

Represents the result of a blockchain transaction\.

```csharp
public record TransactionResult : System.IEquatable<ResQ.Core.TransactionResult>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → TransactionResult

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[TransactionResult](./ResQ.Core.TransactionResult.md 'ResQ\.Core\.TransactionResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var result = new TransactionResult
{
    TxHash = "0xabc123...",
    BlockHeight = 1234567,
    GasConsumed = 1000000,
    Status = TransactionStatus.Confirmed
};
```

### Remarks
Contains the transaction hash, block information, gas consumption, and status\.

| Properties | |
| :--- | :--- |
| [BlockHeight](./ResQ.Core.TransactionResult.BlockHeight.md 'ResQ\.Core\.TransactionResult\.BlockHeight') | Block height where transaction was included\. |
| [ErrorMessage](./ResQ.Core.TransactionResult.ErrorMessage.md 'ResQ\.Core\.TransactionResult\.ErrorMessage') | Error message if transaction failed\. |
| [GasConsumed](./ResQ.Core.TransactionResult.GasConsumed.md 'ResQ\.Core\.TransactionResult\.GasConsumed') | Gas consumed by the transaction\. |
| [Status](./ResQ.Core.TransactionResult.Status.md 'ResQ\.Core\.TransactionResult\.Status') | Current transaction status\. |
| [TxHash](./ResQ.Core.TransactionResult.TxHash.md 'ResQ\.Core\.TransactionResult\.TxHash') | Hexadecimal transaction hash\. |
