### [ResQ\.Core](ResQ.Core.md 'ResQ\.Core').[NeoClient](ResQ.Core.NeoClient.md 'ResQ\.Core\.NeoClient')

## NeoClient\.VerifyLocationAttestationAsync\(string, Location, DateTimeOffset, CancellationToken\) Method

Verifies a location attestation on the blockchain\.

```csharp
public System.Threading.Tasks.Task<bool> VerifyLocationAttestationAsync(string droneId, ResQ.Core.Location location, System.DateTimeOffset timestamp, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Core.NeoClient.VerifyLocationAttestationAsync(string,ResQ.Core.Location,System.DateTimeOffset,System.Threading.CancellationToken).droneId'></a>

`droneId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The drone identifier\.

<a name='ResQ.Core.NeoClient.VerifyLocationAttestationAsync(string,ResQ.Core.Location,System.DateTimeOffset,System.Threading.CancellationToken).location'></a>

`location` [Location](ResQ.Core.Location.md 'ResQ\.Core\.Location')

The location to verify\.

<a name='ResQ.Core.NeoClient.VerifyLocationAttestationAsync(string,ResQ.Core.Location,System.DateTimeOffset,System.Threading.CancellationToken).timestamp'></a>

`timestamp` [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')

The timestamp of the attestation\.

<a name='ResQ.Core.NeoClient.VerifyLocationAttestationAsync(string,ResQ.Core.Location,System.DateTimeOffset,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
True if the attestation is valid\.
