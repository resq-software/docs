# Function: before()

&gt; **before**\<`T`\>(`config`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [before/before.ts:78](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/before/before.ts#L78)

Decorator that executes a function before the decorated method.
The before function is called before the method body executes.

Applying the decorator rewrites the property descriptor's `value` with the
wrapped method, which becomes **async** (returns a `Promise`) even if the
original was synchronous. With `config.wait`, a throwing hook aborts the call;
see [beforeFn](../../before.fn/functions/beforeFn) for the full per-call contract.

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method.

## Parameters

### config

[`BeforeConfig`](../../before.types/interfaces/BeforeConfig)\<`T`\>

Configuration for the before hook.

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The decorator function.

## Throws

At decoration time, when applied to anything without a method
  value (an accessor or field), with message
  `"@before is applicable only on a methods."`.

## Example

```typescript
class DataProcessor {
  @before({
    func: function () {
      console.log("About to process...");
    },
    wait: false,
  })
  processItems(items: string[]): number {
    return items.length;
  }
}
```
