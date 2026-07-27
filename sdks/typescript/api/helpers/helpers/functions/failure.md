# Function: failure()

&gt; **failure**\<`E`\>(`error`): `Failure`\<`E`\>

Defined in: [packages/helpers/src/helpers.ts:173](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L173)

Wrap an error in a Failure branch. The returned object is frozen
so consumers cannot mutate `success`/`error` after the fact.

## Type Parameters

### E

`E`

## Parameters

### error

`E`

The error value (any type — typically `Error`, but can be
  a plain string, code, or domain-specific type).

## Returns

`Failure`\<`E`\>

`{ success: false, error }` (frozen).
