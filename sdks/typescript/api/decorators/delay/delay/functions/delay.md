# Function: delay()

> **delay**\<`T`\>(`delayMs`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [delay/delay.ts:48](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/delay/delay.ts#L48)

Decorator that delays the execution of a method by the specified time.

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method

## Parameters

### delayMs

`number`

The delay time in milliseconds

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The decorator function

## Throws

When applied to a non-method property

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
