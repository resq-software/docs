# Type Alias: XOR\<T, U\>

&gt; **XOR**\<`T`, `U`\> = `T` \| `U` *extends* `object` ? [`Without`](./Without)\<`T`, `U`\> & `U` \| [`Without`](./Without)\<`U`, `T`\> & `T` : `T` \| `U`

Defined in: [object.ts:185](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L185)

Exclusive-or of two object types: a value matching `T` **or** `U` but never a
mix of both. Stronger than a plain union — it forbids the keys of the other
branch, so excess/mixed properties are a compile error. The two-type
counterpart of [RequireExactlyOne](./RequireExactlyOne).

## Type Parameters

### T

`T`

### U

`U`

## Example

```ts
type ById = { id: string };
type ByEmail = { email: string };
declare function lookup(q: XOR<ById, ByEmail>): void;
lookup({ id: "1" });                 // ✓
lookup({ email: "a@b.com" });        // ✓
lookup({ id: "1", email: "a@b.com" }); // ✗ — can't be both
```
