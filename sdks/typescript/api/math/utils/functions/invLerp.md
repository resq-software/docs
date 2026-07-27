# Function: invLerp()

&gt; **invLerp**(`a`, `b`, `t`): `number`

Defined in: [packages/math/src/utils.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/utils.ts#L56)

Inverse of [lerp](./lerp): map a value in `[a, b]` back to its `[0, 1]` factor.

Returns `0` for a degenerate range (`a === b`) rather than dividing by zero.

## Parameters

### a

`number`

Range start.

### b

`number`

Range end.

### t

`number`

The value to locate within `[a, b]`.

## Returns

`number`

The interpolation factor, or `0` when the range has zero width.

## Example

```ts
invLerp(0, 10, 5); // → 0.5
```

## See

[lerp](./lerp)
