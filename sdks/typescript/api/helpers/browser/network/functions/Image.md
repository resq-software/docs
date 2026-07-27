# Function: Image()

&gt; **Image**(`width?`, `height?`): `HTMLImageElement`

Defined in: [packages/helpers/src/browser/network.ts:57](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/network.ts#L57)

**`Internal`**

Just a wrapper around `new Image`, and yeah, it's a bit strange that it's in the network.ts file
but the main concern here is the referrerPolicy and setting it correctly.

## Parameters

### width?

`number`

Optional width for the image element

### height?

`number`

Optional height for the image element

## Returns

`HTMLImageElement`

HTMLImageElement with referrerPolicy set to 'strict-origin-when-cross-origin'
