# Function: isChromeOS()

&gt; **isChromeOS**(): `boolean`

Defined in: [packages/helpers/src/browser/platform.ts:110](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/platform.ts#L110)

Detect whether the current user agent is Chrome OS.

## Returns

`boolean`

`true` if the platform is Chrome OS, otherwise `false`.

## See

https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgent

## Example

```ts
if (isChromeOS()) console.log("Running on Chrome OS");
```
