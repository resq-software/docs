# Interface: EmailRegistryEntry

Defined in: [packages/email-templates/src/mailer.tsx:185](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L185)

A registry entry: the subject builder and component renderer for one template.

Both functions take `unknown` because the registry is keyed by name and has
erased each def's `data` type. They must only be called with data that has
already passed that template's schema (as [Mailer.renderEmail](./Mailer#renderemail) does after
[Mailer.decode](./Mailer#decode)); calling them with unvalidated data is unsound.

## Properties

### render

&gt; **render**: (`data`) =&gt; `ReactElement`

Defined in: [packages/email-templates/src/mailer.tsx:189](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L189)

Renders the body element from validated `data` (typed `unknown` after name-erasure).

#### Parameters

##### data

`unknown`

#### Returns

`ReactElement`

***

### subject

&gt; **subject**: (`data`) =&gt; `string`

Defined in: [packages/email-templates/src/mailer.tsx:187](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L187)

Builds the subject from validated `data` (typed `unknown` after name-erasure).

#### Parameters

##### data

`unknown`

#### Returns

`string`
