### [ResQ\.Core](./ResQ.Core.md 'ResQ\.Core').[ResQExtensions](./ResQ.Core.ResQExtensions.md 'ResQ\.Core\.ResQExtensions')

## ResQExtensions\.IsCritical\(this Detection\) Method

Determines if a detection is critical and requires immediate action\.

```csharp
public static bool IsCritical(this ResQ.Core.Detection detection);
```
#### Parameters

<a name='ResQ.Core.ResQExtensions.IsCritical(thisResQ.Core.Detection).detection'></a>

`detection` [Detection](./ResQ.Core.Detection.md 'ResQ\.Core\.Detection')

The detection to evaluate\.

#### Returns
[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')  
True if the detection is critical\.

### Remarks
A detection is considered critical if it has high confidence \(\>= 0\.85\)
and is of a critical type \(Fire, Person, or Flood\)\.
