# Function: beforeFn()

&gt; **beforeFn**\<`T`, `D`, `A`\>(`originalMethod`, `config`): [`Method`](../../../types/type-aliases/Method)\<`Promise`\<`D`\>, `A`\>

Defined in: [before/before.fn.ts:69](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/before/before.fn.ts#L69)

Wraps a method to execute a before-hook function before the method runs.

The wrapper is **always async** (returns a `Promise<D>` even for a synchronous
`originalMethod`). With `config.wait`, the hook is awaited first: if it throws
or rejects, the returned promise rejects and `originalMethod` is never called
(guard semantics). Without `wait`, the hook is invoked but not awaited — its
return is ignored and the method runs regardless. Each call is independent
(no shared state); there is no `AbortSignal` support.

## Type Parameters

### T

`T` = `unknown`

The type owning the named hook when `config.func` is a method name.

### D

`D` = `unknown`

The return type of the original method.

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method.

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to wrap.

### config

[`BeforeConfig`](../../before.types/interfaces/BeforeConfig)\<`T`\>

Configuration for the before hook.

## Returns

[`Method`](../../../types/type-aliases/Method)\<`Promise`\<`D`\>, `A`\>

The wrapped method.

## Throws

As a rejected promise, when `config.func` is a method name
  that does not resolve to a callable on the invocation's `this`.

## Example

```typescript
class Service {
  process(data: string): string {
    return data.toUpperCase();
  }
}

const service = new Service();
const wrapped = beforeFn(
  service.process.bind(service),
  {
    func: () => {
      console.log('About to process...');
    },
    wait: false
  }
);

await wrapped('hello'); // Logs "About to process..." then returns "HELLO"
```
