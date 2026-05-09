### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\.ExtractIncidentId\(string\) Method

Extracts an incident ID from a JSON payload string\.

```csharp
private static string? ExtractIncidentId(string? payload);
```
#### Parameters

<a name='ResQ.Blockchain.MockNeoClient.ExtractIncidentId(string).payload'></a>

`payload` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The JSON payload to parse\.

#### Returns
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The extracted incident ID from "incidentId" or "incident" fields, or null if not found\.
