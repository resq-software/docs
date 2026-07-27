# Function: getBrowser()

&gt; **getBrowser**(): [`BrowserName`](../type-aliases/BrowserName)

Defined in: [packages/helpers/src/browser/platform.ts:127](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/platform.ts#L127)

Resolve the browser name from the user-agent string.

## Returns

[`BrowserName`](../type-aliases/BrowserName)

The browser name: `"edge"`, `"chrome"`, `"firefox"`, `"safari"`, `"opera"`, `"android"`, `"iphone"`, or `"unknown"`.

## Throws

If `navigator.userAgent` is not accessible.

## See

https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgent

## Example

```ts
const browser = getBrowser(); // → "chrome", "firefox", etc.
```
