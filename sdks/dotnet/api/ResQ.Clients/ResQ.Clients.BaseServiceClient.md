### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients')

## BaseServiceClient Class

Abstract base class for ResQ service clients\.
Provides common HTTP client setup with resilience patterns \(retry, circuit breaker, timeout\)\.

```csharp
public abstract class BaseServiceClient : System.IDisposable
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; BaseServiceClient

Derived  
&#8627; [CoordinationHceClient](./ResQ.Clients.CoordinationHceClient.md 'ResQ\.Clients\.CoordinationHceClient')  
&#8627; [InfrastructureApiClient](./ResQ.Clients.InfrastructureApiClient.md 'ResQ\.Clients\.InfrastructureApiClient')

Implements [System\.IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable 'System\.IDisposable')

| Properties | |
| :--- | :--- |
| [AuthorizationHeader](./ResQ.Clients.BaseServiceClient.AuthorizationHeader.md 'ResQ\.Clients\.BaseServiceClient\.AuthorizationHeader') | Gets or sets the authorization header for the current async flow\. |
| [ServiceName](./ResQ.Clients.BaseServiceClient.ServiceName.md 'ResQ\.Clients\.BaseServiceClient\.ServiceName') | Service name for logging purposes \(e\.g\., "Infrastructure API", "Coordination HCE"\)\. |

| Methods | |
| :--- | :--- |
| [Dispose\(\)](./ResQ.Clients.BaseServiceClient.Dispose().md 'ResQ\.Clients\.BaseServiceClient\.Dispose\(\)') | Disposes the HTTP client\. |
| [ExecuteWithResilienceAsync\(HttpMethod, Func&lt;CancellationToken,Task&lt;HttpResponseMessage&gt;&gt;, CancellationToken\)](./ResQ.Clients.BaseServiceClient.ExecuteWithResilienceAsync(System.Net.Http.HttpMethod,System.Func_System.Threading.CancellationToken,System.Threading.Tasks.Task_System.Net.Http.HttpResponseMessage__,System.Threading.CancellationToken).md 'ResQ\.Clients\.BaseServiceClient\.ExecuteWithResilienceAsync\(System\.Net\.Http\.HttpMethod, System\.Func\<System\.Threading\.CancellationToken,System\.Threading\.Tasks\.Task\<System\.Net\.Http\.HttpResponseMessage\>\>, System\.Threading\.CancellationToken\)') | Executes an HTTP request with a resilience policy appropriate for the HTTP method\. |
| [SendAsync\(HttpMethod, string, HttpContent, CancellationToken, bool\)](./ResQ.Clients.BaseServiceClient.SendAsync(System.Net.Http.HttpMethod,string,System.Net.Http.HttpContent,System.Threading.CancellationToken,bool).md 'ResQ\.Clients\.BaseServiceClient\.SendAsync\(System\.Net\.Http\.HttpMethod, string, System\.Net\.Http\.HttpContent, System\.Threading\.CancellationToken, bool\)') | Sends an HTTP request, applying authorization from the current async flow when present\. |
