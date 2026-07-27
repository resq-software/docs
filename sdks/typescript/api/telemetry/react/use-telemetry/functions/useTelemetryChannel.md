# Function: useTelemetryChannel()

&gt; **useTelemetryChannel**(`subscription`): [`TelemetryChannel`](../interfaces/TelemetryChannel)

Defined in: [react/use-telemetry.ts:61](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/react/use-telemetry.ts#L61)

Attach handlers to the shared socket for the lifetime of the component and
get a `send` bound to it. Handlers are read through a ref so passing fresh
closures each render never re-subscribes.

## Parameters

### subscription

`Readonly`\<[`TelemetrySubscription`](../../../types/interfaces/TelemetrySubscription)\>

## Returns

[`TelemetryChannel`](../interfaces/TelemetryChannel)

## Example

```tsx
const ops = useTelemetryChannel({
  onOpen: () => ops.send("subscribe:ops"),
  onMessage: (raw) => applyOps(JSON.parse(raw)),
});
```
