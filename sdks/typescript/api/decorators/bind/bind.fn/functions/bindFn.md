# Function: bindFn()

> **bindFn**\<`D`, `A`\>(`originalMethod`, `context`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [bind/bind.fn.ts:43](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/bind/bind.fn.ts#L43)

Creates a bound version of a method.

## Type Parameters

### D

`D` = `unknown`

The return type of the original method

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to bind

### context

`unknown`

The context (`this`) to bind to

## Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The bound method

## Example

```typescript
class Calculator {
  private multiplier = 10;

  multiply(value: number): number {
    return value * this.multiplier;
  }
}

const calc = new Calculator();

// Create bound version
const boundMultiply = bindFn(calc.multiply.bind(calc), calc);
const result = boundMultiply(5); // 50

// Can also be used with different context
const calc2 = new Calculator();
// calc2.multiplier = 20;
const boundToCalc2 = bindFn(calc.multiply, calc2);
```
