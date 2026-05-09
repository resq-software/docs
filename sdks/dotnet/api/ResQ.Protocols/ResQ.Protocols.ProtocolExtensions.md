---
sidebarTitle: 'ProtocolExtensions'
---

### [ResQ\.Protocols](./ResQ.Protocols.md 'ResQ\.Protocols')

## ProtocolExtensions Class

Provides extension methods for working with protobuf\-generated types and timestamps\.

```csharp
public static class ProtocolExtensions
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; ProtocolExtensions

### Example

```csharp
// Convert Unix timestamp from protobuf message
var timestamp = protoMessage.TimestampMs.FromUnixMs();
Console.WriteLine($"Event occurred at: {timestamp}");

// Convert to Unix timestamp for protobuf
var now = DateTimeOffset.UtcNow;
protoMessage.TimestampMs = now.ToUnixMs();
```

### Remarks
This static class contains utility extension methods that simplify working with
protocol buffer generated types, particularly for timestamp conversions between
Unix milliseconds and \.NET [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset') types\.


These extensions are commonly used when serializing/deserializing gRPC messages
and when interfacing with systems that use Unix timestamps.

| Methods | |
| :--- | :--- |
| [FromUnixMs\(this long\)](./ResQ.Protocols.ProtocolExtensions.FromUnixMs(thislong).md 'ResQ\.Protocols\.ProtocolExtensions\.FromUnixMs\(this long\)') | Converts a Unix timestamp in milliseconds to a [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')\. |
| [NowUnixMs\(\)](./ResQ.Protocols.ProtocolExtensions.NowUnixMs().md 'ResQ\.Protocols\.ProtocolExtensions\.NowUnixMs\(\)') | Creates a Unix timestamp in milliseconds for the current UTC time\. |
| [ToUnixMs\(this DateTimeOffset\)](./ResQ.Protocols.ProtocolExtensions.ToUnixMs(thisSystem.DateTimeOffset).md 'ResQ\.Protocols\.ProtocolExtensions\.ToUnixMs\(this System\.DateTimeOffset\)') | Converts a [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset') to a Unix timestamp in milliseconds\. |
