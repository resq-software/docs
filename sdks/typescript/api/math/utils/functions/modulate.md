# Function: modulate()

&gt; **modulate**(`value`, `rangeA`, `rangeB`, `clamp?`): `number`

Defined in: [packages/math/src/utils.ts:121](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/utils.ts#L121)

Remap a value from an input range onto an output range.

Handles a degenerate input range (equal endpoints) by returning the output
low bound, and can optionally clamp the result to the output range regardless
of its direction.

## Parameters

### value

`number`

The value to remap, expressed in the input range.

### rangeA

`number`[]

Input range as a two-element `[low, high]` array; only indices 0 and 1 are read.

### rangeB

`number`[]

Output range as a two-element `[low, high]` array; `high < low` is allowed and reverses the mapping.

### clamp?

`boolean` = `false`

When `true`, constrain the result to the output range regardless of its direction.

## Returns

`number`

The remapped value, or `NaN` if a range array is missing an endpoint.

## Example

```ts
modulate(5, [0, 10], [0, 100]); // → 50
```
