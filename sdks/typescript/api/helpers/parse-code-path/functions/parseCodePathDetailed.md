# Function: parseCodePathDetailed()

&gt; **parseCodePathDetailed**(`context`, `entity`, `options?`): `string`

Defined in: [packages/helpers/src/parse-code-path.ts:178](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/parse-code-path.ts#L178)

Build a detailed code-location string with optional line number, ISO
timestamp, and a custom prefix. Useful for enhanced debugging or audit logs.

Effectively non-throwing: line-number extraction is wrapped in its own
try/catch and getFilePath never throws. When `includeTimestamp` is
set the output reads the clock (`new Date()`), so the result is
**non-deterministic** across calls; `includeLineNumber` likewise varies with
the call site.

## Parameters

### context

`string` \| `number`

Context description of the operation or location.

### entity

`string` \| `symbol` \| `object` \| `null` \| `undefined`

The entity whose name is included: a function, class, or instance, a string, or a
  symbol. `null` and `undefined` are accepted and yield `"UnknownEntity"`.

### options?

Optional configuration for the output string.

#### customPrefix?

`string`

Prefix to use instead of the default `"location"`.

#### includeLineNumber?

`boolean`

When true, appends the call-site line number; silently omitted if the stack cannot be parsed.

#### includeTimestamp?

`boolean`

When true, appends a live ISO 8601 timestamp (makes output time-dependent).

## Returns

`string`

The detailed formatted location string.

## Example

```ts
parseCodePathDetailed("init", MyClass, { includeLineNumber: true, includeTimestamp: true });
// → "location: ...:42 [2024-06-01T08:00:00.000Z] @MyClass: init"
```

## See

[parseCodePath](./parseCodePath)
