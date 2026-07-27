# Function: formatBytes()

&gt; **formatBytes**(`bytes`): `string`

Defined in: [packages/helpers/src/formatting/number.ts:73](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/number.ts#L73)

Format a byte count as a binary-prefixed human-readable string
(Bytes / KB / MB / GB / TB), where one KB = 1024 Bytes.

Note: the unit suffixes use SI symbols for binary prefixes, which is
the historical convention rather than IEC's KiB/MiB/… Pick whichever
matches your product surface and stick with it.

## Parameters

### bytes

`number`

Byte count. `0`, negative, `NaN`, and non-finite inputs
  all return `"0 Bytes"`. Values at or beyond 1 PiB are clamped to the
  largest available unit (`TB`) rather than overflowing the unit table.

## Returns

`string`

Human-readable size to two decimal places, e.g. `"1.50 MB"`.

## Example

```ts
formatBytes(0);             // → "0 Bytes"
formatBytes(1024);          // → "1 KB"
formatBytes(1_572_864);     // → "1.5 MB"
formatBytes(1_073_741_824); // → "1 GB"
```
