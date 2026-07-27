# Class: RecursionLimitError

Defined in: [packages/math/src/error.ts:202](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/error.ts#L202)

Thrown when recursion depth exceeds the configured limit during parsing or evaluation.

## Extends

- [`MathError`](./MathError)

## Constructors

### Constructor

&gt; **new RecursionLimitError**(`limit`): `RecursionLimitError`

Defined in: [packages/math/src/error.ts:209](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/error.ts#L209)

#### Parameters

##### limit

`number`

The configured maximum recursion depth.

#### Returns

`RecursionLimitError`

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

### limit

&gt; `readonly` **limit**: `number`

Defined in: [packages/math/src/error.ts:204](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/error.ts#L204)

The configured maximum recursion depth.

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

### stack?

&gt; `optional` **stack?**: `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from

[`MathError`](./MathError).[`stack`](./MathError#stack)
