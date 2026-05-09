### [ResQ\.Core](ResQ.Core.md 'ResQ\.Core')

## TransactionStatus Enum

Represents the status of a blockchain transaction\.

```csharp
public enum TransactionStatus
```
### Fields

<a name='ResQ.Core.TransactionStatus.Pending'></a>

`Pending` 0

Transaction submitted but not yet confirmed\.

<a name='ResQ.Core.TransactionStatus.Confirmed'></a>

`Confirmed` 1

Transaction has been confirmed on the blockchain\.

<a name='ResQ.Core.TransactionStatus.Failed'></a>

`Failed` 2

Transaction failed or was rejected\.

### Example

```csharp
var result = await neoClient.RecordEventAsync(evt);
if (result.Status == TransactionStatus.Confirmed)
{
    Console.WriteLine($"Confirmed in block {result.BlockHeight}");
}
```

### Remarks
Transaction status tracks the lifecycle of a transaction from submission
through confirmation on the blockchain\.
