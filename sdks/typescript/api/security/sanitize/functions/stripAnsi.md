# Function: stripAnsi()

&gt; **stripAnsi**(`text`): `string`

Defined in: [sanitize.ts:607](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L607)

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
