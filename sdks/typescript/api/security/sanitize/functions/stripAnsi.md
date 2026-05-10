# Function: stripAnsi()

> **stripAnsi**(`text`): `string`

Defined in: [sanitize.ts:427](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/sanitize.ts#L427)

Strips ANSI escape codes from a string.
Useful for cleaning terminal output before logging to files.

## Parameters

### text

`string`

The text potentially containing ANSI codes.

## Returns

`string`

The text with ANSI codes removed.

## Example

```typescript
stripAnsi('\x1b[31mRed text\x1b[0m'); // 'Red text'
```
