# Function: getPlatform()

&gt; **getPlatform**(): [`Platform`](../type-aliases/Platform)

Defined in: [packages/helpers/src/browser/platform.ts:169](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/platform.ts#L169)

Resolve the device platform: `"ios"`, `"android"`, `"macos"`, `"chromeos"`,
`"windows"`, or `"unknown"`.

## Returns

[`Platform`](../type-aliases/Platform)

The detected platform.

## See

 - [isIOS](./isIOS)
 - [isAndroid](./isAndroid)
 - [isMacOS](./isMacOS)
 - [isChromeOS](./isChromeOS)
 - [isWindows](./isWindows)

## Example

```ts
const platform = getPlatform(); // → "android", "ios", etc.
```
