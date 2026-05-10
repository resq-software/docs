# Function: throttleAsync()

> **throttleAsync**\<`T`, `D`\>(`parallelCalls?`): [`Decorator`](../../../types/type-aliases/Decorator.md)\<`T`\>

Defined in: [throttle-async/throttle-async.ts:82](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/throttle-async/throttle-async.ts#L82)

Decorator that limits concurrent async method calls.
Excess calls are queued and executed when slots become available.

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

### D

`D` = `any`

The resolved type of the async method

## Parameters

### parallelCalls?

`number`

Maximum number of concurrent calls allowed

## Returns

[`Decorator`](../../../types/type-aliases/Decorator.md)\<`T`\>

The decorator function

## Throws

When applied to a non-method property

## Example

```typescript
class BatchProcessor {
  // Process up to 5 items concurrently
  @throttleAsync(5)
  async processItem(item: Item): Promise<Result> {
    return await this.performHeavyProcessing(item);
  }
}

const processor = new BatchProcessor();
const items = Array.from({ length: 100 }, (_, i) => ({ id: i }));

// Process 100 items, 5 at a time
const results = await Promise.all(
  items.map(item => processor.processItem(item))
);
```
