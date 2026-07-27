# Function: delegateFn()

&gt; **delegateFn**\<`D`, `A`\>(`originalMethod`, `keyResolver?`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [delegate/delegate.fn.ts:74](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/delegate/delegate.fn.ts#L74)

Wraps an async method to deduplicate concurrent calls.
Multiple calls with the same key will share the same promise
until the first one completes.

Keeps a per-wrapper `Map` of in-flight promises keyed by `keyResolver` (or, by
default, `JSON.stringify(args)`). The entry is removed via `.finally` once the
promise **settles** — resolve *or* reject — so dedup only spans overlapping
in-flight calls; a call after settlement re-invokes the method. Concurrent
callers sharing a key share its fate: one rejection rejects them all. Distinct
keys never dedup. There is no `AbortSignal` support and no ordering guarantee
across keys.

The key is computed **synchronously** before the method is called, so a
throwing key generator (the default `JSON.stringify` on a circular or `BigInt`
argument, or a custom `keyResolver` that throws) propagates as a synchronous
exception, not a rejected promise. Failures from `originalMethod` itself are
rejected promises.

## Type Parameters

### D

`D` = `unknown`

The resolved type of the promise.

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method.

## Parameters

### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The async method to wrap.

### keyResolver?

(...`args`) =&gt; `string`

Optional function to generate cache keys from arguments.

## Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The delegated method that shares in-flight promises by key.

## Throws

Synchronously, when the default key generator cannot
  `JSON.stringify` the arguments (circular reference or `BigInt`).

## Example

```typescript
class Service {
  async fetchData(id: string): Promise<Data> {
    console.log(`Fetching ${id}`);
    return fetch(`/api/data/${id}`).then(r => r.json());
  }
}

const service = new Service();
const delegated = delegateFn(
  service.fetchData.bind(service),
  (id) => id // Use id directly as key
);

// These share the same promise - "Fetching 123" is logged only once
const p1 = delegated('123');
const p2 = delegated('123');
const [d1, d2] = await Promise.all([p1, p2]);
```
