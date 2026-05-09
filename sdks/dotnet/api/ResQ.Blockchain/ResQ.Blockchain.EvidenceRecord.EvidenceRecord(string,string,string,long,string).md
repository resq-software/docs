### [ResQ\.Blockchain](ResQ.Blockchain.md 'ResQ\.Blockchain').[EvidenceRecord](ResQ.Blockchain.EvidenceRecord.md 'ResQ\.Blockchain\.EvidenceRecord')

## EvidenceRecord\(string, string, string, long, string\) Constructor

Represents evidence metadata linked to IPFS storage\.

```csharp
public EvidenceRecord(string IncidentId, string IpfsCid, string ContentType, long SizeBytes, string Hash);
```
#### Parameters

<a name='ResQ.Blockchain.EvidenceRecord.EvidenceRecord(string,string,string,long,string).IncidentId'></a>

`IncidentId` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

ID of the incident this evidence belongs to\.

<a name='ResQ.Blockchain.EvidenceRecord.EvidenceRecord(string,string,string,long,string).IpfsCid'></a>

`IpfsCid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

IPFS Content Identifier for the evidence file\.

<a name='ResQ.Blockchain.EvidenceRecord.EvidenceRecord(string,string,string,long,string).ContentType'></a>

`ContentType` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

MIME type of the evidence \(e\.g\., "image/jpeg", "video/mp4"\)\.

<a name='ResQ.Blockchain.EvidenceRecord.EvidenceRecord(string,string,string,long,string).SizeBytes'></a>

`SizeBytes` [System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')

Size of the evidence file in bytes\.

<a name='ResQ.Blockchain.EvidenceRecord.EvidenceRecord(string,string,string,long,string).Hash'></a>

`Hash` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

Cryptographic hash of the evidence content for verification\.

### Example

```csharp
var evidence = new EvidenceRecord(
    IncidentId: "inc-001",
    IpfsCid: "Qmabc123...",
    ContentType: "image/jpeg",
    SizeBytes: 1024567,
    Hash: "sha256:..."
);

var result = await neoClient.RecordEvidenceAsync(evidence);
```

### Remarks
Evidence records link incidents to their associated evidence stored on IPFS\.
The hash field provides a content verification mechanism to ensure evidence
integrity when retrieved from IPFS\.
