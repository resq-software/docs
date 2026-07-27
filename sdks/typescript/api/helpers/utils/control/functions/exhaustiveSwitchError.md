# Function: exhaustiveSwitchError()

&gt; **exhaustiveSwitchError**(`value`, `property?`): `never`

Defined in: [packages/helpers/src/utils/control.ts:209](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L209)

**`Internal`**

Throws an error for unhandled switch cases in exhaustive switch statements.

Utility function to ensure exhaustive handling of discriminated unions in switch
statements. When called, it indicates a programming error where a case was not handled.
The TypeScript 'never' type ensures this function is only reachable if all cases aren't covered.

Delegates the actual throw to `@resq-systems/types` `assertNever`, the single
source of truth for exhaustiveness enforcement, while preserving this
helper's original `Unknown switch case ...` message (including the optional
`property` extraction) for backward compatibility.

## Parameters

### value

`never`

The unhandled value (typed as 'never' for exhaustiveness checking)

### property?

`string`

Optional property name to extract from the value for better error messages

## Returns

`never`

Never returns (always throws)

## Throws

Always — reaching this at runtime means a union member went
  unhandled. The message is `Unknown switch case <value>` (or the extracted
  `property` when provided and present on an object `value`).

## Example

```ts
type Shape = 'circle' | 'square' | 'triangle'

function getArea(shape: Shape): number {
  switch (shape) {
    case 'circle': return Math.PI * 5 * 5
    case 'square': return 10 * 10
    case 'triangle': return 0.5 * 10 * 8
    default: return exhaustiveSwitchError(shape)
  }
}
```
