### [ResQ\.Protocols](./ResQ.Protocols.md 'ResQ\.Protocols')

## AlertSeverity Enum

Defines severity levels for alerts and events in the ResQ system\.

```csharp
public enum AlertSeverity
```
### Fields

<a name='ResQ.Protocols.AlertSeverity.Low'></a>

`Low` 0

Low severity \- routine information or minor issues\.

<a name='ResQ.Protocols.AlertSeverity.Medium'></a>

`Medium` 1

Medium severity \- notable events that may require attention\.

<a name='ResQ.Protocols.AlertSeverity.High'></a>

`High` 2

High severity \- significant issues requiring prompt response\.

<a name='ResQ.Protocols.AlertSeverity.Critical'></a>

`Critical` 3

Critical severity \- urgent issues requiring immediate action\.

### Example

```csharp
// Create an alert with severity
var alert = new Alert
{
    Severity = AlertSeverity.High,
    Message = "Fire detected in sector 7"
};

// Convert from risk score
double riskScore = 0.85;
var severity = riskScore >= 0.9 ? AlertSeverity.Critical :
               riskScore >= 0.75 ? AlertSeverity.High :
               riskScore >= 0.6 ? AlertSeverity.Medium :
               AlertSeverity.Low;
```

### Remarks
These severity levels are used throughout the system to classify the urgency
and importance of alerts, incidents, and events\. They map to protocol buffer
enum values and are ordered from lowest \(Low\) to highest \(Critical\) severity\.


When converting from risk scores or confidence values, use the following thresholds:
- Critical: Risk score >= 0.9 or confidence >= 0.95
- High: Risk score >= 0.75 or confidence >= 0.85
- Medium: Risk score >= 0.6 or confidence >= 0.7
- Low: Risk score < 0.6 or confidence < 0.7
