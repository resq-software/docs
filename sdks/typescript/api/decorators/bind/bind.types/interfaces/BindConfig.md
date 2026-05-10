# Interface: BindConfig

Defined in: [bind/bind.types.ts:27](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/bind/bind.types.ts#L27)

Configuration options for the bind decorator.

 BindConfig

## Example

```typescript
// Lazy binding (default) - binds on first access
const lazyConfig: BindConfig = { lazy: true };

// Eager binding - binds immediately
const eagerConfig: BindConfig = { lazy: false };
```

## Properties

### lazy?

> `optional` **lazy?**: `boolean`

Defined in: [bind/bind.types.ts:32](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/bind/bind.types.ts#L32)

If true, the method is bound lazily on first access.
                                  If false, the method is bound at decoration time.
