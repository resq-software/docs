# Function: useAssetPositions()

&gt; **useAssetPositions**(): [`AssetPositions`](../interfaces/AssetPositions)

Defined in: [use-asset-positions.ts:49](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/use-asset-positions.ts#L49)

Track the latest position of every asset seen on the telemetry socket.

## Returns

[`AssetPositions`](../interfaces/AssetPositions)

## Example

```tsx
const { assets } = useAssetPositions();
return <TelemetryMap>{assets.map((a) => <AssetMarker key={a.id} asset={a} />)}</TelemetryMap>;
```
