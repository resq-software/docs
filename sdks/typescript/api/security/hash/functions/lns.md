# Function: lns()

&gt; **lns**(`str`): `string`

Defined in: [hash.ts:101](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/hash.ts#L101)

Reversibly scramble a string by rotating character blocks and shifting digits.

A lightweight, non-cryptographic obfuscation: it reorders characters via a fixed
sequence of block rotations, reverses the result, and maps each digit `d` to
`d < 5 ? d + 5 : d > 5 ? d - 5 : d`. Provides obscurity, not security — do not
use it to protect secrets.

Despite "scramble", the transform is **not a true inverse**: the digit map sends
both `0` and `5` to `5`, so any input containing those digits cannot be
recovered unambiguously. Non-digit characters (including whitespace) are only
reordered, never substituted. Deterministic and free of side effects.

## Parameters

### str

`string`

The string to transform.

## Returns

`string`

The transformed string, same length as `str`.
