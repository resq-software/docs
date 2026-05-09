---
sidebarTitle: 'Clients'
---

## ResQ\.Clients Namespace

| Classes | |
| :--- | :--- |
| [AuthResponse](./ResQ.Clients.AuthResponse.md 'ResQ\.Clients\.AuthResponse') | Response from the HCE authentication endpoint\. |
| [BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient') | Abstract base class for ResQ service clients\. Provides common HTTP client setup with resilience patterns \(retry, circuit breaker, timeout\)\. |
| [BlockchainEventRequest](./ResQ.Clients.BlockchainEventRequest.md 'ResQ\.Clients\.BlockchainEventRequest') | Request to record a blockchain event via infrastructure\-api\. |
| [BlockchainEventResponse](./ResQ.Clients.BlockchainEventResponse.md 'ResQ\.Clients\.BlockchainEventResponse') | Response from recording a blockchain event\. |
| [CoordinationHceClient](./ResQ.Clients.CoordinationHceClient.md 'ResQ\.Clients\.CoordinationHceClient') | HTTP client for coordination\-hce \(Node\.js/Elysia\) service\. Provides methods to send telemetry, report incidents, and query fleet status\. Inherits resilience patterns from [BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient')\. |
| [CreateIncidentRequest](./ResQ.Clients.CreateIncidentRequest.md 'ResQ\.Clients\.CreateIncidentRequest') | Request to create a new incident\. |
| [Detection](./ResQ.Clients.Detection.md 'ResQ\.Clients\.Detection') | A detection result from the drone's AI system\. |
| [FleetStatus](./ResQ.Clients.FleetStatus.md 'ResQ\.Clients\.FleetStatus') | Status response for a fleet of drones\. |
| [HceHealthResponse](./ResQ.Clients.HceHealthResponse.md 'ResQ\.Clients\.HceHealthResponse') | Health check response from HCE service\. |
| [HealthResponse](./ResQ.Clients.HealthResponse.md 'ResQ\.Clients\.HealthResponse') | Health check response from infrastructure\-api\. |
| [IncidentAck](./ResQ.Clients.IncidentAck.md 'ResQ\.Clients\.IncidentAck') | Acknowledgment response from incident report\. |
| [IncidentResponse](./ResQ.Clients.IncidentResponse.md 'ResQ\.Clients\.IncidentResponse') | Response from creating or retrieving an incident\. |
| [InfraAuthResponse](./ResQ.Clients.InfraAuthResponse.md 'ResQ\.Clients\.InfraAuthResponse') | JWT response from infrastructure\-api /login endpoint\. |
| [InfrastructureApiClient](./ResQ.Clients.InfrastructureApiClient.md 'ResQ\.Clients\.InfrastructureApiClient') | HTTP client for infrastructure\-api \(Rust/Axum\) service\. Provides methods to upload evidence, record blockchain events, and manage incidents\. Inherits resilience patterns from [BaseServiceClient](./ResQ.Clients.BaseServiceClient.md 'ResQ\.Clients\.BaseServiceClient')\. |
| [LocationDto](./ResQ.Clients.LocationDto.md 'ResQ\.Clients\.LocationDto') | Geographic location with coordinates and altitude\. |
| [ReportIncidentRequest](./ResQ.Clients.ReportIncidentRequest.md 'ResQ\.Clients\.ReportIncidentRequest') | Request to report an incident to HCE\. |
| [TelemetryBatchRequest](./ResQ.Clients.TelemetryBatchRequest.md 'ResQ\.Clients\.TelemetryBatchRequest') | Request containing a batch of telemetry packets from a drone\. |
| [TelemetryPacket](./ResQ.Clients.TelemetryPacket.md 'ResQ\.Clients\.TelemetryPacket') | A single telemetry packet from a drone\. |
| [UploadResponse](./ResQ.Clients.UploadResponse.md 'ResQ\.Clients\.UploadResponse') | Response from an IPFS upload operation\. |
