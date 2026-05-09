---
sidebarTitle: 'TransactionResult'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain')

## TransactionResult Class

Represents the result of a blockchain transaction submission\.

```csharp
public record TransactionResult : System.IEquatable<ResQ.Blockchain.TransactionResult>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; TransactionResult

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[TransactionResult](./ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var result = new TransactionResult(
    TransactionHash: "0xabc123...",
    IsConfirmed: true,
    BlockHeight: 1234567,
    Timestamp: DateTimeOffset.UtcNow
);

if (result.IsConfirmed)
{
    Console.WriteLine($"Confirmed in block {result.BlockHeight}");
}
```

### Remarks
This record contains all relevant information about a transaction after it has been
submitted to the Neo N3 blockchain, including its hash, confirmation status, and
the block height at which it was included\.

| Constructors | |
| :--- | :--- |
| [TransactionResult\(string, bool, ulong, DateTimeOffset\)](./ResQ.Blockchain.TransactionResult.TransactionResult(string,bool,ulong,System.DateTimeOffset).md 'ResQ\.Blockchain\.TransactionResult\.TransactionResult\(string, bool, ulong, System\.DateTimeOffset\)') | Represents the result of a blockchain transaction submission\. |

| Properties | |
| :--- | :--- |
| [BlockHeight](./ResQ.Blockchain.TransactionResult.BlockHeight.md 'ResQ\.Blockchain\.TransactionResult\.BlockHeight') | The block number where the transaction was included\. |
| [IsConfirmed](./ResQ.Blockchain.TransactionResult.IsConfirmed.md 'ResQ\.Blockchain\.TransactionResult\.IsConfirmed') | True if the transaction has been confirmed on\-chain\. |
| [Timestamp](./ResQ.Blockchain.TransactionResult.Timestamp.md 'ResQ\.Blockchain\.TransactionResult\.Timestamp') | The UTC timestamp when the result was created\. |
| [TransactionHash](./ResQ.Blockchain.TransactionResult.TransactionHash.md 'ResQ\.Blockchain\.TransactionResult\.TransactionHash') | The hexadecimal hash of the transaction\. |
