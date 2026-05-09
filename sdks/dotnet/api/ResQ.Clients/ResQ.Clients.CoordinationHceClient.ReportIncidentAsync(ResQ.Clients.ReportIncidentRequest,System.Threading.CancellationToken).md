### [ResQ\.Clients](ResQ.Clients.md 'ResQ\.Clients').[CoordinationHceClient](ResQ.Clients.CoordinationHceClient.md 'ResQ\.Clients\.CoordinationHceClient')

## CoordinationHceClient\.ReportIncidentAsync\(ReportIncidentRequest, CancellationToken\) Method

Reports an incident to HCE\.
Uses timeout and circuit\-breaker handling without replaying the mutation on failure\.

```csharp
public System.Threading.Tasks.Task<ResQ.Clients.IncidentAck> ReportIncidentAsync(ResQ.Clients.ReportIncidentRequest incident, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.CoordinationHceClient.ReportIncidentAsync(ResQ.Clients.ReportIncidentRequest,System.Threading.CancellationToken).incident'></a>

`incident` [ReportIncidentRequest](ResQ.Clients.ReportIncidentRequest.md 'ResQ\.Clients\.ReportIncidentRequest')

<a name='ResQ.Clients.CoordinationHceClient.ReportIncidentAsync(ResQ.Clients.ReportIncidentRequest,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[IncidentAck](ResQ.Clients.IncidentAck.md 'ResQ\.Clients\.IncidentAck')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
