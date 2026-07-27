# Function: lerp()

&gt; **lerp**(`a`, `b`, `t`): `number`

Defined in: [packages/math/src/utils.ts:37](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/utils.ts#L37)

Linearly interpolate between two values.

## Parameters

### a

`number`

Start value, returned when `t` is `0`.

### b

`number`

End value, returned when `t` is `1`.

### t

`number`

Interpolation factor, typically in `[0, 1]` but not clamped.

## Returns

`number`

The value `t` of the way from `a` to `b`.

## Example

```ts
lerp(0, 10, 0.5); // → 5
```
