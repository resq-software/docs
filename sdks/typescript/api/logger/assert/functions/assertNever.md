# Function: assertNever()

&gt; **assertNever**(`value`): `never`

Defined in: [\_assert.ts:35](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/_assert.ts#L35)

Compile-time exhaustiveness guard. Placing a call in the `default` arm of a
`switch` over a finite union makes TypeScript error if a case is ever left
unhandled, keeping the mapping in sync with the union it switches over.

If reached at runtime, it throws — signalling an unhandled value slipped past
the type system.

## Parameters

### value

`never`

The value that should have been narrowed to `never`.

## Returns

`never`

## Throws

Always, when invoked at runtime.
