# Variable: STRUCTURED\_CLONE\_OBJECT\_PROTOTYPE

&gt; `const` **STRUCTURED\_CLONE\_OBJECT\_PROTOTYPE**: `any`

Defined in: [packages/helpers/src/utils/value.ts:178](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/value.ts#L178)

**`Internal`**

The prototype object used by structuredClone for cloned objects.
When we patch structuredClone in jsdom for testing (see https://github.com/jsdom/jsdom/issues/3363),
the Object that is used as a prototype for the cloned object is not the same as the Object in
the code under test (that comes from jsdom's fake global context). This constant is used in
our code to work around this case.

This is also the case for Array prototype, but that problem can be worked around with an
Array.isArray() check.
