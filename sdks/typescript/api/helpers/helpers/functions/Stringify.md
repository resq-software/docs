# Function: Stringify()

&gt; **Stringify**(`obj`): `string`

Defined in: [packages/helpers/src/helpers.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L46)

Serialize a value to a JSON string with two-space indentation.

Thin wrapper over `JSON.stringify(obj, null, 2)` for readable debug and log
output; throws on circular references exactly as `JSON.stringify` does.

## Parameters

### obj

`object`

The value to serialize.

## Returns

`string`

The indented JSON representation.

## Throws

If `obj` contains a circular reference.

## Example

```ts
Stringify({ name: "John", age: 30 });
// → '{\n  "name": "John",\n  "age": 30\n}'
```
