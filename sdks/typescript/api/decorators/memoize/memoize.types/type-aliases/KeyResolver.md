# Type Alias: KeyResolver

&gt; **KeyResolver** = (...`args`) =&gt; `string`

Defined in: [memoize/memoize.types.ts:43](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.types.ts#L43)

Resolves a cache key from a method's arguments.

The returned string is the cache identity: it must be deterministic and
collision-free for the inputs that should share (or not share) a cached value.
Two argument sets that map to the same string are treated as the same call, so
an over-broad resolver silently returns stale results.

## Parameters

### args

...`unknown`[]

The method arguments.

## Returns

`string`

The cache key; equal keys are treated as the same cached call.

## Example

```ts
const keyResolver: KeyResolver = (userId, includeDetails) =>
  `${userId}-${includeDetails}`;
```
