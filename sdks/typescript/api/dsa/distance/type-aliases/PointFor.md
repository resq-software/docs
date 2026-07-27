# Type Alias: PointFor\<F\>

&gt; **PointFor**\<`F`\> = `F` *extends* `"threed"` ? [`Coordinates3D`](../interfaces/Coordinates3D) : [`Coordinates2D`](../interfaces/Coordinates2D)

Defined in: [distance.ts:104](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L104)

The point shape a given formula requires. Every formula operates on 2D
coordinates except `"threed"`, which needs an altitude component. Used to
make [Distance.calculate](../classes/Distance#calculate) reject 2D points for the 3D formula at the
type level.

## Type Parameters

### F

`F` *extends* [`DistanceFormula`](./DistanceFormula)
