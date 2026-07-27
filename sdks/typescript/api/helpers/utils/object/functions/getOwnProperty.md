# Function: getOwnProperty()

**`Internal`**

## Call Signature

&gt; **getOwnProperty**\<`K`, `V`\>(`obj`, `key`): `V` \| `undefined`

Defined in: [packages/helpers/src/utils/object.ts:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L64)

**`Internal`**

Safely gets an object's own property value (not inherited). Returns undefined if the property
doesn't exist as an own property. Provides type-safe access with proper TypeScript inference.

### Type Parameters

#### K

`K` *extends* `string`

#### V

`V`

### Parameters

#### obj

`Partial`\<`Record`\<`K`, `V`\>\>

The object to get the property from

#### key

`K`

The property key to retrieve

### Returns

`V` \| `undefined`

The property value if it exists as an own property, undefined otherwise

### Example

```ts
const user = { name: 'Alice', age: 30 }
const name = getOwnProperty(user, 'name') // 'Alice'
const missing = getOwnProperty(user, 'unknown') // undefined
const inherited = getOwnProperty(user, 'toString') // undefined (inherited)
```

## Call Signature

&gt; **getOwnProperty**\<`O`\>(`obj`, `key`): `O`\[keyof `O`\] \| `undefined`

Defined in: [packages/helpers/src/utils/object.ts:69](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L69)

**`Internal`**

### Type Parameters

#### O

`O` *extends* `object`

### Parameters

#### obj

`O`

#### key

`string`

### Returns

`O`\[keyof `O`\] \| `undefined`

## Call Signature

&gt; **getOwnProperty**(`obj`, `key`): `unknown`

Defined in: [packages/helpers/src/utils/object.ts:71](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L71)

**`Internal`**

### Parameters

#### obj

`object`

#### key

`string`

### Returns

`unknown`
