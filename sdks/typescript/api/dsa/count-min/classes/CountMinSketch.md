# Class: CountMinSketch

Defined in: [count-min.ts:39](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/count-min.ts#L39)

Sub-linear-memory frequency estimator.

Estimates the number of times a string has been observed using
`O(width × depth)` memory regardless of the cardinality of the keyspace.
Estimates satisfy `estimate(x) ≥ trueCount(x)` and, with probability
`≥ 1 − delta`, `estimate(x) ≤ trueCount(x) + epsilon · totalCount`.

Parameters:
- `width = ⌈ e / epsilon ⌉` (columns per row)
- `depth = ⌈ ln(1 / delta) ⌉`  (independent hash rows)

Use cases: heavy-hitter detection, request-rate estimation, log-rollup
counts where exact counts are not affordable.

## Example

```ts
const sketch = new CountMinSketch(0.001, 0.01); // ~2718 × 5
for (const ip of requests) sketch.increment(ip);
sketch.estimate("203.0.113.7"); // approximate count
```

## Constructors

### Constructor

> **new CountMinSketch**(`epsilon`, `delta`): `CountMinSketch`

Defined in: [count-min.ts:52](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/count-min.ts#L52)

#### Parameters

##### epsilon

`number`

Additive error bound, in `(0, 1)`. Smaller ⇒ more
  memory, tighter estimates.

##### delta

`number`

Probability that the error bound is exceeded, in
  `(0, 1)`. Smaller ⇒ more rows.

#### Returns

`CountMinSketch`

#### Throws

RangeError if either parameter is outside `(0, 1)`.

## Methods

### estimate()

> **estimate**(`key`): `number`

Defined in: [count-min.ts:92](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/count-min.ts#L92)

#### Parameters

##### key

`string`

#### Returns

`number`

An over-estimate of the number of times `key` has been
  incremented. Never returns less than the true count.

***

### increment()

> **increment**(`key`, `count?`): `void`

Defined in: [count-min.ts:80](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/count-min.ts#L80)

Add `count` to the running tally for `key`.

#### Parameters

##### key

`string`

The item being counted.

##### count?

`number` = `1`

Increment amount; defaults to `1`. Negative counts are
  permitted but break the upper-bound guarantee.

#### Returns

`void`
