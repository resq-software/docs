# Function: TelemetryProvider()

&gt; **TelemetryProvider**(`__namedParameters`): `Element`

Defined in: [react/telemetry-provider.tsx:58](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/react/telemetry-provider.tsx#L58)

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
