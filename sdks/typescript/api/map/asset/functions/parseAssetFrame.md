# Function: parseAssetFrame()

&gt; **parseAssetFrame**(`raw`): [`Asset`](../interfaces/Asset) \| `null`

Defined in: [asset.ts:93](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/asset.ts#L93)

Parse a telemetry frame into an [Asset](../interfaces/Asset), or `null` when it lacks an id
or a finite position.

## Parameters

### raw

`string` \| `Frame`

## Returns

[`Asset`](../interfaces/Asset) \| `null`

## Example

```ts
parseAssetFrame('{"drone_id":"UNIT-1","lat":38.9,"lon":-77,"heading_deg":120}');
// → { id: "UNIT-1", latitude: 38.9, longitude: -77, heading: 120 }
```
