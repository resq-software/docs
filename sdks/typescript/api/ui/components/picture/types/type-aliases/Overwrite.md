# Type Alias: Overwrite\<T, U\>

&gt; **Overwrite**\<`T`, `U`\> = `Omit`\<`T`, keyof `U`\> & `U`

Defined in: [packages/ui/src/components/picture/types.ts:34](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/picture/types.ts#L34)

`T` with any keys also present in `U` replaced by `U`'s versions.

Used to layer the Picture-specific props (`U`) over a host element's props
(`T`), letting the component's own typings win on any name collision.

## Type Parameters

### T

`T`

The base shape whose colliding members are dropped.

### U

`U`

The overriding shape; its members are kept as-is.
