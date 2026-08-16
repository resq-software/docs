---
sidebarTitle: 'BuildResiliencePipeline(bool)'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient')

## BaseServiceClient\.BuildResiliencePipeline\(bool\) Method

Builds the resilience pipeline with circuit breaker, timeout, and optional retries\.

```csharp
private Polly.ResiliencePipeline<System.Net.Http.HttpResponseMessage> BuildResiliencePipeline(bool enableRetries);
```
#### Parameters

<a name='ResQ.Clients.BaseServiceClient.BuildResiliencePipeline(bool).enableRetries'></a>

`enableRetries` [System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')

#### Returns
[Polly\.ResiliencePipeline&lt;](https://www.pollydocs.org/api/Polly.ResiliencePipeline-1.html 'Polly\.ResiliencePipeline\`1')[System\.Net\.Http\.HttpResponseMessage](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage 'System\.Net\.Http\.HttpResponseMessage')[&gt;](https://www.pollydocs.org/api/Polly.ResiliencePipeline-1.html 'Polly\.ResiliencePipeline\`1')
