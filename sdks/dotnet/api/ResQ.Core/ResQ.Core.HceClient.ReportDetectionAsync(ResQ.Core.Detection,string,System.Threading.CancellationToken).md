---
sidebarTitle: 'ReportDetectionAsync(Detection, string, CancellationToken)'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[HceClient](./ResQ.Core.HceClient.md 'ResQ\.Core\.HceClient')

## HceClient\.ReportDetectionAsync\(Detection, string, CancellationToken\) Method

Reports a critical detection to the HCE service\.

```csharp
public System.Threading.Tasks.Task<bool> ReportDetectionAsync(ResQ.Core.Detection detection, string droneId, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Core.HceClient.ReportDetectionAsync(ResQ.Core.Detection,string,System.Threading.CancellationToken).detection'></a>

`detection` [Detection](./ResQ.Core.Detection.md 'ResQ\.Core\.Detection')

The detection to report\.

<a name='ResQ.Core.HceClient.ReportDetectionAsync(ResQ.Core.Detection,string,System.Threading.CancellationToken).droneId'></a>

`droneId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

ID of the drone that made the detection\.

<a name='ResQ.Core.HceClient.ReportDetectionAsync(ResQ.Core.Detection,string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
True if the report was accepted\.
