# Interface: DistanceOptions

Defined in: [distance.ts:112](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/distance.ts#L112)

Options for distance calculations.

## Properties

### p?

&gt; `optional` **p?**: `number`

Defined in: [distance.ts:120](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/distance.ts#L120)

Minkowski norm order. Must be strictly positive (`> 0`); `Infinity` is
accepted and yields Chebyshev distance. Defaults to `2` when omitted.
- p=1: Manhattan distance
- p=2: Euclidean distance
- p=Infinity: Chebyshev distance
