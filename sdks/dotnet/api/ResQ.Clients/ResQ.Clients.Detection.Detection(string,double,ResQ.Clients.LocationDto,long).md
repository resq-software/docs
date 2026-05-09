---
sidebarTitle: 'Detection(string, double, LocationDto, long)'
---

### [ResQ\.Clients](./ResQ.Clients.md 'ResQ\.Clients').[Detection](./ResQ.Clients.Detection.md 'ResQ\.Clients\.Detection')

## Detection\(string, double, LocationDto, long\) Constructor

A detection result from the drone's AI system\.

```csharp
public Detection(string Type, double Confidence, ResQ.Clients.LocationDto Location, long Timestamp);
```
#### Parameters

<a name='ResQ.Clients.Detection.Detection(string,double,ResQ.Clients.LocationDto,long).Type'></a>

`Type` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Type of detection \(e\.g\., "FIRE", "FLOOD", "PERSON"\)\.

<a name='ResQ.Clients.Detection.Detection(string,double,ResQ.Clients.LocationDto,long).Confidence'></a>

`Confidence` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

AI confidence score \(0\.0 to 1\.0\)\.

<a name='ResQ.Clients.Detection.Detection(string,double,ResQ.Clients.LocationDto,long).Location'></a>

`Location` [LocationDto](./ResQ.Clients.LocationDto.md 'ResQ\.Clients\.LocationDto')

Geographic location of the detection\.

<a name='ResQ.Clients.Detection.Detection(string,double,ResQ.Clients.LocationDto,long).Timestamp'></a>

`Timestamp` [System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')

Unix timestamp when detection occurred\.
