# Variable: isNativeStructuredClone

&gt; `const` **isNativeStructuredClone**: `boolean`

Defined in: [packages/helpers/src/utils/value.ts:165](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/value.ts#L165)

**`Internal`**

Whether the current environment has native structuredClone support.

Resolved once at module load. When `false`, [structuredClone](./structuredClone) uses the
JSON fallback with all its limitations (no `Date`/`Map`/`Set`/functions, throws
on cycles and `BigInt`) — branch on this when clone fidelity matters.

## Returns

True if using native structuredClone, false if using JSON fallback.
