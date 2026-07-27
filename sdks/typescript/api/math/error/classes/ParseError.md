# Class: ParseError

Defined in: [packages/math/src/error.ts:148](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L148)

Thrown by the Pratt parser for invalid or unexpected input.

## Extends

- [`MathError`](./MathError)

## Constructors

### Constructor

&gt; **new ParseError**(`message`, `position`, `found?`): `ParseError`

Defined in: [packages/math/src/error.ts:159](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L159)

#### Parameters

##### message

`string`

Human-readable description of the parse failure.

##### position

`number`

Zero-based character offset where parsing failed.

##### found?

`string`

The token or character actually encountered.

#### Returns

`ParseError`

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

### found

&gt; `readonly` **found**: `string`

Defined in: [packages/math/src/error.ts:152](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L152)

The token or character actually encountered.

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

### position

&gt; `readonly` **position**: `number`

Defined in: [packages/math/src/error.ts:150](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L150)

Zero-based character offset in the source where parsing failed.

***

### stack?

&gt; `optional` **stack?**: `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from

[`MathError`](./MathError).[`stack`](./MathError#stack)
