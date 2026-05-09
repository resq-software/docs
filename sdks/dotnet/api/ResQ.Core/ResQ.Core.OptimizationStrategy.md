### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## OptimizationStrategy Class

Represents an optimization strategy from DTSOP \(Drone Tactical Strategy Optimization\)\.

```csharp
public record OptimizationStrategy : System.IEquatable<ResQ.Core.OptimizationStrategy>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; OptimizationStrategy

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[OptimizationStrategy](./ResQ.Core.OptimizationStrategy.md 'ResQ\.Core\.OptimizationStrategy')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var strategy = new OptimizationStrategy
{
    StrategyId = "strat-001",
    ScenarioId = "scen-001",
    EstimatedCoveragePercent = 85.5,
    EstimatedResponseTimeMinutes = 12.3,
    Deployments = new List<DeploymentRecommendation>
    {
        new() { DroneId = "drn-001", TargetPosition = location, MissionType = "Search", Priority = 1 }
    }
};
```

### Remarks
Optimization strategies provide recommended drone deployments, coverage estimates,
and response time predictions for disaster scenarios\.

| Properties | |
| :--- | :--- |
| [ConfidenceScore](./ResQ.Core.OptimizationStrategy.ConfidenceScore.md 'ResQ\.Core\.OptimizationStrategy\.ConfidenceScore') | Confidence score for this strategy \(0\.0 to 1\.0\)\. |
| [Deployments](./ResQ.Core.OptimizationStrategy.Deployments.md 'ResQ\.Core\.OptimizationStrategy\.Deployments') | List of recommended drone deployments\. |
| [EstimatedCoveragePercent](./ResQ.Core.OptimizationStrategy.EstimatedCoveragePercent.md 'ResQ\.Core\.OptimizationStrategy\.EstimatedCoveragePercent') | Estimated area coverage percentage\. |
| [EstimatedResponseTimeMinutes](./ResQ.Core.OptimizationStrategy.EstimatedResponseTimeMinutes.md 'ResQ\.Core\.OptimizationStrategy\.EstimatedResponseTimeMinutes') | Estimated response time in minutes\. |
| [GeneratedAt](./ResQ.Core.OptimizationStrategy.GeneratedAt.md 'ResQ\.Core\.OptimizationStrategy\.GeneratedAt') | UTC timestamp when the strategy was generated\. |
| [ScenarioId](./ResQ.Core.OptimizationStrategy.ScenarioId.md 'ResQ\.Core\.OptimizationStrategy\.ScenarioId') | ID of the scenario this strategy applies to\. |
| [StrategyId](./ResQ.Core.OptimizationStrategy.StrategyId.md 'ResQ\.Core\.OptimizationStrategy\.StrategyId') | Unique identifier for this strategy\. |
