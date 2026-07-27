# Function: rng()

&gt; **rng**(`seed?`): () =&gt; `number`

Defined in: [packages/math/src/utils.ts:81](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/utils.ts#L81)

Create a seeded pseudo-random number generator using xorshift.

The same seed always yields the same sequence, which makes it suitable for
reproducible tests and deterministic sampling. Each call to the returned
function produces a value in `[-1, 1)`. Adapted from seedrandom.

`rng` itself is pure. The **returned** generator is stateful: it holds mutable
internal state and advances it on every call, so calls are order-dependent and
one generator cannot back two independent streams — mint a separate generator
per stream.

## Parameters

### seed?

`string` = `""`

Seed string; the empty default still produces a stable sequence.

## Returns

A stateful generator that returns the next number on each call.

() =&gt; `number`

## Example

```ts
const next = rng("seed");
next(); // → deterministic value in [-1, 1)
```
