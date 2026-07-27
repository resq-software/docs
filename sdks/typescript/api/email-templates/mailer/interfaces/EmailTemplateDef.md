# Interface: EmailTemplateDef\<Name, DataSchema\>

Defined in: [packages/email-templates/src/mailer.tsx:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L64)

A template definition: its discriminant [EmailTemplateDef.name](#name-1), `data`
schema, subject builder, and React component.

`name` must be unique across the defs handed to [createMailer](../functions/createMailer) — it is the
payload union's discriminant, and a later def with a duplicate name silently
overwrites the earlier one in the registry (last write wins in
`Object.fromEntries`). `subject` and `Component` are only ever invoked with data
that has already cleared `data`'s schema at the decode boundary, so they may
treat every field as valid and should stay pure.

## Type Parameters

### Name

`Name` *extends* `string`

The literal template name (e.g. `"otp"`); the payload discriminant.

### DataSchema

`DataSchema` *extends* `Schema.Top`

The Effect Schema whose decoded `Type` is this template's `data`.

## Properties

### Component

&gt; `readonly` **Component**: (`data`) =&gt; `ReactElement`

Defined in: [packages/email-templates/src/mailer.tsx:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L72)

Renders the email body from already-validated `data`.

#### Parameters

##### data

`DataSchema`\[`"Type"`\]

#### Returns

`ReactElement`

***

### data

&gt; `readonly` **data**: `DataSchema`

Defined in: [packages/email-templates/src/mailer.tsx:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L68)

Effect Schema that validates this template's `data` at the decode boundary.

***

### name

&gt; `readonly` **name**: `Name`

Defined in: [packages/email-templates/src/mailer.tsx:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L66)

Unique template name; the payload union's discriminant.

***

### subject

&gt; `readonly` **subject**: (`data`) =&gt; `string`

Defined in: [packages/email-templates/src/mailer.tsx:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L70)

Builds the subject line from already-validated `data`. Should be pure.

#### Parameters

##### data

`DataSchema`\[`"Type"`\]

#### Returns

`string`
