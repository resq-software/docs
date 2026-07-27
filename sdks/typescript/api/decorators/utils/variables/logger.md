# Variable: logger

&gt; `const` **logger**: `object`

Defined in: [\_utils.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/_utils.ts#L56)

Minimal console-backed logger so decorators can report without a dependency.

## Type Declaration

### info()

&gt; **info**(`message`, `data?`): `void`

Log an informational message, appending JSON-encoded `data` when present.

Writes one line to `console.info` (stdout) — an I/O side effect, not a pure
call. `data` is serialized with `JSON.stringify`, so a circular reference or
a `BigInt` value in it makes the call throw.

#### Parameters

##### message

`string`

The human-readable message.

##### data?

`Record`\<`string`, `unknown`\>

Optional structured context to serialize alongside `message`.

#### Returns

`void`

#### Throws

If `data` cannot be JSON-serialized (circular reference
  or `BigInt` value).
