# Function: beforeFn()

> **beforeFn**\<`D`, `A`\>(`originalMethod`, `config`): [`Method`](../../../types/type-aliases/Method)\<`Promise`\<`D`\>, `A`\>

Defined in: [before/before.fn.ts:51](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/before/before.fn.ts#L51)

Wraps a method to execute a before hook function before the method runs.

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

[`BeforeConfig`](../../before.types/interfaces/BeforeConfig)\<`any`\>

Configuration for the before hook

## Returns

[`Method`](../../../types/type-aliases/Method)\<`Promise`\<`D`\>, `A`\>

The wrapped method

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
