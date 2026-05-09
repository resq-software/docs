### [ResQ\.Clients](ResQ.Clients.md 'ResQ\.Clients').[InfrastructureApiClient](ResQ.Clients.InfrastructureApiClient.md 'ResQ\.Clients\.InfrastructureApiClient')

## InfrastructureApiClient\.CreateIncidentAsync\(CreateIncidentRequest, CancellationToken\) Method

Creates an incident record\.
Uses timeout and circuit\-breaker handling without replaying the mutation on failure\.

```csharp
public System.Threading.Tasks.Task<ResQ.Clients.IncidentResponse> CreateIncidentAsync(ResQ.Clients.CreateIncidentRequest request, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.InfrastructureApiClient.CreateIncidentAsync(ResQ.Clients.CreateIncidentRequest,System.Threading.CancellationToken).request'></a>

`request` [CreateIncidentRequest](ResQ.Clients.CreateIncidentRequest.md 'ResQ\.Clients\.CreateIncidentRequest')

<a name='ResQ.Clients.InfrastructureApiClient.CreateIncidentAsync(ResQ.Clients.CreateIncidentRequest,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[IncidentResponse](ResQ.Clients.IncidentResponse.md 'ResQ\.Clients\.IncidentResponse')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
