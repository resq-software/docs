### [ResQ\.Clients](ResQ.Clients.md 'ResQ\.Clients').[InfrastructureApiClient](ResQ.Clients.InfrastructureApiClient.md 'ResQ\.Clients\.InfrastructureApiClient')

## InfrastructureApiClient\.AuthenticateAsync\(string, string, CancellationToken\) Method

Authenticates with infrastructure\-api to get a JWT token\.
Sets the Authorization header for subsequent requests\.

```csharp
public System.Threading.Tasks.Task<bool> AuthenticateAsync(string username, string password, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.InfrastructureApiClient.AuthenticateAsync(string,string,System.Threading.CancellationToken).username'></a>

`username` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

<a name='ResQ.Clients.InfrastructureApiClient.AuthenticateAsync(string,string,System.Threading.CancellationToken).password'></a>

`password` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

<a name='ResQ.Clients.InfrastructureApiClient.AuthenticateAsync(string,string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
