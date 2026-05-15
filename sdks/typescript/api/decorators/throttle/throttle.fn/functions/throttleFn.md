# Function: throttleFn()

> **throttleFn**\<`D`, `A`\>(`originalMethod`, `delayMs`): [`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

Defined in: [throttle/throttle.fn.ts:54](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/throttle/throttle.fn.ts#L54)

Wraps a method to throttle its execution to once per time period.

## Type Parameters

### D

`D` = `any`

The return type of the original method

### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to throttle

### delayMs

`number`

The throttle interval in milliseconds

## Returns

[`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

The throttled method

## Example

```typescript
class ScrollTracker {
  scrollY = 0;

  updatePosition(y: number): void {
    this.scrollY = y;
    console.log('Position updated:', y);
  }
}

const tracker = new ScrollTracker();

// Throttle to once per 100ms
const throttledUpdate = throttleFn(
  tracker.updatePosition.bind(tracker),
  100
);

// Rapid scroll events
window.addEventListener('scroll', (e) => {
  throttledUpdate(window.scrollY);
  // Only logs once every 100ms even during rapid scrolling
});
```
