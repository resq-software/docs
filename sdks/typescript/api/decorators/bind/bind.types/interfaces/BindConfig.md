# Interface: BindConfig

Defined in: [bind/bind.types.ts:39](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/bind/bind.types.ts#L39)

Configuration options describing a bind strategy.

A single flag selecting when the binding happens; an absent [lazy](#lazy) means
"use the default strategy" rather than a distinct third mode.

## Example

```typescript
// Lazy binding (default) - binds on first access
const lazyConfig: BindConfig = { lazy: true };

// Eager binding - binds immediately
const eagerConfig: BindConfig = { lazy: false };
```

## Properties

### lazy?

&gt; `optional` **lazy?**: `boolean`

Defined in: [bind/bind.types.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/bind/bind.types.ts#L44)

If true, the method is bound lazily on first access.
If false (default), the method is bound at decoration time.
