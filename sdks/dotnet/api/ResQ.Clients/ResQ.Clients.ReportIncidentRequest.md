### [ResQ\.Clients](ResQ.Clients.md 'ResQ\.Clients')

## ReportIncidentRequest Class

Request to report an incident to HCE\.

```csharp
public record ReportIncidentRequest : System.IEquatable<ResQ.Clients.ReportIncidentRequest>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; ReportIncidentRequest

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[ReportIncidentRequest](ResQ.Clients.ReportIncidentRequest.md 'ResQ\.Clients\.ReportIncidentRequest')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

| Constructors | |
| :--- | :--- |
| [ReportIncidentRequest\(string, string, LocationDto, string\)](ResQ.Clients.ReportIncidentRequest.ReportIncidentRequest(string,string,ResQ.Clients.LocationDto,string).md 'ResQ\.Clients\.ReportIncidentRequest\.ReportIncidentRequest\(string, string, ResQ\.Clients\.LocationDto, string\)') | Request to report an incident to HCE\. |

| Properties | |
| :--- | :--- |
| [Description](ResQ.Clients.ReportIncidentRequest.Description.md 'ResQ\.Clients\.ReportIncidentRequest\.Description') | Optional human\-readable description\. |
| [IncidentType](ResQ.Clients.ReportIncidentRequest.IncidentType.md 'ResQ\.Clients\.ReportIncidentRequest\.IncidentType') | Type of incident \(e\.g\., "FIRE", "FLOOD"\)\. |
| [Location](ResQ.Clients.ReportIncidentRequest.Location.md 'ResQ\.Clients\.ReportIncidentRequest\.Location') | Geographic location of the incident\. |
| [Severity](ResQ.Clients.ReportIncidentRequest.Severity.md 'ResQ\.Clients\.ReportIncidentRequest\.Severity') | Severity level \(e\.g\., "LOW", "MEDIUM", "HIGH", "CRITICAL"\)\. |
