---
sidebarTitle: 'Velocity'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## Velocity Class

Represents a velocity vector in NED \(North\-East\-Down\) coordinate frame\.

```csharp
public record Velocity : System.IEquatable<ResQ.Core.Velocity>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') → Velocity

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[Velocity](./ResQ.Core.Velocity.md 'ResQ\.Core\.Velocity')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
// Drone moving North at 10 m/s, East at 5 m/s, and climbing at 2 m/s
var velocity = new Velocity(10.0, 5.0, -2.0);

// Calculate ground speed (ignoring altitude change)
double groundSpeed = Math.Sqrt(velocity.Vx * velocity.Vx + velocity.Vy * velocity.Vy);
```

### Remarks
The NED frame is a local tangent plane coordinate system commonly used in aviation
and robotics\. Positive X is North, positive Y is East, and positive Z is Down\.

| Constructors | |
| :--- | :--- |
| [Velocity\(double, double, double\)](./ResQ.Core.Velocity.Velocity(double,double,double).md 'ResQ\.Core\.Velocity\.Velocity\(double, double, double\)') | Represents a velocity vector in NED \(North\-East\-Down\) coordinate frame\. |

| Properties | |
| :--- | :--- |
| [Vx](./ResQ.Core.Velocity.Vx.md 'ResQ\.Core\.Velocity\.Vx') | Velocity in North direction \(m/s\)\. Positive is North, negative is South\. |
| [Vy](./ResQ.Core.Velocity.Vy.md 'ResQ\.Core\.Velocity\.Vy') | Velocity in East direction \(m/s\)\. Positive is East, negative is West\. |
| [Vz](./ResQ.Core.Velocity.Vz.md 'ResQ\.Core\.Velocity\.Vz') | Velocity in Down direction \(m/s\)\. Positive is Down, negative is Up\. |
