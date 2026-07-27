# Class: BloomFilter

Defined in: [bloom.ts:54](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/bloom.ts#L54)

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

&gt; **new BloomFilter**(`capacity`, `errorRate?`): `BloomFilter`

Defined in: [bloom.ts:70](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/bloom.ts#L70)

#### Parameters

##### capacity

`number`

Expected number of distinct items to insert. Memory
  use grows linearly with this value.

##### errorRate?

`number` & `Brand`\<`"Probability"`\>

Target false-positive rate as a branded
  [Probability](../../schemas/type-aliases/Probability) in `(0, 1)`. Omit to use the default `0.01` (1%).
  Construct one with `toProbability(...)` so an out-of-range value is
  rejected at the type level; the runtime check below still guards
  untrusted callers that reach this boundary via a cast.

#### Returns

`BloomFilter`

#### Throws

If `capacity <= 0` or `errorRate` is outside `(0, 1)`.

## Methods

### add()

&gt; **add**(`item`): `void`

Defined in: [bloom.ts:98](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/bloom.ts#L98)

Mark `item` as present. Subsequent `has(item)` calls always return
`true`. Adding an item already present is a no-op.

#### Parameters

##### item

`string`

#### Returns

`void`

***

### has()

&gt; **has**(`item`): `boolean`

Defined in: [bloom.ts:112](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/bloom.ts#L112)

Probabilistic membership test.

#### Parameters

##### item

`string`

#### Returns

`boolean`

`false` ⇒ the item was definitely never added.
         `true`  ⇒ the item was probably added (false-positive rate
         bounded by the constructor's `errorRate`).
