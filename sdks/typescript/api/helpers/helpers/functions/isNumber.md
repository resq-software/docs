# Function: isNumber()

&gt; **isNumber**(`value`): `value is number`

Defined in: [packages/helpers/src/helpers.ts:390](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L390)

Type guard: narrow `unknown` to `number`.

Note: returns `true` for `NaN` (which is a `number`). Use
`Number.isFinite` afterward if you need to exclude it.

## Parameters

### value

`unknown`

The value to test.

## Returns

`value is number`

## Example

```ts
if (isNumber(input)) input.toFixed(2);
```
