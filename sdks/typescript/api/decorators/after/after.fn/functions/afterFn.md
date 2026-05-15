# Function: afterFn()

> **afterFn**\<`D`, `A`\>(`originalMethod`, `config`): (...`args`) => `Promise`\<`D`\>

Defined in: [after/after.fn.ts:51](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/after/after.fn.ts#L51)

Wraps a method to execute an after hook function after the method completes.

## Type Parameters

### D

`D` = `any`

The return type of the original method

### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to wrap

### config

[`AfterConfig`](../../after.types/interfaces/AfterConfig)\<`any`, `D`\>

Configuration for the after hook

## Returns

The wrapped method

(...`args`) => `Promise`\<`D`\>

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
