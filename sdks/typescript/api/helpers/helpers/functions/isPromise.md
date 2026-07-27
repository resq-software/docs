# Function: isPromise()

&gt; **isPromise**(`value`): `value is Promise<unknown>`

Defined in: [packages/helpers/src/helpers.ts:434](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L434)

Type guard: narrow `unknown` to a `PromiseLike` / `Promise`.

Uses Promises/A+ duck-typing (presence of a callable `.then`) rather
than `instanceof Promise` so it works across realm boundaries
(iframes, workers) and with custom thenables.

## Parameters

### value

`unknown`

The value to test.

## Returns

`value is Promise<unknown>`

## Example

```ts
const v = maybeAsync();
const value = isPromise(v) ? await v : v;
```
