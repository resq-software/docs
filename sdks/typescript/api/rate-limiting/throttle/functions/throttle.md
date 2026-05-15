# Function: throttle()

> **throttle**\<`T`\>(`func`, `wait`, `options?`): (...`args`) => `ReturnType`\<`T`\> \| `undefined` & `object`

Defined in: [throttle.ts:106](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L106)

Throttle a function to only execute once per specified interval

## Type Parameters

### T

`T` *extends* `AnyFunction`

## Parameters

### func

`T`

Function to throttle

### wait

`number`

Wait time in milliseconds

### options?

Throttle options

#### leading?

`boolean`

#### trailing?

`boolean`

## Returns

(...`args`) => `ReturnType`\<`T`\> \| `undefined` & `object`

Throttled function

## Example

```ts
const fetchData = throttle(() => fetch('/api/data'), 1000);
fetchData(); // Executes immediately
fetchData(); // Ignored
fetchData(); // Ignored
// After 1000ms, next call will execute
```
