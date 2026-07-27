# Class: ExecutionLimitError

Defined in: [packages/math/src/error.ts:187](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L187)

Thrown when evaluator execution steps exceed the configured limit.

## Extends

- [`MathError`](./MathError)

## Constructors

### Constructor

&gt; **new ExecutionLimitError**(`limit`): `ExecutionLimitError`

Defined in: [packages/math/src/error.ts:194](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L194)

#### Parameters

##### limit

`number`

The configured maximum number of execution steps.

#### Returns

`ExecutionLimitError`

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

Defined in: [packages/math/src/error.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L38)

Stable machine-readable error code (e.g. `"SORT_ERROR"`); constant per subclass.

#### Inherited from

[`MathError`](./MathError).[`code`](./MathError#code)

***

### limit

&gt; `readonly` **limit**: `number`

Defined in: [packages/math/src/error.ts:189](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L189)

The configured maximum number of execution steps.

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
