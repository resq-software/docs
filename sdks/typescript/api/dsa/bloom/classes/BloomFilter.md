# Class: BloomFilter

Defined in: [bloom.ts:42](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/bloom.ts#L42)

Space-efficient probabilistic set membership test.

`has(x)` is guaranteed to return `true` for any item that was added; for
items that were *not* added it returns `true` with probability ≤ the
configured `errorRate` (false positives) and `false` otherwise (no false
negatives).

Bit array size `m` and hash count `k` are derived from `capacity` and
`errorRate` using the standard formulas:

- `m = ⌈ -n · ln(p) / (ln 2)² ⌉`
- `k = max(1, round((m / n) · ln 2))`

Hashing uses double FNV-1a with per-call seeds — no allocation per
`add`/`has` call.

## Example

```ts
const seen = new BloomFilter(100_000, 0.001); // 0.1% false-positive rate
seen.add("drone-04");
seen.has("drone-04"); // → true
seen.has("drone-99"); // → false (with high probability)
```

## Constructors

### Constructor

> **new BloomFilter**(`capacity`, `errorRate?`): `BloomFilter`

Defined in: [bloom.ts:55](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/bloom.ts#L55)

#### Parameters

##### capacity

`number`

Expected number of distinct items to insert. Memory
  use grows linearly with this value.

##### errorRate?

`number` = `0.01`

Target false-positive rate, in `(0, 1)`. Default
  `0.01` (1%). Smaller values increase memory and hash count.

#### Returns

`BloomFilter`

#### Throws

RangeError if `capacity <= 0` or `errorRate` is outside `(0, 1)`.

## Methods

### add()

> **add**(`item`): `void`

Defined in: [bloom.ts:82](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/bloom.ts#L82)

Mark `item` as present. Subsequent `has(item)` calls always return
`true`. Adding an item already present is a no-op.

#### Parameters

##### item

`string`

#### Returns

`void`

***

### has()

> **has**(`item`): `boolean`

Defined in: [bloom.ts:96](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/bloom.ts#L96)

Probabilistic membership test.

#### Parameters

##### item

`string`

#### Returns

`boolean`

`false` ⇒ the item was definitely never added.
         `true`  ⇒ the item was probably added (false-positive rate
         bounded by the constructor's `errorRate`).
