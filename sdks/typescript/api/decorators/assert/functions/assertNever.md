# Function: assertNever()

&gt; **assertNever**(`x`): `never`

Defined in: [\_assert.ts:47](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/_assert.ts#L47)

Exhaustiveness guard for discriminated unions.

Call this in the `default` branch of a `switch` over a union's discriminant.
If every variant is handled, `x` narrows to `never` and this type-checks; if a
variant is added later without a matching case, the call becomes a compile error.

## Parameters

### x

`never`

The value that should be of type `never` once all cases are handled

## Returns

`never`

## Throws

Always, if reached at runtime with an unexpected value

## Example

```typescript
switch (mode.kind) {
  case "sync":
    return handleSync(mode);
  case "async":
    return handleAsync(mode);
  default:
    return assertNever(mode);
}
```
