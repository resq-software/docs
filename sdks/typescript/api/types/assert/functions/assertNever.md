# Function: assertNever()

&gt; **assertNever**(`value`, `message?`): `never`

Defined in: [assert.ts:59](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/assert.ts#L59)

Assert that a code path is unreachable. Placed in the `default` arm of an
exhaustive `switch`, the `value: never` parameter fails to type-check the
moment the union it discriminates gains a member that isn't handled above —
so adding a case to the union without adding a branch is a build error, not a
production surprise. At runtime (should it ever be reached via an untyped
caller) it throws.

## Parameters

### value

`never`

The value that should have been narrowed to `never`.

### message?

`string`

Optional override for the thrown error message.

## Returns

`never`

Never returns — always throws.

## Throws

Always, when actually invoked at runtime.

## Example

```ts
type ThreatType = "xss" | "sql_injection" | "path_traversal";

function message(t: ThreatType): string {
  switch (t) {
    case "xss": return "script content";
    case "sql_injection": return "database commands";
    case "path_traversal": return "file path characters";
    default: return assertNever(t); // ✗ compile error if a ThreatType is added
  }
}
```
