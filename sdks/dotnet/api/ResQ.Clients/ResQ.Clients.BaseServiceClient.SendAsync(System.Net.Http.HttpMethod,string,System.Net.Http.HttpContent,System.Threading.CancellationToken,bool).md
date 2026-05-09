---
sidebarTitle: 'SendAsync(HttpMethod, string, HttpContent, CancellationToken, bool)'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient')

## BaseServiceClient\.SendAsync\(HttpMethod, string, HttpContent, CancellationToken, bool\) Method

Sends an HTTP request, applying authorization from the current async flow when present\.

```csharp
protected System.Threading.Tasks.Task<System.Net.Http.HttpResponseMessage> SendAsync(System.Net.Http.HttpMethod method, string requestUri, System.Net.Http.HttpContent? content=null, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken), bool includeAuthorization=true);
```
#### Parameters

<a name='ResQ.Clients.BaseServiceClient.SendAsync(System.Net.Http.HttpMethod,string,System.Net.Http.HttpContent,System.Threading.CancellationToken,bool).method'></a>

`method` [System\.Net\.Http\.HttpMethod](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpmethod 'System\.Net\.Http\.HttpMethod')

<a name='ResQ.Clients.BaseServiceClient.SendAsync(System.Net.Http.HttpMethod,string,System.Net.Http.HttpContent,System.Threading.CancellationToken,bool).requestUri'></a>

`requestUri` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

<a name='ResQ.Clients.BaseServiceClient.SendAsync(System.Net.Http.HttpMethod,string,System.Net.Http.HttpContent,System.Threading.CancellationToken,bool).content'></a>

`content` [System\.Net\.Http\.HttpContent](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpcontent 'System\.Net\.Http\.HttpContent')

<a name='ResQ.Clients.BaseServiceClient.SendAsync(System.Net.Http.HttpMethod,string,System.Net.Http.HttpContent,System.Threading.CancellationToken,bool).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

<a name='ResQ.Clients.BaseServiceClient.SendAsync(System.Net.Http.HttpMethod,string,System.Net.Http.HttpContent,System.Threading.CancellationToken,bool).includeAuthorization'></a>

`includeAuthorization` [System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Net\.Http\.HttpResponseMessage](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage 'System\.Net\.Http\.HttpResponseMessage')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')
