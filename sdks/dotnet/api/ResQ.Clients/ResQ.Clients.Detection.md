---
sidebarTitle: 'Detection'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients')

## Detection Class

A detection result from the drone's AI system\.

```csharp
public record Detection : System.IEquatable<ResQ.Clients.Detection>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; Detection

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[Detection](./ResQ.Clients.Detection.md 'ResQ\.Clients\.Detection')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

| Constructors | |
| :--- | :--- |
| [Detection\(string, double, LocationDto, long\)](./ResQ.Clients.Detection.Detection(string,double,ResQ.Clients.LocationDto,long).md 'ResQ\.Clients\.Detection\.Detection\(string, double, ResQ\.Clients\.LocationDto, long\)') | A detection result from the drone's AI system\. |

| Properties | |
| :--- | :--- |
| [Confidence](./ResQ.Clients.Detection.Confidence.md 'ResQ\.Clients\.Detection\.Confidence') | AI confidence score \(0\.0 to 1\.0\)\. |
| [Location](./ResQ.Clients.Detection.Location.md 'ResQ\.Clients\.Detection\.Location') | Geographic location of the detection\. |
| [Timestamp](./ResQ.Clients.Detection.Timestamp.md 'ResQ\.Clients\.Detection\.Timestamp') | Unix timestamp when detection occurred\. |
| [Type](./ResQ.Clients.Detection.Type.md 'ResQ\.Clients\.Detection\.Type') | Type of detection \(e\.g\., "FIRE", "FLOOD", "PERSON"\)\. |
