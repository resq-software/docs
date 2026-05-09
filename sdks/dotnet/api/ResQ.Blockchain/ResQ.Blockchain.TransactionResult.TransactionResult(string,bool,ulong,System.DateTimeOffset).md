### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[TransactionResult](./ResQ.Blockchain.TransactionResult.md 'ResQ\.Blockchain\.TransactionResult')

## TransactionResult\(string, bool, ulong, DateTimeOffset\) Constructor

Represents the result of a blockchain transaction submission\.

```csharp
public TransactionResult(string TransactionHash, bool IsConfirmed, ulong BlockHeight, System.DateTimeOffset Timestamp);
```
#### Parameters

<a name='ResQ.Blockchain.TransactionResult.TransactionResult(string,bool,ulong,System.DateTimeOffset).TransactionHash'></a>

`TransactionHash` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The hexadecimal hash of the transaction\.

<a name='ResQ.Blockchain.TransactionResult.TransactionResult(string,bool,ulong,System.DateTimeOffset).IsConfirmed'></a>

`IsConfirmed` [System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')

True if the transaction has been confirmed on\-chain\.

<a name='ResQ.Blockchain.TransactionResult.TransactionResult(string,bool,ulong,System.DateTimeOffset).BlockHeight'></a>

`BlockHeight` [System\.UInt64](https://learn.microsoft.com/en-us/dotnet/api/system.uint64 'System\.UInt64')

The block number where the transaction was included\.

<a name='ResQ.Blockchain.TransactionResult.TransactionResult(string,bool,ulong,System.DateTimeOffset).Timestamp'></a>

`Timestamp` [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')

The UTC timestamp when the result was created\.

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
