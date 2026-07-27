# Function: afterFn()

&gt; **afterFn**\<`T`, `D`, `A`\>(`originalMethod`, `config`): (...`args`) =&gt; `Promise`\<`Awaited`\<`D`\>\>

Defined in: [after/after.fn.ts:69](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/after/after.fn.ts#L69)

Wraps a method to execute an after-hook function once the method completes.

The wrapper is **always async**: it returns a `Promise` even when
`originalMethod` is synchronous, because it awaits the result so the hook
receives the resolved value. The hook runs only on success — if
`originalMethod` throws or rejects, the returned promise rejects with that
error and the hook is skipped. Each call is independent (no shared state), so
concurrent invocations are safe; there is no `AbortSignal` support.

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

[`AfterConfig`](../../after.types/interfaces/AfterConfig)\<`T`, `Awaited`\<`D`\>\>

Configuration for the after hook.

## Returns

The wrapped method, which resolves to the original method's value.

(...`args`) =&gt; `Promise`\<`Awaited`\<`D`\>\>

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
const wrapped = afterFn(
  service.process.bind(service),
  {
    func: ({ args, response }) => {
      console.log(`Called with ${args[0]}, returned ${response}`);
    },
    wait: false
  }
);

await wrapped('hello'); // Logs: Called with hello, returned HELLO
```
