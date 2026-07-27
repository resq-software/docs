# Class: MathError

Defined in: [packages/math/src/error.ts:36](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L36)

Base class for all math engine errors.

Every error the engine throws is an instance of this class, so `catch (e) { if
(e instanceof MathError) … &#125;` reliably distinguishes engine failures from
unrelated exceptions. Each subclass overrides `name` to its own class name and
fixes a distinct [code](#code); the pair `(name, code)` is stable across
releases and safe to switch on, whereas `message` is human-facing and may change.

## Extends

- `Error`

## Extended by

- [`SortError`](./SortError)
- [`UnboundVariableError`](./UnboundVariableError)
- [`UndefinedOpError`](./UndefinedOpError)
- [`DomainError`](./DomainError)
- [`ParseError`](./ParseError)
- [`StackError`](./StackError)
- [`ExecutionLimitError`](./ExecutionLimitError)
- [`RecursionLimitError`](./RecursionLimitError)

## Constructors

### Constructor

&gt; **new MathError**(`code`, `message`): `MathError`

Defined in: [packages/math/src/error.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L44)

#### Parameters

##### code

`string`

Stable machine-readable error code.

##### message

`string`

Human-readable description.

#### Returns

`MathError`

#### Overrides

`Error.constructor`

## Properties

### cause?

&gt; `optional` **cause?**: `unknown`

Defined in: node\_modules/typescript/lib/lib.es2022.error.d.ts:24

#### Inherited from

`Error.cause`

***

### code

&gt; `readonly` **code**: `string`

Defined in: [packages/math/src/error.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/error.ts#L38)

Stable machine-readable error code (e.g. `"SORT_ERROR"`); constant per subclass.

***

### message

&gt; **message**: `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1075

#### Inherited from

`Error.message`

***

### name

&gt; **name**: `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1074

#### Inherited from

`Error.name`

***

### stack?

&gt; `optional` **stack?**: `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1076

#### Inherited from

`Error.stack`
