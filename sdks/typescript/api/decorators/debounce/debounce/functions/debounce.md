# Function: debounce()

&gt; **debounce**\<`T`\>(`delayMs`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [debounce/debounce.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/debounce/debounce.ts#L59)

Decorator that debounces method calls, ensuring the method only executes
after the specified delay has passed since the last call.

Debounce state is kept **per instance** via a `WeakMap` keyed on `this`, so
two instances of the same class debounce independently and the state is
garbage-collected with the instance. The decorated method returns `undefined`
(the original return value is discarded — see [debounceFn](../../debounce.fn/functions/debounceFn)).

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method.

## Parameters

### delayMs

`number`

The debounce delay in milliseconds.

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The decorator function.

## Throws

At decoration time, when applied to anything without a method
  value, with message `"@debounce is applicable only on a methods."`.

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
