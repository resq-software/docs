# Function: toTrackGeoJSON()

&gt; **toTrackGeoJSON**(`points`): `FeatureCollection`\<`LineString`\>

Defined in: [track.ts:37](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/track.ts#L37)

Convert ordered positions into a GeoJSON `FeatureCollection` with a single
`LineString` feature, suitable for a react-map-gl `<Source type="geojson">`.

## Parameters

### points

readonly [`LngLat`](../interfaces/LngLat)[]

## Returns

`FeatureCollection`\<`LineString`\>
