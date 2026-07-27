# Function: throttleFn()

&gt; **throttleFn**\<`D`, `A`\>(`originalMethod`, `delayMs`): [`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

Defined in: [throttle/throttle.fn.ts:67](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/throttle/throttle.fn.ts#L67)

Wrap a method so it executes at most once per `delayMs` (function form of
[throttle](../..)). Calls made during the cooldown are dropped.

Leading-edge only — the first call runs synchronously and dropped calls are not
replayed on the trailing edge. Each admitted call schedules a `setTimeout` that
reopens the gate after `delayMs` (a clock/timer effect); the cooldown cannot be
cancelled. Every call to `throttleFn` owns its own cooldown state.

## Type Parameters

### D

`D` = `unknown`

The return type of the original method.

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to throttle.

### delayMs

`number`

The minimum interval between executions, in milliseconds.

## Returns

[`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

The throttled method. It always returns `void`; the wrapped method's
return value is discarded.

## Example

```ts
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
