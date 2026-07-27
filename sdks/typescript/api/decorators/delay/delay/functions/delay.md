# Function: delay()

&gt; **delay**\<`T`\>(`delayMs`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [delay/delay.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/delay/delay.ts#L59)

Decorator that delays the execution of a method by the specified time.

Rewrites the descriptor so calls return `undefined` immediately and the body
runs `delayMs` later; the original return value is discarded (see
[delayFn](../../delay.fn/functions/delayFn)). Every call schedules its own timer — there is no dedup.

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method.

## Parameters

### delayMs

`number`

The delay time in milliseconds.

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The decorator function.

## Throws

At decoration time, when applied to anything without a method
  value, with message `"@delay is applicable only on a methods."`.

## Example

```typescript
class AnimationController {
  @delay(500)
  fadeIn(element: HTMLElement) {
    element.style.opacity = '1';
  }

  @delay(1000)
  fadeOut(element: HTMLElement) {
    element.style.opacity = '0';
  }
}

const controller = new AnimationController();
controller.fadeIn(element); // Fades in after 500ms
controller.fadeOut(element); // Fades out after 1000ms
```
