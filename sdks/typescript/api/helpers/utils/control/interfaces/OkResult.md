# ~~Interface: OkResult\<T\>~~

Defined in: [packages/helpers/src/utils/control.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L48)

Represents a successful result containing a value.

Interface for the success case of a Result type, containing the computed value.
Used in conjunction with ErrorResult to create a discriminated union for error handling.

## Example

```ts
const success: OkResult<string> = { ok: true, value: 'Hello World' }
if (success.ok) {
  console.log(success.value) // 'Hello World'
}
```

## Deprecated

Superseded by success / failure from
`@resq-systems/helpers` (the `{ success, value }` Result). Not a drop-in: the
discriminant is renamed `ok` → `success` when migrating. This parallel
`{ ok, value }` type is unused; removed in the next major.

## Type Parameters

### T

`T`

## Properties

### ~~ok~~

&gt; `readonly` **ok**: `true`

Defined in: [packages/helpers/src/utils/control.ts:50](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L50)

Discriminant marking the success branch; always `true`. Narrow on this to reach [value](#value).

***

### ~~value~~

&gt; `readonly` **value**: `T`

Defined in: [packages/helpers/src/utils/control.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L51)
