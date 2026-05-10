# Function: delegateFn()

> **delegateFn**\<`D`, `A`\>(`originalMethod`, `keyResolver?`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod.md)\<`D`, `A`\>

Defined in: [delegate/delegate.fn.ts:77](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/delegate/delegate.fn.ts#L77)

Wraps an async method to deduplicate concurrent calls.
Multiple calls with the same key will share the same promise
until the first one completes.

## Type Parameters

### D

`D` = `any`

The resolved type of the promise

### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

## Parameters

### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod.md)\<`D`, `A`\>

The async method to wrap

### keyResolver?

(...`args`) => `string`

Optional function to generate cache keys

## Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod.md)\<`D`, `A`\>

The delegated method

## Example

```typescript
class Service {
  async fetchData(id: string): Promise<Data> {
    console.log(`Fetching ${id}`);
    return fetch(`/api/data/${id}`).then(r => r.json());
  }
}

const service = new Service();
const delegated = delegateFn(
  service.fetchData.bind(service),
  (id) => id // Use id directly as key
);

// These share the same promise - "Fetching 123" is logged only once
const p1 = delegated('123');
const p2 = delegated('123');
const [d1, d2] = await Promise.all([p1, p2]);
```
