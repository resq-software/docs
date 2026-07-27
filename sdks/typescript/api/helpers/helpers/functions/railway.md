# Function: railway()

## Call Signature

&gt; **railway**\<`TInput`, `T1`, `E`\>(`input`, `fn1`): `Result`\<`T1`, `E`\>

Defined in: [packages/helpers/src/helpers.ts:282](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L282)

Compose up to five `Result`-returning steps over an input value,
short-circuiting on the first Failure.

Each step receives the previous step's success value and may return a
new `Success` (continuing the pipeline) or a `Failure` (stopping it).
The first failure is returned verbatim — later steps are not invoked.

### Type Parameters

#### TInput

`TInput`

#### T1

`T1`

#### E

`E`

### Parameters

#### input

`TInput`

Initial value piped into `fn1`.

#### fn1

(`input`) =&gt; `Result`\<`T1`, `E`\>

### Returns

`Result`\<`T1`, `E`\>

Final `Result` from the last step that ran.

### Example

```ts
railway(
  rawInput,
  parse,        // (raw) => Result<Parsed, ValidationError>
  normalize,    // (p)   => Result<Parsed, ValidationError>
  persist,      // (p)   => Result<Saved,  DatabaseError>
);
```

## Call Signature

&gt; **railway**\<`TInput`, `T1`, `T2`, `E`\>(`input`, `fn1`, `fn2`): `Result`\<`T2`, `E`\>

Defined in: [packages/helpers/src/helpers.ts:286](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L286)

Compose up to five `Result`-returning steps over an input value,
short-circuiting on the first Failure.

Each step receives the previous step's success value and may return a
new `Success` (continuing the pipeline) or a `Failure` (stopping it).
The first failure is returned verbatim — later steps are not invoked.

### Type Parameters

#### TInput

`TInput`

#### T1

`T1`

#### T2

`T2`

#### E

`E`

### Parameters

#### input

`TInput`

Initial value piped into `fn1`.

#### fn1

(`input`) =&gt; `Result`\<`T1`, `E`\>

#### fn2

(`input`) =&gt; `Result`\<`T2`, `E`\>

### Returns

`Result`\<`T2`, `E`\>

Final `Result` from the last step that ran.

### Example

```ts
railway(
  rawInput,
  parse,        // (raw) => Result<Parsed, ValidationError>
  normalize,    // (p)   => Result<Parsed, ValidationError>
  persist,      // (p)   => Result<Saved,  DatabaseError>
);
```

## Call Signature

&gt; **railway**\<`TInput`, `T1`, `T2`, `T3`, `E`\>(`input`, `fn1`, `fn2`, `fn3`): `Result`\<`T3`, `E`\>

Defined in: [packages/helpers/src/helpers.ts:291](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L291)

Compose up to five `Result`-returning steps over an input value,
short-circuiting on the first Failure.

Each step receives the previous step's success value and may return a
new `Success` (continuing the pipeline) or a `Failure` (stopping it).
The first failure is returned verbatim — later steps are not invoked.

### Type Parameters

#### TInput

`TInput`

#### T1

`T1`

#### T2

`T2`

#### T3

`T3`

#### E

`E`

### Parameters

#### input

`TInput`

Initial value piped into `fn1`.

#### fn1

(`input`) =&gt; `Result`\<`T1`, `E`\>

#### fn2

(`input`) =&gt; `Result`\<`T2`, `E`\>

#### fn3

(`input`) =&gt; `Result`\<`T3`, `E`\>

### Returns

`Result`\<`T3`, `E`\>

Final `Result` from the last step that ran.

### Example

```ts
railway(
  rawInput,
  parse,        // (raw) => Result<Parsed, ValidationError>
  normalize,    // (p)   => Result<Parsed, ValidationError>
  persist,      // (p)   => Result<Saved,  DatabaseError>
);
```

## Call Signature

&gt; **railway**\<`TInput`, `T1`, `T2`, `T3`, `T4`, `E`\>(`input`, `fn1`, `fn2`, `fn3`, `fn4`): `Result`\<`T4`, `E`\>

Defined in: [packages/helpers/src/helpers.ts:297](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L297)

Compose up to five `Result`-returning steps over an input value,
short-circuiting on the first Failure.

Each step receives the previous step's success value and may return a
new `Success` (continuing the pipeline) or a `Failure` (stopping it).
The first failure is returned verbatim — later steps are not invoked.

### Type Parameters

#### TInput

`TInput`

#### T1

`T1`

#### T2

`T2`

#### T3

`T3`

#### T4

`T4`

#### E

`E`

### Parameters

#### input

`TInput`

Initial value piped into `fn1`.

#### fn1

(`input`) =&gt; `Result`\<`T1`, `E`\>

#### fn2

(`input`) =&gt; `Result`\<`T2`, `E`\>

#### fn3

(`input`) =&gt; `Result`\<`T3`, `E`\>

#### fn4

(`input`) =&gt; `Result`\<`T4`, `E`\>

### Returns

`Result`\<`T4`, `E`\>

Final `Result` from the last step that ran.

### Example

```ts
railway(
  rawInput,
  parse,        // (raw) => Result<Parsed, ValidationError>
  normalize,    // (p)   => Result<Parsed, ValidationError>
  persist,      // (p)   => Result<Saved,  DatabaseError>
);
```

## Call Signature

&gt; **railway**\<`TInput`, `T1`, `T2`, `T3`, `T4`, `T5`, `E`\>(`input`, `fn1`, `fn2`, `fn3`, `fn4`, `fn5`): `Result`\<`T5`, `E`\>

Defined in: [packages/helpers/src/helpers.ts:304](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L304)

Compose up to five `Result`-returning steps over an input value,
short-circuiting on the first Failure.

Each step receives the previous step's success value and may return a
new `Success` (continuing the pipeline) or a `Failure` (stopping it).
The first failure is returned verbatim — later steps are not invoked.

### Type Parameters

#### TInput

`TInput`

#### T1

`T1`

#### T2

`T2`

#### T3

`T3`

#### T4

`T4`

#### T5

`T5`

#### E

`E`

### Parameters

#### input

`TInput`

Initial value piped into `fn1`.

#### fn1

(`input`) =&gt; `Result`\<`T1`, `E`\>

#### fn2

(`input`) =&gt; `Result`\<`T2`, `E`\>

#### fn3

(`input`) =&gt; `Result`\<`T3`, `E`\>

#### fn4

(`input`) =&gt; `Result`\<`T4`, `E`\>

#### fn5

(`input`) =&gt; `Result`\<`T5`, `E`\>

### Returns

`Result`\<`T5`, `E`\>

Final `Result` from the last step that ran.

### Example

```ts
railway(
  rawInput,
  parse,        // (raw) => Result<Parsed, ValidationError>
  normalize,    // (p)   => Result<Parsed, ValidationError>
  persist,      // (p)   => Result<Saved,  DatabaseError>
);
```
