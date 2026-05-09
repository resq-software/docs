---
sidebarTitle: 'NowUnixMs()'
---

### [ResQ\.Protocols](./ResQ.Protocols.md 'ResQ\.Protocols').[ProtocolExtensions](./ResQ.Protocols.ProtocolExtensions.md 'ResQ\.Protocols\.ProtocolExtensions')

## ProtocolExtensions\.NowUnixMs\(\) Method

Creates a Unix timestamp in milliseconds for the current UTC time\.

```csharp
public static long NowUnixMs();
```

#### Returns
[System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')  
The current UTC time as a Unix timestamp in milliseconds\.

### Example

```csharp
// Set current timestamp in protobuf message
protoMessage.TimestampMs = ProtocolExtensions.NowUnixMs();

// Or use as a static import
using static ResQ.Protocols.ProtocolExtensions;
protoMessage.TimestampMs = NowUnixMs();
```

### Remarks
This is a convenience method equivalent to `DateTimeOffset.UtcNow.ToUnixTimeMilliseconds()`\.
It's commonly used when setting timestamp fields in protobuf messages\.
