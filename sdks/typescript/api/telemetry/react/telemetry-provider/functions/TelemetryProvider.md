# Function: TelemetryProvider()

&gt; **TelemetryProvider**(`__namedParameters`): `Element`

Defined in: [react/telemetry-provider.tsx:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/react/telemetry-provider.tsx#L58)

Provide a single reconnecting telemetry socket to the subtree.

## Parameters

### \_\_namedParameters

`Readonly`\<[`TelemetryProviderProps`](../interfaces/TelemetryProviderProps)\>

## Returns

`Element`

## Example

```tsx
<TelemetryProvider url="wss://host/fleet/ws">
  <FleetMap />
</TelemetryProvider>
```
