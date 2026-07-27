# Function: parseCodePath()

&gt; **parseCodePath**(`context`, `entity`): `string`

Defined in: [packages/helpers/src/parse-code-path.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/parse-code-path.ts#L59)

Build a formatted string describing a code location: the file path, the
associated entity name (function, class, instance, string, or symbol), and a
human-readable context.

Useful for debugging, developer logging, and traceability.

Effectively non-throwing for ordinary entities: getFilePath swallows
any stack-trace parse failure and falls back to a sentinel path, and
extractEntityName handles every input kind. Reads the current call
stack / `__filename` but has no side effects.

## Parameters

### context

`string` \| `number`

A description, situation, or custom value relevant to this code path.

### entity

`string` \| `symbol` \| `object` \| `null` \| `undefined`

The entity whose name is included: a function, class, or instance, a string, or a
  symbol. `null` and `undefined` are accepted and yield `"UnknownEntity"`.

## Returns

`string`

A formatted string of the form `"location: <path> @<entity>: <context>"`.
  When the location cannot be determined, `<path>` degrades to
  `"unknown-location"` rather than the call failing.

## Example

```ts
function myFunction() {}
parseCodePath("initialization", myFunction);
// → "location: /current/dir/file.js @myFunction: initialization"

class MyClass {}
parseCodePath("instantiating MyClass", MyClass);
// → "location: ... @MyClass: instantiating MyClass"

parseCodePath("some context", "EntityAsString");
// → "location: ... @EntityAsString: some context"
```

## See

[parseCodePathDetailed](./parseCodePathDetailed)
