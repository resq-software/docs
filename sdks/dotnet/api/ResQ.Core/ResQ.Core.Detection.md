### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## Detection Class

Represents an AI detection result from drone sensors\.

```csharp
public record Detection : System.IEquatable<ResQ.Core.Detection>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; Detection

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[Detection](./ResQ.Core.Detection.md 'ResQ\.Core\.Detection')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var detection = new Detection
{
    DetectionId = "det-001",
    Type = DetectionType.Fire,
    Confidence = 0.95f,
    Location = new Location(37.7749, -122.4194),
    EvidenceCid = "Qmabc123..."
};
```

### Remarks
Detection records contain information about objects or phenomena identified
by the AI vision system, including location, confidence, and evidence links\.

| Properties | |
| :--- | :--- |
| [Confidence](./ResQ.Core.Detection.Confidence.md 'ResQ\.Core\.Detection\.Confidence') | AI confidence score \(0\.0 to 1\.0\)\. |
| [DetectedAt](./ResQ.Core.Detection.DetectedAt.md 'ResQ\.Core\.Detection\.DetectedAt') | UTC timestamp when the detection was made\. |
| [DetectionId](./ResQ.Core.Detection.DetectionId.md 'ResQ\.Core\.Detection\.DetectionId') | Unique identifier for this detection\. |
| [EvidenceCid](./ResQ.Core.Detection.EvidenceCid.md 'ResQ\.Core\.Detection\.EvidenceCid') | IPFS CID of the evidence file, if uploaded\. |
| [EvidenceUploaded](./ResQ.Core.Detection.EvidenceUploaded.md 'ResQ\.Core\.Detection\.EvidenceUploaded') | True if evidence has been uploaded to storage\. |
| [Location](./ResQ.Core.Detection.Location.md 'ResQ\.Core\.Detection\.Location') | Geographic location of the detection\. |
| [Type](./ResQ.Core.Detection.Type.md 'ResQ\.Core\.Detection\.Type') | Type of object or phenomenon detected\. |
