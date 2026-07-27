# Function: isNonNullish()

&gt; **isNonNullish**\<`T`\>(`value`): value is Exclude\<T, null \| undefined\>

Defined in: [packages/helpers/src/utils/value.ts:93](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/value.ts#L93)

Get whether a value is not nullish (not null and not undefined).

## Type Parameters

### T

`T`

## Parameters

### value

`T`

The value to check.

## Returns

value is Exclude\<T, null \| undefined\>

True if the value is neither null nor undefined, with proper type narrowing.

## Example

```ts
const maybeString: string | null | undefined = getValue()

if (isNonNullish(maybeString)) {
  // TypeScript knows maybeString is string, not null or undefined
  console.log(maybeString.charAt(0))
}

// Filter nullish values from arrays
const values = ["hello", null, "world", undefined, "!"]
const cleanValues = values.filter(isNonNullish) // ["hello", "world", "!"]
```
