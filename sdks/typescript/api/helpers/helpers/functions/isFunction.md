# Function: isFunction()

&gt; **isFunction**(`value`): `value is (args: unknown[]) => unknown`

Defined in: [packages/helpers/src/helpers.ts:417](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L417)

Type guard: narrow `unknown` to a callable.

Matches arrow functions, `function` declarations, classes, and
built-in callables. Use `isFunction` before invoking values pulled
from untrusted sources (e.g. dynamic imports, JSON-config).

## Parameters

### value

`unknown`

The value to test.

## Returns

`value is (args: unknown[]) => unknown`

## Example

```ts
if (isFunction(handler)) handler(payload);
```
