# Class: ManualPromise\<T\>

Defined in: [packages/helpers/src/utils/manual-promise.ts:53](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/manual-promise.ts#L53)

A Promise whose settlement is controlled from the outside via
[resolve](#resolve-1) / [reject](#reject-1)
— the classic "deferred" primitive. Useful for bridging callback/event APIs
into `async`/`await`, or for handing a value off between a producer and a
consumer that don't share a call stack.

It extends the native `Promise`, so it is awaitable and `.then`-able directly.
Chained operations (`.then`, `.catch`, `.finally`) return plain `Promise`s via
`Symbol.species`, not `ManualPromise`s.

## Example

```ts
const ready = new ManualPromise<number>();
setTimeout(() => ready.resolve(42), 10);
const value = await ready; // → 42
ready.isDone(); // → true
```

## Extends

- `Promise`\<`T`\>

## Type Parameters

### T

`T` = `void`

The resolved value type (defaults to `void`).

## Constructors

### Constructor

&gt; **new ManualPromise**\<`T`\>(): `ManualPromise`\<`T`\>

Defined in: [packages/helpers/src/utils/manual-promise.ts:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/manual-promise.ts#L58)

#### Returns

`ManualPromise`\<`T`\>

#### Overrides

`Promise<T>.constructor`

## Accessors

### \[toStringTag\]

#### Get Signature

&gt; **get** **\[toStringTag\]**(): `string`

Defined in: [packages/helpers/src/utils/manual-promise.ts:92](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/manual-promise.ts#L92)

##### Returns

`string`

#### Overrides

`Promise.[toStringTag]`

***

### \[species\]

#### Get Signature

&gt; **get** `static` **\[species\]**(): `PromiseConstructor`

Defined in: [packages/helpers/src/utils/manual-promise.ts:88](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/manual-promise.ts#L88)

##### Returns

`PromiseConstructor`

#### Overrides

`Promise.[species]`

## Methods

### catch()

#### Call Signature

&gt; **catch**\<`TResult`\>(`onrejected?`): `Promise`\<`T` \| `TResult`\>

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1562

Attaches a callback for only the rejection of the Promise.

##### Type Parameters

###### TResult

`TResult` = `never`

##### Parameters

###### onrejected?

((`reason`) =&gt; `TResult` \| `PromiseLike`\<`TResult`\>) \| `null`

The callback to execute when the Promise is rejected.

##### Returns

`Promise`\<`T` \| `TResult`\>

A Promise for the completion of the callback.

##### Inherited from

`Promise.catch`

#### Call Signature

&gt; **catch**\<`TResult`\>(`onrejected?`): `Promise`\<`T` \| `TResult`\>

Defined in: node\_modules/@total-typescript/ts-reset/dist/promise-catch.d.ts:24

Attaches a callback for only the rejection of the Promise.

##### Type Parameters

###### TResult

`TResult` = `never`

##### Parameters

###### onrejected?

((`reason`) =&gt; `TResult` \| `PromiseLike`\<`TResult`\>) \| `null`

The callback to execute when the Promise is rejected.

##### Returns

`Promise`\<`T` \| `TResult`\>

A Promise for the completion of the callback.

##### Inherited from

`Promise.catch`

***

### finally()

&gt; **finally**(`onfinally?`): `Promise`\<`T`\>

Defined in: node\_modules/typescript/lib/lib.es2018.promise.d.ts:27

Attaches a callback that is invoked when the Promise is settled (fulfilled or rejected). The
resolved value cannot be modified from the callback.

#### Parameters

##### onfinally?

(() =&gt; `void`) \| `null`

The callback to execute when the Promise is settled (fulfilled or rejected).

#### Returns

`Promise`\<`T`\>

A Promise for the completion of the callback.

#### Inherited from

`Promise.finally`

***

### isDone()

&gt; **isDone**(): `boolean`

Defined in: [packages/helpers/src/utils/manual-promise.ts:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/manual-promise.ts#L70)

#### Returns

`boolean`

`true` once the promise has been resolved or rejected.

***

### reject()

&gt; **reject**(`reason?`): `void`

Defined in: [packages/helpers/src/utils/manual-promise.ts:81](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/manual-promise.ts#L81)

Reject the promise with `reason` (any value, matching native `Promise`).

#### Parameters

##### reason?

`unknown`

#### Returns

`void`

***

### resolve()

&gt; **resolve**(`value`): `void`

Defined in: [packages/helpers/src/utils/manual-promise.ts:75](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/manual-promise.ts#L75)

Resolve the promise with `value`.

#### Parameters

##### value

`T`

#### Returns

`void`

***

### then()

#### Call Signature

&gt; **then**\<`TResult1`, `TResult2`\>(`onfulfilled?`, `onrejected?`): `Promise`\<`TResult1` \| `TResult2`\>

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1555

Attaches callbacks for the resolution and/or rejection of the Promise.

##### Type Parameters

###### TResult1

`TResult1` = `T`

###### TResult2

`TResult2` = `never`

##### Parameters

###### onfulfilled?

((`value`) =&gt; `TResult1` \| `PromiseLike`\<`TResult1`\>) \| `null`

The callback to execute when the Promise is resolved.

###### onrejected?

((`reason`) =&gt; `TResult2` \| `PromiseLike`\<`TResult2`\>) \| `null`

The callback to execute when the Promise is rejected.

##### Returns

`Promise`\<`TResult1` \| `TResult2`\>

A Promise for the completion of which ever callback is executed.

##### Inherited from

`Promise.then`

#### Call Signature

&gt; **then**\<`TResult1`, `TResult2`\>(`onfulfilled?`, `onrejected?`): `Promise`\<`TResult1` \| `TResult2`\>

Defined in: node\_modules/@total-typescript/ts-reset/dist/promise-catch.d.ts:8

Attaches callbacks for the resolution and/or rejection of the Promise.

##### Type Parameters

###### TResult1

`TResult1` = `T`

###### TResult2

`TResult2` = `never`

##### Parameters

###### onfulfilled?

((`value`) =&gt; `TResult1` \| `PromiseLike`\<`TResult1`\>) \| `null`

The callback to execute when the Promise is resolved.

###### onrejected?

((`reason`) =&gt; `TResult2` \| `PromiseLike`\<`TResult2`\>) \| `null`

The callback to execute when the Promise is rejected.

##### Returns

`Promise`\<`TResult1` \| `TResult2`\>

A Promise for the completion of which ever callback is executed.

##### Inherited from

`Promise.then`

***

### all()

#### Call Signature

&gt; `static` **all**\<`T`\>(`values`): `Promise`\<`Awaited`\<`T`\>[]\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:253

Creates a Promise that is resolved with an array of results when all of the provided Promises
resolve, or rejected when any Promise is rejected.

##### Type Parameters

###### T

`T`

##### Parameters

###### values

`Iterable`\<`T` \| `PromiseLike`\<`T`\>\>

An iterable of Promises.

##### Returns

`Promise`\<`Awaited`\<`T`\>[]\>

A new Promise.

##### Inherited from

`Promise.all`

#### Call Signature

&gt; `static` **all**\<`T`\>(`values`): `Promise`\<\{ -readonly \[P in string \| number \| symbol\]: Awaited\<T\[P\]\> \}\>

Defined in: node\_modules/typescript/lib/lib.es2015.promise.d.ts:37

Creates a Promise that is resolved with an array of results when all of the provided Promises
resolve, or rejected when any Promise is rejected.

##### Type Parameters

###### T

`T` *extends* readonly `unknown`[] \| \[\]

##### Parameters

###### values

`T`

An array of Promises.

##### Returns

`Promise`\<\{ -readonly \[P in string \| number \| symbol\]: Awaited\<T\[P\]\> \}\>

A new Promise.

##### Inherited from

`Promise.all`

***

### allSettled()

#### Call Signature

&gt; `static` **allSettled**\<`T`\>(`values`): `Promise`\<\{ -readonly \[P in string \| number \| symbol\]: PromiseSettledResult\<Awaited\<T\[P\]\>\> \}\>

Defined in: node\_modules/typescript/lib/lib.es2020.promise.d.ts:36

Creates a Promise that is resolved with an array of results when all
of the provided Promises resolve or reject.

##### Type Parameters

###### T

`T` *extends* readonly `unknown`[] \| \[\]

##### Parameters

###### values

`T`

An array of Promises.

##### Returns

`Promise`\<\{ -readonly \[P in string \| number \| symbol\]: PromiseSettledResult\<Awaited\<T\[P\]\>\> \}\>

A new Promise.

##### Inherited from

`Promise.allSettled`

#### Call Signature

&gt; `static` **allSettled**\<`T`\>(`values`): `Promise`\<`PromiseSettledResult`\<`Awaited`\<`T`\>\>[]\>

Defined in: node\_modules/typescript/lib/lib.es2020.promise.d.ts:44

Creates a Promise that is resolved with an array of results when all
of the provided Promises resolve or reject.

##### Type Parameters

###### T

`T`

##### Parameters

###### values

`Iterable`\<`T` \| `PromiseLike`\<`T`\>\>

An array of Promises.

##### Returns

`Promise`\<`PromiseSettledResult`\<`Awaited`\<`T`\>\>[]\>

A new Promise.

##### Inherited from

`Promise.allSettled`

***

### any()

#### Call Signature

&gt; `static` **any**\<`T`\>(`values`): `Promise`\<`Awaited`\<`T`\[`number`\]\>\>

Defined in: node\_modules/typescript/lib/lib.es2021.promise.d.ts:38

The any function returns a promise that is fulfilled by the first given promise to be fulfilled, or rejected with an AggregateError containing an array of rejection reasons if all of the given promises are rejected. It resolves all elements of the passed iterable to promises as it runs this algorithm.

##### Type Parameters

###### T

`T` *extends* readonly `unknown`[] \| \[\]

##### Parameters

###### values

`T`

An array or iterable of Promises.

##### Returns

`Promise`\<`Awaited`\<`T`\[`number`\]\>\>

A new Promise.

##### Inherited from

`Promise.any`

#### Call Signature

&gt; `static` **any**\<`T`\>(`values`): `Promise`\<`Awaited`\<`T`\>\>

Defined in: node\_modules/typescript/lib/lib.es2021.promise.d.ts:45

The any function returns a promise that is fulfilled by the first given promise to be fulfilled, or rejected with an AggregateError containing an array of rejection reasons if all of the given promises are rejected. It resolves all elements of the passed iterable to promises as it runs this algorithm.

##### Type Parameters

###### T

`T`

##### Parameters

###### values

`Iterable`\<`T` \| `PromiseLike`\<`T`\>\>

An array or iterable of Promises.

##### Returns

`Promise`\<`Awaited`\<`T`\>\>

A new Promise.

##### Inherited from

`Promise.any`

***

### race()

#### Call Signature

&gt; `static` **race**\<`T`\>(`values`): `Promise`\<`Awaited`\<`T`\>\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:261

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved
or rejected.

##### Type Parameters

###### T

`T`

##### Parameters

###### values

`Iterable`\<`T` \| `PromiseLike`\<`T`\>\>

An iterable of Promises.

##### Returns

`Promise`\<`Awaited`\<`T`\>\>

A new Promise.

##### Inherited from

`Promise.race`

#### Call Signature

&gt; `static` **race**\<`T`\>(`values`): `Promise`\<`Awaited`\<`T`\[`number`\]\>\>

Defined in: node\_modules/typescript/lib/lib.es2015.promise.d.ts:48

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved
or rejected.

##### Type Parameters

###### T

`T` *extends* readonly `unknown`[] \| \[\]

##### Parameters

###### values

`T`

An array of Promises.

##### Returns

`Promise`\<`Awaited`\<`T`\[`number`\]\>\>

A new Promise.

##### Inherited from

`Promise.race`

***

### reject()

&gt; `static` **reject**\<`T`\>(`reason?`): `Promise`\<`T`\>

Defined in: node\_modules/typescript/lib/lib.es2015.promise.d.ts:58

Creates a new rejected promise for the provided reason.

#### Type Parameters

##### T

`T` = `never`

#### Parameters

##### reason?

`any`

The reason the promise was rejected.

#### Returns

`Promise`\<`T`\>

A new rejected Promise.

#### Inherited from

`Promise.reject`

***

### resolve()

#### Call Signature

&gt; `static` **resolve**(): `Promise`\<`void`\>

Defined in: node\_modules/typescript/lib/lib.es2015.promise.d.ts:64

Creates a new resolved promise.

##### Returns

`Promise`\<`void`\>

A resolved promise.

##### Inherited from

`Promise.resolve`

#### Call Signature

&gt; `static` **resolve**\<`T`\>(`value`): `Promise`\<`Awaited`\<`T`\>\>

Defined in: node\_modules/typescript/lib/lib.es2015.promise.d.ts:70

Creates a new resolved promise for the provided value.

##### Type Parameters

###### T

`T`

##### Parameters

###### value

`T`

A promise.

##### Returns

`Promise`\<`Awaited`\<`T`\>\>

A promise whose internal state matches the provided promise.

##### Inherited from

`Promise.resolve`

#### Call Signature

&gt; `static` **resolve**\<`T`\>(`value`): `Promise`\<`Awaited`\<`T`\>\>

Defined in: node\_modules/typescript/lib/lib.es2015.promise.d.ts:76

Creates a new resolved promise for the provided value.

##### Type Parameters

###### T

`T`

##### Parameters

###### value

`T` \| `PromiseLike`\<`T`\>

A promise.

##### Returns

`Promise`\<`Awaited`\<`T`\>\>

A promise whose internal state matches the provided promise.

##### Inherited from

`Promise.resolve`
