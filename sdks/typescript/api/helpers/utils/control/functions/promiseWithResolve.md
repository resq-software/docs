# Function: promiseWithResolve()

&gt; **promiseWithResolve**\<`T`\>(): `Promise`\<`T`\> & `object`

Defined in: [packages/helpers/src/utils/control.ts:300](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L300)

**`Internal`**

Create a Promise with externally accessible resolve and reject functions.

Creates a Promise along with its resolve and reject functions exposed as
properties on the returned object. This allows external code to control when the
Promise resolves or rejects, useful for coordination between async operations.

## Type Parameters

### T

`T`

## Returns

`Promise`\<`T`\> & `object`

A Promise object with additional resolve and reject methods

## Example

```ts
const deferred = promiseWithResolve<string>()

// Set up the promise consumer
deferred.then(value => console.log(`Resolved: ${value}`))
deferred.catch(error => console.error(`Rejected: ${error}`))

// Later, resolve from external code
setTimeout(() => {
  deferred.resolve('Hello World')
}, 1000)
```
