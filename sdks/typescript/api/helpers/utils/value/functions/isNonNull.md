# Function: isNonNull()

&gt; **isNonNull**\<`T`\>(`value`): `value is Exclude<T, null>`

Defined in: [packages/helpers/src/utils/value.ts:69](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/value.ts#L69)

Get whether a value is not null.

## Type Parameters

### T

`T`

## Parameters

### value

`T`

The value to check.

## Returns

`value is Exclude<T, null>`

True if the value is not null, with proper type narrowing.

## Example

```ts
const maybeString: string | null = getValue()

if (isNonNull(maybeString)) {
  // TypeScript knows maybeString is string, not null
  console.log(maybeString.length)
}

// Filter null values from arrays
const values = ["a", null, "b", null, "c"]
const nonNullValues = values.filter(isNonNull) // ["a", "b", "c"]
```
