### [ResQ\.Core](ResQ.Core.md 'ResQ\.Core')

## TelemetryPacket Class

Represents a complete telemetry packet from a drone\.

```csharp
public record TelemetryPacket : System.IEquatable<ResQ.Core.TelemetryPacket>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; TelemetryPacket

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[TelemetryPacket](ResQ.Core.TelemetryPacket.md 'ResQ\.Core\.TelemetryPacket')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var telemetry = new TelemetryPacket
{
    DroneId = "drn-001",
    SequenceNumber = 12345,
    Position = new Location(37.7749, -122.4194, 100.0),
    Velocity = new Velocity(10.0, 5.0, -1.0),
    Status = DroneStatus.InFlight,
    BatteryPercent = 75.5f,
    Detections = new List<Detection>()
};
```

### Remarks
This record contains comprehensive telemetry data from a drone including
position, velocity, status, battery levels, sensor health, and mission
progress\. It is used for real\-time monitoring and logging\.

| Properties | |
| :--- | :--- |
| [BatteryPercent](ResQ.Core.TelemetryPacket.BatteryPercent.md 'ResQ\.Core\.TelemetryPacket\.BatteryPercent') | Battery level as percentage \(0\-100\)\. |
| [BatteryVoltage](ResQ.Core.TelemetryPacket.BatteryVoltage.md 'ResQ\.Core\.TelemetryPacket\.BatteryVoltage') | Battery voltage in volts\. |
| [CameraOk](ResQ.Core.TelemetryPacket.CameraOk.md 'ResQ\.Core\.TelemetryPacket\.CameraOk') | True if camera is functioning normally\. |
| [CurrentMissionId](ResQ.Core.TelemetryPacket.CurrentMissionId.md 'ResQ\.Core\.TelemetryPacket\.CurrentMissionId') | ID of the current mission, if any\. |
| [Detections](ResQ.Core.TelemetryPacket.Detections.md 'ResQ\.Core\.TelemetryPacket\.Detections') | List of AI detections from this telemetry packet\. |
| [DroneId](ResQ.Core.TelemetryPacket.DroneId.md 'ResQ\.Core\.TelemetryPacket\.DroneId') | Unique identifier for the drone\. |
| [GpsOk](ResQ.Core.TelemetryPacket.GpsOk.md 'ResQ\.Core\.TelemetryPacket\.GpsOk') | True if GPS is functioning normally\. |
| [ImuOk](ResQ.Core.TelemetryPacket.ImuOk.md 'ResQ\.Core\.TelemetryPacket\.ImuOk') | True if IMU is functioning normally\. |
| [MissionProgressPercent](ResQ.Core.TelemetryPacket.MissionProgressPercent.md 'ResQ\.Core\.TelemetryPacket\.MissionProgressPercent') | Mission completion percentage \(0\-100\)\. |
| [Position](ResQ.Core.TelemetryPacket.Position.md 'ResQ\.Core\.TelemetryPacket\.Position') | Current geographic position of the drone\. |
| [SequenceNumber](ResQ.Core.TelemetryPacket.SequenceNumber.md 'ResQ\.Core\.TelemetryPacket\.SequenceNumber') | Sequence number for ordering telemetry packets\. |
| [Status](ResQ.Core.TelemetryPacket.Status.md 'ResQ\.Core\.TelemetryPacket\.Status') | Current operational status\. |
| [SwarmId](ResQ.Core.TelemetryPacket.SwarmId.md 'ResQ\.Core\.TelemetryPacket\.SwarmId') | Optional swarm identifier if the drone is part of a swarm\. |
| [ThermalOk](ResQ.Core.TelemetryPacket.ThermalOk.md 'ResQ\.Core\.TelemetryPacket\.ThermalOk') | True if thermal sensor is functioning normally\. |
| [Timestamp](ResQ.Core.TelemetryPacket.Timestamp.md 'ResQ\.Core\.TelemetryPacket\.Timestamp') | UTC timestamp when the telemetry was recorded\. |
| [Velocity](ResQ.Core.TelemetryPacket.Velocity.md 'ResQ\.Core\.TelemetryPacket\.Velocity') | Current velocity vector in NED frame\. |
