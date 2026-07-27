# Function: groupBy()

&gt; **groupBy**\<`K`, `V`\>(`array`, `keySelector`): `Record`\<`K`, `V`[]\>

Defined in: [packages/helpers/src/utils/object.ts:311](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L311)

**`Internal`**

Groups an array of values into a record by a key extracted from each value.
The key selector function is called for each element to determine the grouping key.

## Type Parameters

### K

`K` *extends* `string`

### V

`V`

## Parameters

### array

readonly `V`[]

The array to group

### keySelector

(`value`) =&gt; `K`

Function that extracts the grouping key from each value

## Returns

`Record`\<`K`, `V`[]\>

A record where keys are the extracted keys and values are arrays of grouped items

## Example

```ts
const people = [
  { name: 'Alice', age: 25 },
  { name: 'Bob', age: 30 },
  { name: 'Charlie', age: 25 }
]
const byAge = groupBy(people, person => `age-${person.age}`)
// { 'age-25': [Alice, Charlie], 'age-30': [Bob] }
```
