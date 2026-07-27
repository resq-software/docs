# Function: AssetMarker()

&gt; **AssetMarker**(`__namedParameters`): `Element`

Defined in: [asset-marker.tsx:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/asset-marker.tsx#L83)

Place an asset on the map.

## Parameters

### \_\_namedParameters

`Readonly`\<[`AssetMarkerProps`](../interfaces/AssetMarkerProps)\>

## Returns

`Element`

## Example

```tsx
<AssetMarker asset={asset} onSelect={setSelected} />
// richer: <AssetMarker asset={asset}><HeadingIndicator heading={asset.heading} className="size-10" /></AssetMarker>
```
