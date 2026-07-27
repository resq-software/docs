# ~~Interface: ErrorResult\<E\>~~

Defined in: [packages/helpers/src/utils/control.ts:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L72)

Represents a failed result containing an error.

Interface for the error case of a Result type, containing the error information.
Used in conjunction with OkResult to create a discriminated union for error handling.

## Example

```ts
const failure: ErrorResult<string> = { ok: false, error: 'Something went wrong' }
if (!failure.ok) {
  console.error(failure.error) // 'Something went wrong'
}
```

## Deprecated

Superseded by success / failure from
`@resq-systems/helpers` (the `{ success, value }` Result). Not a drop-in: the
discriminant is renamed `ok` → `success` when migrating. This parallel
`{ ok, value }` type is unused; removed in the next major.

## Type Parameters

### E

`E`

## Properties

### ~~error~~

&gt; `readonly` **error**: `E`

Defined in: [packages/helpers/src/utils/control.ts:75](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L75)

***

### ~~ok~~

&gt; `readonly` **ok**: `false`

Defined in: [packages/helpers/src/utils/control.ts:74](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L74)

Discriminant marking the failure branch; always `false`. Narrow on this to reach [error](#error).
