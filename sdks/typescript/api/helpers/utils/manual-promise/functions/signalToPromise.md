# Function: signalToPromise()

&gt; **signalToPromise**(`signal`): `object`

Defined in: [packages/helpers/src/utils/manual-promise.ts:116](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/manual-promise.ts#L116)

Bridge an AbortSignal to a promise that resolves when the signal
aborts. Returns the `promise` plus a `dispose` callback that detaches the
internal listener — always call `dispose` (e.g. in a `finally`) to avoid
leaking a listener on a long-lived signal.

If the signal is already aborted, the promise is already resolved and
`dispose` is a no-op.

## Parameters

### signal

`AbortSignal`

## Returns

`object`

### dispose

&gt; **dispose**: () =&gt; `void`

#### Returns

`void`

### promise

&gt; **promise**: `Promise`\<`void`\>

## Example

```ts
const { promise, dispose } = signalToPromise(controller.signal);
try {
  await Promise.race([work(), promise]);
} finally {
  dispose();
}
```
