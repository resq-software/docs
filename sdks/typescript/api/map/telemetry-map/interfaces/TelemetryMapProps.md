# Interface: TelemetryMapProps

Defined in: [telemetry-map.tsx:35](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L35)

## Properties

### children?

&gt; `optional` **children?**: `ReactNode`

Defined in: [telemetry-map.tsx:49](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L49)

Markers, sources, and layers.

***

### cursor?

&gt; `optional` **cursor?**: `string`

Defined in: [telemetry-map.tsx:43](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L43)

CSS cursor over the canvas.

***

### initialViewState?

&gt; `optional` **initialViewState?**: `object`

Defined in: [telemetry-map.tsx:39](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L39)

Initial camera.

#### latitude

&gt; **latitude**: `number`

#### longitude

&gt; **longitude**: `number`

#### zoom

&gt; **zoom**: `number`

***

### interactive?

&gt; `optional` **interactive?**: `boolean`

Defined in: [telemetry-map.tsx:41](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L41)

Disable pan/zoom for a static display.

***

### mapStyle?

&gt; `optional` **mapStyle?**: `string`

Defined in: [telemetry-map.tsx:37](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L37)

Basemap style URL; falls back to a token-free dark basemap.

***

### onClick?

&gt; `optional` **onClick?**: (`event`) =&gt; `void`

Defined in: [telemetry-map.tsx:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L45)

Map click handler.

#### Parameters

##### event

###### lngLat

\{ `lat`: `number`; `lng`: `number`; \}

###### lngLat.lat

`number`

###### lngLat.lng

`number`

#### Returns

`void`

***

### style?

&gt; `optional` **style?**: `CSSProperties`

Defined in: [telemetry-map.tsx:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/telemetry-map.tsx#L47)

Container style; defaults to filling the positioned parent.
