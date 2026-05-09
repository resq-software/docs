---
sidebarTitle: 'EvidenceRecord'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain')

## EvidenceRecord Class

Represents evidence metadata linked to IPFS storage\.

```csharp
public record EvidenceRecord : System.IEquatable<ResQ.Blockchain.EvidenceRecord>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; EvidenceRecord

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[EvidenceRecord](./ResQ.Blockchain.EvidenceRecord.md 'ResQ\.Blockchain\.EvidenceRecord')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

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

| Constructors | |
| :--- | :--- |
| [EvidenceRecord\(string, string, string, long, string\)](./ResQ.Blockchain.EvidenceRecord.EvidenceRecord(string,string,string,long,string).md 'ResQ\.Blockchain\.EvidenceRecord\.EvidenceRecord\(string, string, string, long, string\)') | Represents evidence metadata linked to IPFS storage\. |

| Properties | |
| :--- | :--- |
| [ContentType](./ResQ.Blockchain.EvidenceRecord.ContentType.md 'ResQ\.Blockchain\.EvidenceRecord\.ContentType') | MIME type of the evidence \(e\.g\., "image/jpeg", "video/mp4"\)\. |
| [Hash](./ResQ.Blockchain.EvidenceRecord.Hash.md 'ResQ\.Blockchain\.EvidenceRecord\.Hash') | Cryptographic hash of the evidence content for verification\. |
| [IncidentId](./ResQ.Blockchain.EvidenceRecord.IncidentId.md 'ResQ\.Blockchain\.EvidenceRecord\.IncidentId') | ID of the incident this evidence belongs to\. |
| [IpfsCid](./ResQ.Blockchain.EvidenceRecord.IpfsCid.md 'ResQ\.Blockchain\.EvidenceRecord\.IpfsCid') | IPFS Content Identifier for the evidence file\. |
| [SizeBytes](./ResQ.Blockchain.EvidenceRecord.SizeBytes.md 'ResQ\.Blockchain\.EvidenceRecord\.SizeBytes') | Size of the evidence file in bytes\. |
