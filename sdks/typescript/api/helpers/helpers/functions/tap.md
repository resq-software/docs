# Function: tap()

&gt; **tap**\<`T`, `E`\>(`fn`): (`result`) =&gt; `Result`\<`T`, `E`\>

Defined in: [packages/helpers/src/helpers.ts:366](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L366)

Curried side-effect helper. On `Success`, invoke `fn(value)` for its
side effects and pass the result through unchanged. On `Failure`, do
nothing. The returned `Result` is identical to the input (same shape
and value identity).

Useful for instrumentation, logging, or analytics events sprinkled
through a pipeline without breaking the chain.

## Type Parameters

### T

`T`

### E

`E`

## Parameters

### fn

(`value`) =&gt; `void`

Side-effect callback; its return value is discarded.

## Returns

A function `Result<T, E> → Result<T, E>` (same `Result`).

(`result`) =&gt; `Result`\<`T`, `E`\>

## Example

```ts
pipe(
  parse(input),
  tap((parsed) => logger.debug("parsed", parsed)),
  bindResult(persist),
);
```
