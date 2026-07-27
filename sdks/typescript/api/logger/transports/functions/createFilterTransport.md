# Function: createFilterTransport()

&gt; **createFilterTransport**(`inner`, `predicate`): [`LogTransport`](../../logger.types/interfaces/LogTransport)

Defined in: [transports.ts:146](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/transports.ts#L146)

Wrap a transport so it only receives entries for which `predicate` is true —
a composable filter (Decorator over Observer). Compose with [byLevel](./byLevel)
for the common "only these levels" case.

The wrapper is transparent to the write channel: for a matching entry it
returns exactly what `inner.write` returns (forwarding its promise when the
inner transport is async); for a non-matching entry it returns `undefined`
without invoking `inner`. The wrapper is stateless — `predicate` owns any
state — and its `name` is derived as `filter(<inner.name>)`.

## Parameters

### inner

[`LogTransport`](../../logger.types/interfaces/LogTransport)

The transport that receives entries passing the predicate.

### predicate

(`entry`) =&gt; `boolean`

Returns `true` for entries that should reach `inner`.

## Returns

[`LogTransport`](../../logger.types/interfaces/LogTransport)

A transport that forwards only matching entries to `inner`.

## Example

```ts
Logger.addTransport(createFilterTransport(new JsonTransport(), byLevel("error", "warn")));
```
