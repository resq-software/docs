# Function: recover()

&gt; **recover**\<`T`, `E1`, `E2`\>(`fn`): (`result`) =&gt; `Result`\<`T`, `E2`\>

Defined in: [packages/helpers/src/helpers.ts:340](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L340)

Curried error-recovery combinator. Applies `fn` to the error of a
Failure, optionally lifting the pipeline back to a `Success`
with a different success type. Pass `Success` through unchanged.

## Type Parameters

### T

`T`

### E1

`E1`

### E2

`E2`

## Parameters

### fn

(`error`) =&gt; `Result`\<`T`, `E2`\>

Recovery handler: takes the original error, returns a new
  `Result` (success-with-fallback or different failure).

## Returns

A function `Result<T, E1> → Result<T, E2>`.

(`result`) =&gt; `Result`\<`T`, `E2`\>

## Example

**Fall back to a default**

```ts
const withFallback = recover<User, FetchError, never>((_err) =>
  success(GUEST_USER),
);
withFallback(failure(timeoutErr)); // → success(GUEST_USER)
```
