# Function: AirspeedIndicator()

&gt; **AirspeedIndicator**(`__namedParameters`): `Element`

Defined in: [packages/ui/src/components/airspeed-indicator/airspeed-indicator.tsx:199](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/airspeed-indicator/airspeed-indicator.tsx#L199)

Round pointer gauge (airspeed / generic telemetry dial).

## Parameters

### \_\_namedParameters

`Readonly`\<[`AirspeedIndicatorProps`](../interfaces/AirspeedIndicatorProps)\>

## Returns

`Element`

## Example

```tsx
<AirspeedIndicator
  speed={120}
  maxSpeed={200}
  bands={[{ from: 40, to: 140, tone: "normal" }, { from: 140, to: 180, tone: "caution" }]}
  redline={180}
/>
```
