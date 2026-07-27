# Function: warnOnce()

&gt; **warnOnce**(`message`): `void`

Defined in: [packages/helpers/src/utils/warn.ts:90](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/warn.ts#L90)

**`Internal`**

Issues a warning message to the console, but only once per unique message.
Subsequent calls with the same message are ignored, preventing console spam.
All messages are logged using the resq structured logger under the "helpers" context.

Effects: writes through the shared `helpers` logger and records `message` in a
module-global set of already-seen strings. Dedup is by exact string equality and
persists for the process lifetime (never cleared), so a message logs at most
once; repeat calls with the same string are no-ops.

## Parameters

### message

`string`

The warning message to display

## Returns

`void`

## Example

```ts
// Warn about deprecated usage
function oldFunction() {
  warnOnce('oldFunction is deprecated, use newFunction instead')
  // Continue with implementation...
}

// First call logs warning
oldFunction() // Shows warning
oldFunction() // No warning (already shown)
oldFunction() // No warning (already shown)
```
