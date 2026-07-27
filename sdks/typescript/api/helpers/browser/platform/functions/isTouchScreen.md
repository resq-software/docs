# Function: isTouchScreen()

&gt; **isTouchScreen**(): `boolean`

Defined in: [packages/helpers/src/browser/platform.ts:199](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/platform.ts#L199)

Detect whether the current device has touchscreen capability.

## Returns

`boolean`

`true` if a touch screen is supported, otherwise `false`.

## See

 - https://developer.mozilla.org/en-US/docs/Web/API/Navigator/maxTouchPoints
 - https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia

## Example

```ts
if (isTouchScreen()) console.log("Device supports touch.");
```
