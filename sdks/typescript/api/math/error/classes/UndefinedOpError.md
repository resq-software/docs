# Class: UndefinedOpError

Defined in: [packages/math/src/error.ts:105](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/error.ts#L105)

Thrown when no type-class instance exists for an operator+sort combination.

## Example

```ts
// There is no instance for "+:bool:bool", so evaluating a bool addition:
evaluate(compile(add(B(true), B(false)))); // throws UndefinedOpError("+", ["bool", "bool"])
```

## Extends

- [`MathError`](./MathError)

## Constructors

### Constructor

&gt; **new UndefinedOpError**(`operator`, `sorts`): `UndefinedOpError`

Defined in: [packages/math/src/error.ts:115](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/error.ts#L115)

#### Parameters

##### operator

`string`

The operator symbol with no matching instance.

##### sorts

readonly `string`[]

The operand sorts that had no registered instance.

#### Returns

`UndefinedOpError`

#### Overrides

[`MathError`](./MathError).[`constructor`](./MathError#constructor)

## Properties

### cause?

&gt; `optional` **cause?**: `unknown`

Defined in: node\_modules/typescript/lib/lib.es2022.error.d.ts:24

#### Inherited from

[`MathError`](./MathError).[`cause`](./MathError#cause)

***

### code

&gt; `readonly` **code**: `string`

Defined in: [packages/math/src/error.ts:38](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/error.ts#L38)

Stable machine-readable error code (e.g. `"SORT_ERROR"`); constant per subclass.

#### Inherited from

[`MathError`](./MathError).[`code`](./MathError#code)

***

### message

&gt; **message**: `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1075

#### Inherited from

[`MathError`](./MathError).[`message`](./MathError#message)

***

### name

&gt; **name**: `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1074

#### Inherited from

[`MathError`](./MathError).[`name`](./MathError#name)

***

### operator

&gt; `readonly` **operator**: `string`

Defined in: [packages/math/src/error.ts:107](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/error.ts#L107)

The operator symbol with no matching instance.

***

### sorts

&gt; `readonly` **sorts**: readonly `string`[]

Defined in: [packages/math/src/error.ts:109](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/error.ts#L109)

The operand sorts that had no registered instance.

***

### stack?

&gt; `optional` **stack?**: `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from

[`MathError`](./MathError).[`stack`](./MathError#stack)
