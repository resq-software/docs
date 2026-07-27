# Function: isString()

&gt; **isString**(`value`): `value is string`

Defined in: [packages/helpers/src/helpers.ts:402](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L402)

Type guard: narrow `unknown` to `string`. Does not match `String`
object wrappers (`new String("x")`), only string primitives.

## Parameters

### value

`unknown`

The value to test.

## Returns

`value is string`

## Example

```ts
if (isString(input)) input.toUpperCase();
```
