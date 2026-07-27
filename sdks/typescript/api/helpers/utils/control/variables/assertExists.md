# Variable: assertExists

&gt; `const` **assertExists**: \<`T`\>(...`args`) =&gt; `NonNullable`

Defined in: [packages/helpers/src/utils/control.ts:268](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L268)

**`Internal`**

Assert that a value is not null or undefined.

Throws an error if the value is null or undefined, otherwise returns the value
with a refined type that excludes null and undefined. Stack trace is omitted for cleaner debugging.

## Type Parameters

### T

`T`

## Parameters

### args

...\[`T`, `string`\]

## Returns

`NonNullable`

The value with null and undefined excluded from the type

## Throws

If `value` is `null` or `undefined` (loose `== null` check, so
  `0`, `''`, and `false` pass). The message is `message` when supplied,
  otherwise `value must be defined`. The wrapper's own frame is stripped from
  the stack (V8 only).

## Example

```ts
const element = document.getElementById('my-id') // HTMLElement | null
const safeElement = assertExists(element, 'Element not found')
// TypeScript now knows safeElement is HTMLElement (not null)
safeElement.addEventListener('click', handler) // Safe to call methods
```
