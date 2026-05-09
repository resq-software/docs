---
sidebarTitle: 'RequestStrategyAsync(string, CancellationToken)'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[DtsopClient](./ResQ.Core.DtsopClient.md 'ResQ\.Core\.DtsopClient')

## DtsopClient\.RequestStrategyAsync\(string, CancellationToken\) Method

Requests an optimization strategy for a scenario\.

```csharp
public System.Threading.Tasks.Task<ResQ.Core.OptimizationStrategy> RequestStrategyAsync(string scenarioId, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Core.DtsopClient.RequestStrategyAsync(string,System.Threading.CancellationToken).scenarioId'></a>

`scenarioId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

ID of the scenario to optimize\.

<a name='ResQ.Core.DtsopClient.RequestStrategyAsync(string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[OptimizationStrategy](./ResQ.Core.OptimizationStrategy.md 'ResQ\.Core\.OptimizationStrategy')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
The optimization strategy\.
