---
sidebarTitle: 'DeploymentRecommendation'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## DeploymentRecommendation Class

Represents a single drone deployment recommendation\.

```csharp
public record DeploymentRecommendation : System.IEquatable<ResQ.Core.DeploymentRecommendation>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → DeploymentRecommendation

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[DeploymentRecommendation](./ResQ.Core.DeploymentRecommendation.md 'ResQ\.Core\.DeploymentRecommendation')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var deployment = new DeploymentRecommendation
{
    DroneId = "drn-001",
    TargetPosition = new Location(37.7749, -122.4194),
    MissionType = "Search",
    Priority = 1,
    Rationale = "High probability survivor location"
};
```

### Remarks
Part of an optimization strategy, specifying which drone should be deployed
where and for what mission\.

| Properties | |
| :--- | :--- |
| [DroneId](./ResQ.Core.DeploymentRecommendation.DroneId.md 'ResQ\.Core\.DeploymentRecommendation\.DroneId') | ID of the drone to deploy\. |
| [MissionType](./ResQ.Core.DeploymentRecommendation.MissionType.md 'ResQ\.Core\.DeploymentRecommendation\.MissionType') | Type of mission to execute\. |
| [Priority](./ResQ.Core.DeploymentRecommendation.Priority.md 'ResQ\.Core\.DeploymentRecommendation\.Priority') | Priority level \(lower number = higher priority\)\. |
| [Rationale](./ResQ.Core.DeploymentRecommendation.Rationale.md 'ResQ\.Core\.DeploymentRecommendation\.Rationale') | Explanation for this recommendation\. |
| [TargetPosition](./ResQ.Core.DeploymentRecommendation.TargetPosition.md 'ResQ\.Core\.DeploymentRecommendation\.TargetPosition') | Target position for deployment\. |
