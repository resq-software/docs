# Function: bindFn()

&gt; **bindFn**\<`D`, `A`\>(`originalMethod`, `context`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [bind/bind.fn.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/bind/bind.fn.ts#L60)

Creates a bound version of a method.

Pure with respect to its inputs: returns a **new** function from
`Function.prototype.bind` and neither mutates `originalMethod` nor `context`.
The binding is permanent — a later `.call`/`.apply` cannot re-point `this`.

## Type Parameters

### D

`D` = `unknown`

The return type of the original method.

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method.

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to bind.

### context

`unknown`

The context (`this`) to bind to.

## Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The bound method.

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
