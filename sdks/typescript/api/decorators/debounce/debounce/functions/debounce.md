# Function: debounce()

> **debounce**\<`T`\>(`delayMs`): [`Decorator`](../../../types/type-aliases/Decorator.md)\<`T`\>

Defined in: [debounce/debounce.ts:47](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/debounce/debounce.ts#L47)

Decorator that debounces method calls, ensuring the method only executes
after the specified delay has passed since the last call.

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method

## Parameters

### delayMs

`number`

The debounce delay in milliseconds

## Returns

[`Decorator`](../../../types/type-aliases/Decorator.md)\<`T`\>

The decorator function

## Throws

When applied to a non-method property

## Example

```typescript
class AutoSave {
  @debounce(1000)
  saveDraft(content: string) {
    // Saves only 1 second after user stops typing
    localStorage.setItem('draft', content);
  }
}

// Usage
const autoSave = new AutoSave();
autoSave.saveDraft('Hello'); // Won't save yet
autoSave.saveDraft('Hello World'); // Resets timer
// After 1 second of inactivity, saveDraft executes once
```
