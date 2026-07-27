# Interface: Coordinates3D

Defined in: [distance.ts:92](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L92)

3D coordinates with latitude, longitude, and altitude.

## Extends

- [`Coordinates2D`](./Coordinates2D)

## Properties

### alt

&gt; **alt**: `number`

Defined in: [distance.ts:94](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L94)

Altitude in meters

***

### lat

&gt; **lat**: `number` & `Brand`\<`"Latitude"`\>

Defined in: [distance.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L83)

Latitude in degrees, branded to `[-90, 90]` — see [Latitude](../../schemas/type-aliases/Latitude).

#### Inherited from

[`Coordinates2D`](./Coordinates2D).[`lat`](./Coordinates2D#lat)

***

### lng

&gt; **lng**: `number` & `Brand`\<`"Longitude"`\>

Defined in: [distance.ts:85](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L85)

Longitude in degrees, branded to `[-180, 180]` — see [Longitude](../../schemas/type-aliases/Longitude).

#### Inherited from

[`Coordinates2D`](./Coordinates2D).[`lng`](./Coordinates2D#lng)
