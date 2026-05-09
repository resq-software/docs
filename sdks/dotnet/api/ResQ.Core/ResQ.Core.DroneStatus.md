### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core')

## DroneStatus Enum

Represents the operational status of a drone\.

```csharp
public enum DroneStatus
```
### Fields

<a name='ResQ.Core.DroneStatus.Idle'></a>

`Idle` 0

Drone is powered on and ready but not armed\.

<a name='ResQ.Core.DroneStatus.Armed'></a>

`Armed` 1

Drone is armed and ready for takeoff\.

<a name='ResQ.Core.DroneStatus.Takeoff'></a>

`Takeoff` 2

Drone is currently taking off\.

<a name='ResQ.Core.DroneStatus.InFlight'></a>

`InFlight` 3

Drone is airborne and executing its mission\.

<a name='ResQ.Core.DroneStatus.Returning'></a>

`Returning` 4

Drone is returning to home/base location\.

<a name='ResQ.Core.DroneStatus.Landing'></a>

`Landing` 5

Drone is currently landing\.

<a name='ResQ.Core.DroneStatus.Landed'></a>

`Landed` 6

Drone has successfully landed\.

<a name='ResQ.Core.DroneStatus.Emergency'></a>

`Emergency` 7

Drone has encountered an emergency situation\.

<a name='ResQ.Core.DroneStatus.Offline'></a>

`Offline` 8

Drone is offline or not responding\.

### Example

```csharp
if (drone.Status == DroneStatus.InFlight)
{
    // Monitor mission progress
}
else if (drone.Status == DroneStatus.Emergency)
{
    // Alert operators
}
```

### Remarks
These statuses represent the drone's current operational state within its
mission lifecycle\. State transitions are typically managed by the flight
controller and mission management system\.
