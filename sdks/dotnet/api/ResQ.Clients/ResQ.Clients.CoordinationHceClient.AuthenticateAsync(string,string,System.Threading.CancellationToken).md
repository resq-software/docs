### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[CoordinationHceClient](./ResQ.Clients.CoordinationHceClient.md 'ResQ\.Clients\.CoordinationHceClient')

## CoordinationHceClient\.AuthenticateAsync\(string, string, CancellationToken\) Method

Authenticates with HCE to get JWT token \(if auth is enabled\)\.

```csharp
public System.Threading.Tasks.Task<bool> AuthenticateAsync(string username, string password, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.CoordinationHceClient.AuthenticateAsync(string,string,System.Threading.CancellationToken).username'></a>

`username` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

<a name='ResQ.Clients.CoordinationHceClient.AuthenticateAsync(string,string,System.Threading.CancellationToken).password'></a>

`password` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

<a name='ResQ.Clients.CoordinationHceClient.AuthenticateAsync(string,string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
