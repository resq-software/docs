# Function: omit()

&gt; **omit**(`obj`, `keys`): `Record`\<`string`, `unknown`\>

Defined in: [packages/helpers/src/utils/object.ts:339](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L339)

**`Internal`**

Creates a new object with specified keys omitted from the original object.
Uses shallow copying and then deletes the unwanted keys.

## Parameters

### obj

`Record`\<`string`, `unknown`\>

The source object

### keys

readonly `string`[]

Array of key names to omit from the result

## Returns

`Record`\<`string`, `unknown`\>

A new object without the specified keys

## Example

```ts
const user = { id: '123', name: 'Alice', password: 'secret', email: 'alice@example.com' }
const publicUser = omit(user, ['password'])
// { id: '123', name: 'Alice', email: 'alice@example.com' }
```
