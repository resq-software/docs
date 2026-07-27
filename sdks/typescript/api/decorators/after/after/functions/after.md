# Function: after()

&gt; **after**\<`T`, `D`\>(`config`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [after/after.ts:77](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/after/after.ts#L77)

Decorator that executes a function after the decorated method completes.
The after function receives the method's arguments and return value.

Applying the decorator rewrites the property descriptor's `value` with the
wrapped method, which becomes **async** (returns a `Promise`) regardless of
whether the original was synchronous — callers must adjust for the added
`await`. See [afterFn](../../after.fn/functions/afterFn) for the per-call failure and hook semantics.

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method.

### D

`D` = `unknown`

The return type of the decorated method.

## Parameters

### config

[`AfterConfig`](../../after.types/interfaces/AfterConfig)\<`T`, `D`\>

Configuration for the after hook.

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The decorator function.

## Throws

At decoration time, when applied to anything without a method
  value (an accessor or field), with message
  `"@after is applicable only on a methods."`.

## Example

```typescript
class DataProcessor {
  @after({
    func: function ({ args, response }) {
      console.log(`Processed ${args[0]} items, result: ${response}`);
    },
    wait: false, // Don't wait for the after function.
  })
  processItems(items: string[]): number {
    return items.length;
  }
}
```
