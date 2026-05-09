---
sidebarTitle: 'BuildResiliencePipeline()'
---

### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataClient](./ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')

## PinataClient\.BuildResiliencePipeline\(\) Method

Builds the resilience pipeline with circuit breaker and timeout policies\.

```csharp
private Polly.ResiliencePipeline<System.Net.Http.HttpResponseMessage> BuildResiliencePipeline();
```

#### Returns
[Polly\.ResiliencePipeline&lt;](https://learn.microsoft.com/en-us/dotnet/api/polly.resiliencepipeline-1 'Polly\.ResiliencePipeline\`1')[System\.Net\.Http\.HttpResponseMessage](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage 'System\.Net\.Http\.HttpResponseMessage')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/polly.resiliencepipeline-1 'Polly\.ResiliencePipeline\`1')
