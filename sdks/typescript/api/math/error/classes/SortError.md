# Class: SortError

Defined in: [packages/math/src/error.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L59)

Thrown when a value's sort does not match what an operator expects.

## Example

```ts
asNum(bool(true)); // throws SortError("num", "bool")
```

## Extends

- [`MathError`](./MathError)

## Constructors

### Constructor

&gt; **new SortError**(`expected`, `actual`, `context?`): `SortError`

Defined in: [packages/math/src/error.ts:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L70)

#### Parameters

##### expected

`string`

The sort the operator required.

##### actual

`string`

The sort actually supplied.

##### context?

`string`

Optional location hint (e.g. operator name) for the message.

#### Returns

`SortError`

#### Overrides

[`MathError`](./MathError).[`constructor`](./MathError#constructor)

## Properties

### actualSort

&gt; `readonly` **actualSort**: `string`

Defined in: [packages/math/src/error.ts:63](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L63)

The sort actually supplied.

***

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

### expectedSort

&gt; `readonly` **expectedSort**: `string`

Defined in: [packages/math/src/error.ts:61](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L61)

The sort the operator required.

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
