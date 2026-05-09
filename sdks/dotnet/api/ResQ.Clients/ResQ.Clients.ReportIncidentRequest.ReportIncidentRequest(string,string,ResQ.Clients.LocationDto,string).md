### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[ReportIncidentRequest](./ResQ.Clients.ReportIncidentRequest.md 'ResQ\.Clients\.ReportIncidentRequest')

## ReportIncidentRequest\(string, string, LocationDto, string\) Constructor

Request to report an incident to HCE\.

```csharp
public ReportIncidentRequest(string IncidentType, string Severity, ResQ.Clients.LocationDto Location, string? Description);
```
#### Parameters

<a name='ResQ.Clients.ReportIncidentRequest.ReportIncidentRequest(string,string,ResQ.Clients.LocationDto,string).IncidentType'></a>

`IncidentType` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Type of incident \(e\.g\., "FIRE", "FLOOD"\)\.

<a name='ResQ.Clients.ReportIncidentRequest.ReportIncidentRequest(string,string,ResQ.Clients.LocationDto,string).Severity'></a>

`Severity` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Severity level \(e\.g\., "LOW", "MEDIUM", "HIGH", "CRITICAL"\)\.

<a name='ResQ.Clients.ReportIncidentRequest.ReportIncidentRequest(string,string,ResQ.Clients.LocationDto,string).Location'></a>

`Location` [LocationDto](./ResQ.Clients.LocationDto.md 'ResQ\.Clients\.LocationDto')

Geographic location of the incident\.

<a name='ResQ.Clients.ReportIncidentRequest.ReportIncidentRequest(string,string,ResQ.Clients.LocationDto,string).Description'></a>

`Description` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Optional human\-readable description\.
