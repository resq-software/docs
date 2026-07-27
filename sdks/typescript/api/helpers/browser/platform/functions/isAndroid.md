# Function: isAndroid()

&gt; **isAndroid**(): `boolean`

Defined in: [packages/helpers/src/browser/platform.ts:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/platform.ts#L72)

Detect whether the current user agent is an Android device.

## Returns

`boolean`

`true` if the platform is Android, otherwise `false`.

## See

https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgent

## Example

```ts
if (isAndroid()) console.log("Running on Android");
```
