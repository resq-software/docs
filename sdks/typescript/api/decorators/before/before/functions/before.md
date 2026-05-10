# Function: before()

> **before**\<`T`\>(`config`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [before/before.ts:75](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/before/before.ts#L75)

Decorator that executes a function before the decorated method.
The before function is called before the method body executes.

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

## Parameters

### config

[`BeforeConfig`](../../before.types/interfaces/BeforeConfig)\<`T`\>

Configuration for the before hook

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The decorator function

## Throws

When applied to a non-method property

## Example

```typescript
class DataProcessor {
  @before({
    func: function() {
      console.log('About to process...');
    },
    wait: false
  })
  processItems(items: string[]): number {
    return items.length;
  }
}
```
