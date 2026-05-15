---
sidebarTitle: 'CoordinationHceClient'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients')

## CoordinationHceClient Class

HTTP client for coordination\-hce \(Node\.js/Elysia\) service\.
Provides methods to send telemetry, report incidents, and query fleet status\.
Inherits resilience patterns from [BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient')\.

```csharp
public class CoordinationHceClient : ResQ.Clients.BaseServiceClient
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → [BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient') → CoordinationHceClient

| Methods | |
| :--- | :--- |
| [AuthenticateAsync\(string, string, CancellationToken\)](./ResQ.Clients.CoordinationHceClient.AuthenticateAsync(string,string,System.Threading.CancellationToken).md 'ResQ\.Clients\.CoordinationHceClient\.AuthenticateAsync\(string, string, System\.Threading\.CancellationToken\)') | Authenticates with HCE to get JWT token \(if auth is enabled\)\. |
| [GetFleetStatusAsync\(string, CancellationToken\)](./ResQ.Clients.CoordinationHceClient.GetFleetStatusAsync(string,System.Threading.CancellationToken).md 'ResQ\.Clients\.CoordinationHceClient\.GetFleetStatusAsync\(string, System\.Threading\.CancellationToken\)') | Gets the status of a fleet\. Includes retry logic for transient read failures\. |
| [GetHealthAsync\(CancellationToken\)](./ResQ.Clients.CoordinationHceClient.GetHealthAsync(System.Threading.CancellationToken).md 'ResQ\.Clients\.CoordinationHceClient\.GetHealthAsync\(System\.Threading\.CancellationToken\)') | Gets HCE health status\. Includes retry logic for transient read failures\. |
| [ReportIncidentAsync\(ReportIncidentRequest, CancellationToken\)](./ResQ.Clients.CoordinationHceClient.ReportIncidentAsync(ResQ.Clients.ReportIncidentRequest,System.Threading.CancellationToken).md 'ResQ\.Clients\.CoordinationHceClient\.ReportIncidentAsync\(ResQ\.Clients\.ReportIncidentRequest, System\.Threading\.CancellationToken\)') | Reports an incident to HCE\. Uses timeout and circuit\-breaker handling without replaying the mutation on failure\. |
| [SendTelemetryBatchAsync\(TelemetryBatchRequest, CancellationToken\)](./ResQ.Clients.CoordinationHceClient.SendTelemetryBatchAsync(ResQ.Clients.TelemetryBatchRequest,System.Threading.CancellationToken).md 'ResQ\.Clients\.CoordinationHceClient\.SendTelemetryBatchAsync\(ResQ\.Clients\.TelemetryBatchRequest, System\.Threading\.CancellationToken\)') | Sends a batch of telemetry packets from a drone\. Uses timeout and circuit\-breaker handling without replaying the mutation on failure\. |
