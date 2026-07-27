# Function: LogClass()

&gt; **LogClass**(`options?`): \<`T`\>(`target`) =&gt; `T`

Defined in: [logger.decorators.ts:273](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.decorators.ts#L273)

Class decorator that wraps every own prototype method with call (and optional
timing) logging, skipping the constructor and any names in
[LogClassOptions.exclude](../../logger.types/interfaces/LogClassOptions#exclude).

Mutates the target's prototype in place, redefining each own method via
`Object.defineProperty`, then returns the same constructor reference (not a
subclass). Only own, enumerable-by-`getOwnPropertyNames` function properties
are wrapped: inherited methods, accessors (getters/setters), and
property-assigned arrow functions are left untouched. As with [Log](./Log),
failures are logged only on the async path; a synchronous throw propagates
un-logged.

## Parameters

### options?

[`LogClassOptions`](../../logger.types/interfaces/LogClassOptions) = `{}`

Configuration options.

## Returns

A class decorator that returns the (mutated) constructor.

\<`T`\>(`target`) =&gt; `T`

## Example

```ts
@LogClass({ exclude: ["privateMethod"], timing: true })
class MyService {
  publicMethod() {}
  privateMethod() {} // Won't be logged.
}
```
