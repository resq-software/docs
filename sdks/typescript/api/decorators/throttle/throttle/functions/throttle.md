# Function: throttle()

> **throttle**\<`T`\>(`delayMs`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [throttle/throttle.ts:48](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/throttle/throttle.ts#L48)

Decorator that throttles method calls to once per specified time period.

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

## Parameters

### delayMs

`number`

The throttle interval in milliseconds

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The decorator function

## Throws

When applied to a non-method property

## Example

```typescript
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
window.addEventListener('resize', () => handler.handleResize());
// handleResize executes at most once every 200ms during resize
```
