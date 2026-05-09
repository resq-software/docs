---
sidebarTitle: 'GetTransactionStatusAsync(string, CancellationToken)'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[NeoClient](./ResQ.Core.NeoClient.md 'ResQ\.Core\.NeoClient')

## NeoClient\.GetTransactionStatusAsync\(string, CancellationToken\) Method

Gets the status of a blockchain transaction\.

```csharp
public System.Threading.Tasks.Task<ResQ.Core.TransactionStatus> GetTransactionStatusAsync(string txHash, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Core.NeoClient.GetTransactionStatusAsync(string,System.Threading.CancellationToken).txHash'></a>

`txHash` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The transaction hash\.

<a name='ResQ.Core.NeoClient.GetTransactionStatusAsync(string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[TransactionStatus](./ResQ.Core.TransactionStatus.md 'ResQ\.Core\.TransactionStatus')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
The current transaction status\.
