# Function: TelemetryMap()

&gt; **TelemetryMap**(`__namedParameters`): `Element`

Defined in: [telemetry-map.tsx:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L64)

Dark telemetry basemap shell.

## Parameters

### \_\_namedParameters

`Readonly`\<[`TelemetryMapProps`](../interfaces/TelemetryMapProps)\>

## Returns

`Element`

## Example

```tsx
<div style={{ position: "relative", height: 480 }}>
  <TelemetryMap initialViewState={{ longitude: -98.5, latitude: 39.8, zoom: 3.6 }}>
    <AssetMarker asset={asset} />
  </TelemetryMap>
</div>
```
