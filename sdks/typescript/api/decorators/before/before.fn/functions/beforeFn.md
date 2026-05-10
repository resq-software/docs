# Function: beforeFn()

> **beforeFn**\<`D`, `A`\>(`originalMethod`, `config`): [`Method`](../../../types/type-aliases/Method.md)\<`Promise`\<`D`\>, `A`\>

Defined in: [before/before.fn.ts:51](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/before/before.fn.ts#L51)

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

[`Method`](../../../types/type-aliases/Method.md)\<`D`, `A`\>

The method to wrap

### config

[`BeforeConfig`](../../before.types/interfaces/BeforeConfig.md)\<`any`\>

Configuration for the before hook

## Returns

[`Method`](../../../types/type-aliases/Method.md)\<`Promise`\<`D`\>, `A`\>

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
