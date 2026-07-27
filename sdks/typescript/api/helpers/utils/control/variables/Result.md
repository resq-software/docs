# ~~Variable: Result~~

&gt; **Result**: `object`

Defined in: [packages/helpers/src/utils/control.ts:108](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L108)

Utility object for creating Result instances.

Provides factory methods for creating OkResult and ErrorResult instances.
This is the preferred way to construct Result values for consistent structure.

## Type Declaration

### ~~all()~~

&gt; **all**\<`T`, `E`\>(`results`): [`Result`](../type-aliases/Result)\<`T`[], `E`\>

Create a successful result containing an array of values.

Short-circuits: iteration stops at the first [ErrorResult](../interfaces/ErrorResult), which is
returned as-is (same reference), so later results are neither inspected nor
collected. Values preserve input order.

#### Type Parameters

##### T

`T`

##### E

`E`

#### Parameters

##### results

readonly [`Result`](../type-aliases/Result)\<`T`, `E`\>[]

The array of results to wrap

#### Returns

[`Result`](../type-aliases/Result)\<`T`[], `E`\>

An [OkResult](../interfaces/OkResult) of all values in order, or the first
  [ErrorResult](../interfaces/ErrorResult) encountered.

### ~~err()~~

&gt; **err**\<`E`\>(`error`): [`ErrorResult`](../interfaces/ErrorResult)\<`E`\>

Create a failed result containing an error.

#### Type Parameters

##### E

`E`

#### Parameters

##### error

`E`

The error value to wrap

#### Returns

[`ErrorResult`](../interfaces/ErrorResult)\<`E`\>

An ErrorResult containing the error

### ~~ok()~~

&gt; **ok**\<`T`\>(`value`): [`OkResult`](../interfaces/OkResult)\<`T`\>

Create a successful result containing a value.

#### Type Parameters

##### T

`T`

#### Parameters

##### value

`T`

The success value to wrap

#### Returns

[`OkResult`](../interfaces/OkResult)\<`T`\>

An OkResult containing the value

## Example

```ts
// Create success result
const success = Result.ok(42)
// success: OkResult<number> = { ok: true, value: 42 }

// Create error result
const failure = Result.err('Invalid input')
// failure: ErrorResult<string> = { ok: false, error: 'Invalid input' }
```

## Deprecated

Superseded by success / failure from
`@resq-systems/helpers`. Not a drop-in: the discriminant is renamed
`ok` → `success` when migrating. This parallel `{ ok, value }` Result factory
is unused; removed in the next major.
