# Class: CountMinSketch

Defined in: [count-min.ts:46](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/count-min.ts#L46)

Sub-linear-memory frequency estimator.

Estimates the number of times a string has been observed using
`O(width × depth)` memory regardless of the cardinality of the keyspace.
Estimates satisfy `estimate(x) ≥ trueCount(x)` and, with probability
`≥ 1 − delta`, `estimate(x) ≤ trueCount(x) + epsilon · totalCount`.

Parameters:
- `width = ⌈ e / epsilon ⌉` (columns per row)
- `depth = ⌈ ln(1 / delta) ⌉`  (independent hash rows)

## Example

```ts
const sketch = new CountMinSketch(0.001, 0.01); // ~2718 × 5
for (const ip of requests) sketch.increment(ip);
sketch.estimate("203.0.113.7"); // approximate count
```

## Constructors

### Constructor

&gt; **new CountMinSketch**(`epsilon`, `delta`): `CountMinSketch`

Defined in: [count-min.ts:61](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/count-min.ts#L61)

#### Parameters

##### epsilon

`number` & `Brand`\<`"Probability"`\>

Additive error bound as a branded [Probability](../../schemas/type-aliases/Probability)
  in `(0, 1)`. Smaller ⇒ more memory, tighter estimates. Construct with
  `toProbability(...)` so an out-of-range value is rejected at the type
  level; the runtime check below still guards untrusted callers.

##### delta

`number` & `Brand`\<`"Probability"`\>

Probability that the error bound is exceeded, as a branded
  [Probability](../../schemas/type-aliases/Probability) in `(0, 1)`. Smaller ⇒ more rows.

#### Returns

`CountMinSketch`

#### Throws

If either parameter is outside `(0, 1)`.

## Methods

### estimate()

&gt; **estimate**(`key`): `number`

Defined in: [count-min.ts:105](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/count-min.ts#L105)

#### Parameters

##### key

`string`

#### Returns

`number`

An over-estimate of the number of times `key` has been
  incremented. Never returns less than the true count.

***

### increment()

&gt; **increment**(`key`, `count?`): `void`

Defined in: [count-min.ts:93](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/count-min.ts#L93)

Add `count` to the running tally for `key`. Mutates the sketch in place.

Counters live in unsigned 32-bit lanes, so a tally that passes
`2³² − 1` wraps around rather than saturating.

#### Parameters

##### key

`string`

The item being counted.

##### count?

`number` = `1`

Increment amount; defaults to `1`. Negative counts are
  permitted but break the upper-bound guarantee (and can wrap a lane to a
  large value).

#### Returns

`void`
