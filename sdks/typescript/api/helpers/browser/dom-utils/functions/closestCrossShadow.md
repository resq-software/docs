# Function: closestCrossShadow()

&gt; **closestCrossShadow**(`element`, `css`, `scope?`): `Element` \| `undefined`

Defined in: [packages/helpers/src/browser/dom-utils.ts:112](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/dom-utils.ts#L112)

Like `Element.closest`, but crosses shadow boundaries. If `scope` is
provided, `element` is assumed to be inside `scope`'s subtree.

## Parameters

### element

`Element` \| `undefined`

### css

`string`

### scope?

`Element` \| `Document`

## Returns

`Element` \| `undefined`
