# Function: createMailer()

&gt; **createMailer**\<`Defs`\>(`defs`): [`Mailer`](../interfaces/Mailer)\<`PayloadFor`\<`Defs`\[`number`\]\>\>

Defined in: [packages/email-templates/src/mailer.tsx:260](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L260)

Compose template definitions into a typed mailer: a discriminated
`{ name, to, data }` contract, a boundary decoder, a registry, and a headless
renderer. Spread the built-in `resqEmailTemplates` and add your own — each
template's `data` is validated by its Effect Schema.

Pure: builds the schema union and registry eagerly and holds no mutable state;
the returned `decode`/`renderEmail` are the only fallible surfaces. `defs`
should have unique `name`s — a duplicate makes the later def win in the registry
while both remain in the schema union (see [EmailTemplateDef](../interfaces/EmailTemplateDef)).

## Type Parameters

### Defs

`Defs` *extends* readonly `AnyTemplateDef`[]

The `as const` tuple of template defs to compose.

## Parameters

### defs

`Defs`

The template definitions; pass `[...resqEmailTemplates, myDef]` to extend the built-ins.

## Returns

[`Mailer`](../interfaces/Mailer)\<`PayloadFor`\<`Defs`\[`number`\]\>\>

A [Mailer](../interfaces/Mailer) whose `decode` throws (and `renderEmail` rejects with)
  [EmailValidationError](../classes/EmailValidationError) on invalid input.

## Example

```ts
const mailer = createMailer(resqEmailTemplates);
const { subject } = await mailer.renderEmail({
  name: "otp",
  to: "user@example.com",
  data: { code: "123456" },
});
subject; // → "Your ResQ Systems verification code: 123456"
```
