# Function: assertNever()

&gt; **assertNever**(`value`): `never`

Defined in: [\_assert.ts:33](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/_assert.ts#L33)

Asserts that a code path is unreachable. Placing this in a `switch` default
arm makes the compiler reject the switch if any union member is left
unhandled, because a non-`never` value cannot be passed here.

## Parameters

### value

`never`

The value the type system has narrowed to `never`.

## Returns

`never`

## Throws

Always, if reached at runtime (e.g. an untyped value slipped
  past the compiler); the message includes the offending value.
