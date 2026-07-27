# Interface: AssetMarkerProps

Defined in: [asset-marker.tsx:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/asset-marker.tsx#L38)

## Properties

### asset

&gt; **asset**: [`Asset`](../../asset/interfaces/Asset)

Defined in: [asset-marker.tsx:40](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/asset-marker.tsx#L40)

The asset to place.

***

### children?

&gt; `optional` **children?**: `ReactNode`

Defined in: [asset-marker.tsx:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/asset-marker.tsx#L48)

Custom marker content; replaces the default heading arrow.

***

### color?

&gt; `optional` **color?**: `string`

Defined in: [asset-marker.tsx:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/asset-marker.tsx#L44)

Fill colour of the default arrow.

***

### onSelect?

&gt; `optional` **onSelect?**: (`asset`) =&gt; `void`

Defined in: [asset-marker.tsx:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/asset-marker.tsx#L46)

Selection handler.

#### Parameters

##### asset

[`Asset`](../../asset/interfaces/Asset)

#### Returns

`void`

***

### size?

&gt; `optional` **size?**: `number`

Defined in: [asset-marker.tsx:42](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/map/src/asset-marker.tsx#L42)

Marker size in px (default 28).
