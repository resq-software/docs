# Interface: MemoizeConfig\<T, D\>

Defined in: [memoize/memoize.types.ts:94](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize/memoize.types.ts#L94)

Configuration for the `@memoize` decorator and memoizeFn.

## Example

```ts
const config: MemoizeConfig<MyService, User> = {
  cache: new LRUCache<string, User>(100),
  keyResolver: (id) => `user-${id}`,
  expirationTimeMs: 300000, // Five minutes.
};
```

## Type Parameters

### T

`T`

The class type a `keyof T` key resolver resolves against.

### D

`D`

The return type of the decorated method.

## Properties

### cache?

&gt; `optional` **cache?**: [`Cache`](./Cache)\<`D`\>

Defined in: [memoize/memoize.types.ts:96](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize/memoize.types.ts#L96)

Custom cache; when omitted, a fresh `Map` is used.

***

### expirationTimeMs?

&gt; `optional` **expirationTimeMs?**: `number`

Defined in: [memoize/memoize.types.ts:107](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize/memoize.types.ts#L107)

Per-entry time-to-live in milliseconds, measured from insertion (not refreshed
on read). When omitted, entries never expire.

***

### keyResolver?

&gt; `optional` **keyResolver?**: [`KeyResolver`](../type-aliases/KeyResolver) \| keyof `T`

Defined in: [memoize/memoize.types.ts:102](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize/memoize.types.ts#L102)

How cache keys are derived. A [KeyResolver](../type-aliases/KeyResolver) is called with the
arguments; a `keyof T` names an instance method resolved and bound to `this`
at call time. When omitted, the key is `JSON.stringify` of the arguments.
