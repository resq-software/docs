### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[PdieClient](./ResQ.Core.PdieClient.md 'ResQ\.Core\.PdieClient')

## PdieClient\.GetPreAlertsAsync\(string, CancellationToken\) Method

Gets current pre\-alerts, optionally filtered by sector\.

```csharp
public System.Threading.Tasks.Task<System.Collections.Generic.List<ResQ.Core.PreAlert>> GetPreAlertsAsync(string? sectorId=null, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Core.PdieClient.GetPreAlertsAsync(string,System.Threading.CancellationToken).sectorId'></a>

`sectorId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Optional sector filter\.

<a name='ResQ.Core.PdieClient.GetPreAlertsAsync(string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Collections\.Generic\.List&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1 'System\.Collections\.Generic\.List\`1')[PreAlert](./ResQ.Core.PreAlert.md 'ResQ\.Core\.PreAlert')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1 'System\.Collections\.Generic\.List\`1')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
List of active pre\-alerts\.
