# Function: beginDOMCaches()

&gt; **beginDOMCaches**(): `void`

Defined in: [packages/helpers/src/browser/dom-utils.ts:243](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/dom-utils.ts#L243)

Begin a computed-style caching scope. Nestable — pair with [endDOMCaches](./endDOMCaches).
While active, [getElementComputedStyle](./getElementComputedStyle) memoizes results per element.

## Returns

`void`
