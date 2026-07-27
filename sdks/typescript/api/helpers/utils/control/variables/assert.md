# Variable: assert

&gt; `const` **assert**: (`value`, `message?`) =&gt; `asserts value`

Defined in: [packages/helpers/src/utils/control.ts:237](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L237)

**`Internal`**

Assert that a value is truthy, throwing an error if it's not.

TypeScript assertion function that throws an error if the provided value is falsy.
After this function executes successfully, TypeScript narrows the type to exclude falsy values.
Stack trace is omitted from the error for cleaner debugging.

## Parameters

### value

`unknown`

The value to assert as truthy

### message?

`string`

Optional custom error message

## Returns

`asserts value`

## Throws

If `value` is falsy. The message is `message` when supplied,
  otherwise `Assertion Error`. The wrapper's own frame is stripped from the
  stack (V8 only), so the trace points at the call site.

## Example

```ts
const user = getUser() // User | null
assert(user, 'User must be logged in')
// TypeScript now knows user is non-null
console.log(user.name) // Safe to access properties
```
