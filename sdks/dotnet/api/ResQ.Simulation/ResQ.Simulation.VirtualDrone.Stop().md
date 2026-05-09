### [ResQ\.Simulation](ResQ.Simulation.md 'ResQ\.Simulation').[VirtualDrone](ResQ.Simulation.VirtualDrone.md 'ResQ\.Simulation\.VirtualDrone')

## VirtualDrone\.Stop\(\) Method

Stops the drone's telemetry loop\.

```csharp
public void Stop();
```

### Remarks
Signals the drone to stop sending telemetry\. The drone will complete its current
iteration and then exit the telemetry loop\.
