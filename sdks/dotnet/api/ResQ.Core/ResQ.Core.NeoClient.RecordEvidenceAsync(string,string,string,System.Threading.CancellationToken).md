---
sidebarTitle: 'RecordEvidenceAsync(string, string, string, CancellationToken)'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[NeoClient](./ResQ.Core.NeoClient.md 'ResQ\.Core\.NeoClient')

## NeoClient\.RecordEvidenceAsync\(string, string, string, CancellationToken\) Method

Records evidence linked to an incident on the blockchain\.

```csharp
public System.Threading.Tasks.Task<ResQ.Core.TransactionResult> RecordEvidenceAsync(string incidentId, string evidenceCid, string evidenceType, System.Threading.CancellationToken ct=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Core.NeoClient.RecordEvidenceAsync(string,string,string,System.Threading.CancellationToken).incidentId'></a>

`incidentId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The incident identifier\.

<a name='ResQ.Core.NeoClient.RecordEvidenceAsync(string,string,string,System.Threading.CancellationToken).evidenceCid'></a>

`evidenceCid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

IPFS CID of the evidence\.

<a name='ResQ.Core.NeoClient.RecordEvidenceAsync(string,string,string,System.Threading.CancellationToken).evidenceType'></a>

`evidenceType` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Type of evidence\.

<a name='ResQ.Core.NeoClient.RecordEvidenceAsync(string,string,string,System.Threading.CancellationToken).ct'></a>

`ct` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[TransactionResult](./ResQ.Core.TransactionResult.md 'ResQ\.Core\.TransactionResult')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
Transaction result\.
