# Function: throttle()

&gt; **throttle**\<`T`\>(`delayMs`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [throttle/throttle.ts:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/throttle/throttle.ts#L62)

Throttle a method to at most one call per `delayMs`; calls made during the
cooldown are dropped.

Leading-edge only: the first call runs immediately and there is no trailing call
for anything dropped during the cooldown. The throttled method returns `void` —
the original's return value is discarded. The cooldown flag is created once, at
decoration time, so it is shared across every instance of the class. Mutates the
supplied property descriptor in place.

## Type Parameters

### T

`T` = `unknown`

The class type that owns the decorated method.

## Parameters

### delayMs

`number`

The minimum interval between executions, in milliseconds.

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The method decorator.

## Throws

If applied to a member without a `value` descriptor (an accessor
or plain property rather than a method).

## Example

```ts
class ResizeHandler {
  private width = window.innerWidth;
  private height = window.innerHeight;

  @throttle(200)
  handleResize(): void {
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.render();
  }
}

const handler = new ResizeHandler();
window.addEventListener("resize", () => handler.handleResize());
// handleResize executes at most once every 200ms during a resize.
```

## See

[throttleFn](../../throttle.fn/functions/throttleFn) for the function form.
