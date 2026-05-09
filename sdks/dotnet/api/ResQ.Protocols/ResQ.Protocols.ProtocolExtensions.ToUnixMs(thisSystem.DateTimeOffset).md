---
sidebarTitle: 'ToUnixMs(DateTimeOffset)'
---

### [ResQ\.Protocols](./ResQ.Protocols.md 'ResQ\.Protocols').[ProtocolExtensions](./ResQ.Protocols.ProtocolExtensions.md 'ResQ\.Protocols\.ProtocolExtensions')

## ProtocolExtensions\.ToUnixMs\(this DateTimeOffset\) Method

Converts a [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset') to a Unix timestamp in milliseconds\.

```csharp
public static long ToUnixMs(this System.DateTimeOffset dateTime);
```
#### Parameters

<a name='ResQ.Protocols.ProtocolExtensions.ToUnixMs(thisSystem.DateTimeOffset).dateTime'></a>

`dateTime` [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')

The date and time to convert\.

#### Returns
[System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')  
The Unix timestamp in milliseconds since January 1, 1970 UTC\.

### Example

```csharp
// Convert current time
var now = DateTimeOffset.UtcNow;
var timestamp = now.ToUnixMs();

// Set protobuf timestamp field
protoMessage.TimestampMs = timestamp;

// Convert specific time
var eventTime = new DateTimeOffset(2024, 1, 1, 0, 0, 0, TimeSpan.Zero);
var eventTimestamp = eventTime.ToUnixMs(); // 1704067200000
```

### Remarks
This method converts a [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset') to Unix time in milliseconds,
which is commonly used in protobuf messages, JSON APIs, and JavaScript interop\.
The conversion accounts for the offset and returns the UTC\-based timestamp\.
