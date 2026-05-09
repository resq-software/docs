---
sidebarTitle: 'Velocity(double, double, double)'
---

### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[Velocity](./ResQ.Core.Velocity.md 'ResQ\.Core\.Velocity')

## Velocity\(double, double, double\) Constructor

Represents a velocity vector in NED \(North\-East\-Down\) coordinate frame\.

```csharp
public Velocity(double Vx, double Vy, double Vz);
```
#### Parameters

<a name='ResQ.Core.Velocity.Velocity(double,double,double).Vx'></a>

`Vx` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Velocity in North direction \(m/s\)\. Positive is North, negative is South\.

<a name='ResQ.Core.Velocity.Velocity(double,double,double).Vy'></a>

`Vy` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Velocity in East direction \(m/s\)\. Positive is East, negative is West\.

<a name='ResQ.Core.Velocity.Velocity(double,double,double).Vz'></a>

`Vz` [System\.Double](https://learn.microsoft.com/en-us/dotnet/api/system.double 'System\.Double')

Velocity in Down direction \(m/s\)\. Positive is Down, negative is Up\.

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
