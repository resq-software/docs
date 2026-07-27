# Class: StackError

Defined in: [packages/math/src/error.ts:168](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L168)

Thrown when a lexical stack lookup is out of bounds.

## Extends

- [`MathError`](./MathError)

## Constructors

### Constructor

&gt; **new StackError**(`index`, `depth`): `StackError`

Defined in: [packages/math/src/error.ts:178](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L178)

#### Parameters

##### index

`number`

The De Bruijn index that was requested.

##### depth

`number`

The stack depth available at the time of access.

#### Returns

`StackError`

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

### depth

&gt; `readonly` **depth**: `number`

Defined in: [packages/math/src/error.ts:172](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L172)

The stack depth available at the time of access.

***

### index

&gt; `readonly` **index**: `number`

Defined in: [packages/math/src/error.ts:170](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L170)

The De Bruijn index that was requested.

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
