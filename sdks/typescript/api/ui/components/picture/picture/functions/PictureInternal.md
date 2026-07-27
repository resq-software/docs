# Function: PictureInternal()

&gt; **PictureInternal**\<`TRootElement`\>(`__namedParameters`): `Element`

Defined in: [packages/ui/src/components/picture/picture.tsx:229](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/picture/picture.tsx#L229)

Generic implementation of the Picture component. Prefer the [Picture](../variables/Picture)
alias, which carries the overloaded call signatures (Picture.Type) that
infer props from the `component` root element.

Tracks its own `isLoading` state to drive the blur-up placeholder and
`aria-busy`. The built-in `onError` handler calls `console.warn` with the
failed `src` (in addition to invoking any caller-supplied `onError`), unless
the caller calls `preventDefault()` on the event.

## Type Parameters

### TRootElement

`TRootElement` *extends* `BaseRootElementType` = `"img"`

The rendered root element type (defaults to `"img"`);
  set via the `component` prop and used to infer the forwarded props.

## Parameters

### \_\_namedParameters

`Props`\<`TRootElement`\>

## Returns

`Element`
