# Function: after()

> **after**\<`T`, `D`\>(`config`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [after/after.ts:74](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/after/after.ts#L74)

Decorator that executes a function after the decorated method completes.
The after function receives the method's arguments and return value.

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

### D

`D` = `any`

The return type of the decorated method

## Parameters

### config

[`AfterConfig`](../../after.types/interfaces/AfterConfig)\<`T`, `D`\>

Configuration for the after hook

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The decorator function

## Throws

When applied to a non-method property

## Example

```typescript
class DataProcessor {
  @after({
    func: function({ args, response }) {
      console.log(`Processed ${args[0]} items, result: ${response}`);
    },
    wait: false // Don't wait for after function
  })
  processItems(items: string[]): number {
    return items.length;
  }
}
```
