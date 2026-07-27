# Function: sleep()

&gt; **sleep**(`ms`): `Promise`\<`void`\>

Defined in: [packages/helpers/src/utils/control.ts:345](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L345)

**`Internal`**

Create a Promise that resolves after a specified delay.

Utility function for introducing delays in async code. Returns a Promise
that resolves with undefined after the specified number of milliseconds. Useful for
implementing timeouts, rate limiting, or adding delays in testing scenarios.

Schedules a `setTimeout` (touches the clock). There is no cancellation hook —
the returned promise always resolves, never rejects, and honours no
`AbortSignal`; the underlying timer cannot be cleared by the caller.

## Parameters

### ms

`number`

The delay in milliseconds

## Returns

`Promise`\<`void`\>

A Promise that resolves after the specified delay

## Example

```ts
async function delayedOperation() {
  console.log('Starting...')
  await sleep(1000) // Wait 1 second
  console.log('Done!')
}

// Can also be used with .then()
sleep(500).then(() => {
  console.log('Half second has passed')
})
```
