### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[InfrastructureApiClient](./ResQ.Clients.InfrastructureApiClient.md 'ResQ\.Clients\.InfrastructureApiClient')

## InfrastructureApiClient\.UploadImageAsync\(byte\[\], string, CancellationToken\) Method

Uploads an image to IPFS via infrastructure\-api\.
Uses timeout and circuit\-breaker handling without replaying the upload on failure\.

```csharp
public System.Threading.Tasks.Task<ResQ.Clients.UploadResponse> UploadImageAsync(byte[] imageData, string fileName, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.InfrastructureApiClient.UploadImageAsync(byte[],string,System.Threading.CancellationToken).imageData'></a>

`imageData` [System\.Byte](https://learn.microsoft.com/en-us/dotnet/api/system.byte 'System\.Byte')[\[\]](https://learn.microsoft.com/en-us/dotnet/api/system.array 'System\.Array')

<a name='ResQ.Clients.InfrastructureApiClient.UploadImageAsync(byte[],string,System.Threading.CancellationToken).fileName'></a>

`fileName` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

<a name='ResQ.Clients.InfrastructureApiClient.UploadImageAsync(byte[],string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[UploadResponse](./ResQ.Clients.UploadResponse.md 'ResQ\.Clients\.UploadResponse')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
