# Function: debounce()

> **debounce**\<`T`\>(`func`, `wait`, `options?`): (...`args`) => `void` & `object`

Defined in: [throttle.ts:177](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L177)

Debounce a function to only execute after it stops being called for specified time

## Type Parameters

### T

`T` *extends* `AnyFunction`

## Parameters

### func

`T`

Function to debounce

### wait

`number`

Wait time in milliseconds

### options?

Debounce options

#### leading?

`boolean`

#### maxWait?

`number`

## Returns

(...`args`) => `void` & `object`

Debounced function

## Example

```ts
const search = debounce((query) => fetchSearchResults(query), 300);
search('a'); // Waiting...
search('ab'); // Waiting...
search('abc'); // Executes after 300ms of no calls
```
