# Function: elementSafeTagName()

&gt; **elementSafeTagName**(`element`): `string`

Defined in: [packages/helpers/src/browser/dom-utils.ts:218](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/dom-utils.ts#L218)

The element's tag name in upper case, resilient to named form fields that
shadow `tagName` (e.g. `<input name="tagName">`).

## Parameters

### element

`Element`

## Returns

`string`
