# Function: isMacOS()

&gt; **isMacOS**(): `boolean`

Defined in: [packages/helpers/src/browser/platform.ts:84](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/platform.ts#L84)

Detect whether the current user agent is a macOS device.

## Returns

`boolean`

`true` if the platform is macOS, otherwise `false`.

## See

https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgent

## Example

```ts
if (isMacOS()) console.log("Running on macOS");
```
