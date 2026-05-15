# Function: stripAnsi()

> **stripAnsi**(`text`): `string`

Defined in: [sanitize.ts:427](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/sanitize.ts#L427)

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
