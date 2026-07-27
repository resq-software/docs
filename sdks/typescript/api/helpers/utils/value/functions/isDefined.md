# Function: isDefined()

&gt; **isDefined**\<`T`\>(`value`): `value is Exclude<T, undefined>`

Defined in: [packages/helpers/src/utils/value.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/value.ts#L45)

Get whether a value is not undefined.

## Type Parameters

### T

`T`

## Parameters

### value

`T`

The value to check.

## Returns

`value is Exclude<T, undefined>`

True if the value is not undefined, with proper type narrowing.

## Example

```ts
const maybeString: string | undefined = getValue()

if (isDefined(maybeString)) {
  // TypeScript knows maybeString is string, not undefined
  console.log(maybeString.toUpperCase())
}

// Filter undefined values from arrays
const values = [1, undefined, 2, undefined, 3]
const definedValues = values.filter(isDefined) // [1, 2, 3]
```
