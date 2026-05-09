---
sidebarTitle: 'InfrastructureApiClient'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients')

## InfrastructureApiClient Class

HTTP client for infrastructure\-api \(Rust/Axum\) service\.
Provides methods to upload evidence, record blockchain events, and manage incidents\.
Inherits resilience patterns from [BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient')\.

```csharp
public class InfrastructureApiClient : ResQ.Clients.BaseServiceClient
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; [BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient') &#129106; InfrastructureApiClient

| Methods | |
| :--- | :--- |
| [AuthenticateAsync\(string, string, CancellationToken\)](./ResQ.Clients.InfrastructureApiClient.AuthenticateAsync(string,string,System.Threading.CancellationToken).md 'ResQ\.Clients\.InfrastructureApiClient\.AuthenticateAsync\(string, string, System\.Threading\.CancellationToken\)') | Authenticates with infrastructure\-api to get a JWT token\. Sets the Authorization header for subsequent requests\. |
| [CreateIncidentAsync\(CreateIncidentRequest, CancellationToken\)](./ResQ.Clients.InfrastructureApiClient.CreateIncidentAsync(ResQ.Clients.CreateIncidentRequest,System.Threading.CancellationToken).md 'ResQ\.Clients\.InfrastructureApiClient\.CreateIncidentAsync\(ResQ\.Clients\.CreateIncidentRequest, System\.Threading\.CancellationToken\)') | Creates an incident record\. Uses timeout and circuit\-breaker handling without replaying the mutation on failure\. |
| [GetHealthAsync\(CancellationToken\)](./ResQ.Clients.InfrastructureApiClient.GetHealthAsync(System.Threading.CancellationToken).md 'ResQ\.Clients\.InfrastructureApiClient\.GetHealthAsync\(System\.Threading\.CancellationToken\)') | Gets infrastructure\-api health status\. Includes retry logic for transient read failures\. |
| [RecordEventAsync\(BlockchainEventRequest, CancellationToken\)](./ResQ.Clients.InfrastructureApiClient.RecordEventAsync(ResQ.Clients.BlockchainEventRequest,System.Threading.CancellationToken).md 'ResQ\.Clients\.InfrastructureApiClient\.RecordEventAsync\(ResQ\.Clients\.BlockchainEventRequest, System\.Threading\.CancellationToken\)') | Records a blockchain event via infrastructure\-api Neo N3 adapter\. Uses timeout and circuit\-breaker handling without replaying the mutation on failure\. |
| [UploadImageAsync\(byte\[\], string, CancellationToken\)](./ResQ.Clients.InfrastructureApiClient.UploadImageAsync(byte[],string,System.Threading.CancellationToken).md 'ResQ\.Clients\.InfrastructureApiClient\.UploadImageAsync\(byte\[\], string, System\.Threading\.CancellationToken\)') | Uploads an image to IPFS via infrastructure\-api\. Uses timeout and circuit\-breaker handling without replaying the upload on failure\. |
