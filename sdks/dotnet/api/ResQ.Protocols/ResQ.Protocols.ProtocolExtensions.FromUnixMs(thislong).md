### [ResQ\.Protocols](ResQ.Protocols.md 'ResQ\.Protocols').[ProtocolExtensions](ResQ.Protocols.ProtocolExtensions.md 'ResQ\.Protocols\.ProtocolExtensions')

## ProtocolExtensions\.FromUnixMs\(this long\) Method

Converts a Unix timestamp in milliseconds to a [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')\.

```csharp
public static System.DateTimeOffset FromUnixMs(this long timestampMs);
```
#### Parameters

<a name='ResQ.Protocols.ProtocolExtensions.FromUnixMs(thislong).timestampMs'></a>

`timestampMs` [System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')

The Unix timestamp in milliseconds since January 1, 1970 UTC\.

#### Returns
[System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')  
A [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset') representing the specified timestamp\.

### Example

```csharp
// From a protobuf timestamp field
long timestampMs = 1704067200000; // 2024-01-01 00:00:00 UTC
var dateTime = timestampMs.FromUnixMs();
Console.WriteLine(dateTime); // 2024-01-01 00:00:00 +00:00

// From current time
var now = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds().FromUnixMs();
```

### Remarks
This method handles the conversion from Unix time \(common in protobuf and JSON APIs\)
to \.NET's [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset') type\. The resulting value has UTC as its offset\.
