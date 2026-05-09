---
sidebarTitle: 'GetHealthAsync(CancellationToken)'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[CoordinationHceClient](./ResQ.Clients.CoordinationHceClient.md 'ResQ\.Clients\.CoordinationHceClient')

## CoordinationHceClient\.GetHealthAsync\(CancellationToken\) Method

Gets HCE health status\.
Includes retry logic for transient read failures\.

```csharp
public System.Threading.Tasks.Task<ResQ.Clients.HceHealthResponse> GetHealthAsync(System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.CoordinationHceClient.GetHealthAsync(System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[HceHealthResponse](./ResQ.Clients.HceHealthResponse.md 'ResQ\.Clients\.HceHealthResponse')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
