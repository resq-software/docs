# Interface: BindConfig

Defined in: [bind/bind.types.ts:27](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/bind/bind.types.ts#L27)

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

Defined in: [bind/bind.types.ts:32](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/bind/bind.types.ts#L32)

If true, the method is bound lazily on first access.
                                  If false, the method is bound at decoration time.
