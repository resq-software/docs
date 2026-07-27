# Class: WeakCache\<K, V\>

Defined in: [weak-cache.ts:46](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/weak-cache.ts#L46)

A lazy, memoizing micro-cache keyed by objects and backed by a `WeakMap`.

Because storage is a `WeakMap`, an entry is eligible for garbage collection
as soon as its key object has no other references — there is no size bound,
no eviction policy, and no way to enumerate entries. This makes it ideal for
attaching derived data to objects you don't own, without leaking memory when
those objects go away. Keys must be objects (`WeakMap`'s constraint); values
are stored by reference, never copied or frozen.

## Example

```ts
const areas = new WeakCache<{ w: number; h: number }, number>();
const rect = { w: 4, h: 5 };
areas.get(rect, (r) => r.w * r.h); // → 20 (computed)
areas.get(rect, () => -1);         // → 20 (cached; callback not called)
```

## Type Parameters

### K

`K` *extends* `object`

The object key type. Constrained to `object` because `WeakMap`
  keys must be garbage-collectable references, not primitives.

### V

`V`

The cached value type.

## Constructors

### Constructor

&gt; **new WeakCache**\<`K`, `V`\>(): `WeakCache`\<`K`, `V`\>

#### Returns

`WeakCache`\<`K`, `V`\>

## Properties

### items

&gt; `readonly` **items**: `WeakMap`\<`K`, `V`\>

Defined in: [weak-cache.ts:51](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/weak-cache.ts#L51)

The backing `WeakMap`. Exposed for direct inspection; prefer [get](#get)
for the memoizing read path.

## Methods

### get()

&gt; **get**\<`P`\>(`item`, `cb`): `V`

Defined in: [weak-cache.ts:67](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/weak-cache.ts#L67)

Return the cached value for `item`, computing and storing it on first miss.

On a miss, `cb` is invoked exactly once and its result is cached; later
calls with the same key return the stored value without calling `cb`
again. Mutates the backing map as a side effect of caching a computed
value.

#### Type Parameters

##### P

`P` *extends* `object`

The concrete key subtype, preserved so `cb` receives `item`
  at its exact type rather than the widened `K`.

#### Parameters

##### item

`P`

The object key to read (and cache under on a miss).

##### cb

(`item`) =&gt; `V`

Loader invoked only on a miss to compute the value for `item`.

#### Returns

`V`

The cached value, or the value freshly computed by `cb`.
