---
sidebarTitle: 'GetHealthAsync(CancellationToken)'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[InfrastructureApiClient](./ResQ.Clients.InfrastructureApiClient.md 'ResQ\.Clients\.InfrastructureApiClient')

## InfrastructureApiClient\.GetHealthAsync\(CancellationToken\) Method

Gets infrastructure\-api health status\.
Includes retry logic for transient read failures\.

```csharp
public System.Threading.Tasks.Task<ResQ.Clients.HealthResponse> GetHealthAsync(System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.InfrastructureApiClient.GetHealthAsync(System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[HealthResponse](./ResQ.Clients.HealthResponse.md 'ResQ\.Clients\.HealthResponse')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
