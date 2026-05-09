### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient')

## BaseServiceClient\.ExecuteWithResilienceAsync\(HttpMethod, Func\<CancellationToken,Task\<HttpResponseMessage\>\>, CancellationToken\) Method

Executes an HTTP request with a resilience policy appropriate for the HTTP method\.

```csharp
protected System.Threading.Tasks.Task<System.Net.Http.HttpResponseMessage> ExecuteWithResilienceAsync(System.Net.Http.HttpMethod method, System.Func<System.Threading.CancellationToken,System.Threading.Tasks.Task<System.Net.Http.HttpResponseMessage>> action, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Clients.BaseServiceClient.ExecuteWithResilienceAsync(System.Net.Http.HttpMethod,System.Func_System.Threading.CancellationToken,System.Threading.Tasks.Task_System.Net.Http.HttpResponseMessage__,System.Threading.CancellationToken).method'></a>

`method` [System\.Net\.Http\.HttpMethod](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpmethod 'System\.Net\.Http\.HttpMethod')

<a name='ResQ.Clients.BaseServiceClient.ExecuteWithResilienceAsync(System.Net.Http.HttpMethod,System.Func_System.Threading.CancellationToken,System.Threading.Tasks.Task_System.Net.Http.HttpResponseMessage__,System.Threading.CancellationToken).action'></a>

`action` [System\.Func&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.func-2 'System\.Func\`2')[System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')[,](https://learn.microsoft.com/en-us/dotnet/api/system.func-2 'System\.Func\`2')[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Net\.Http\.HttpResponseMessage](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage 'System\.Net\.Http\.HttpResponseMessage')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.func-2 'System\.Func\`2')

<a name='ResQ.Clients.BaseServiceClient.ExecuteWithResilienceAsync(System.Net.Http.HttpMethod,System.Func_System.Threading.CancellationToken,System.Threading.Tasks.Task_System.Net.Http.HttpResponseMessage__,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Net\.Http\.HttpResponseMessage](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage 'System\.Net\.Http\.HttpResponseMessage')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
