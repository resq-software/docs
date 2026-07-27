# Function: defineEmailTemplate()

&gt; **defineEmailTemplate**\<`Name`, `DataSchema`\>(`def`): [`EmailTemplateDef`](../interfaces/EmailTemplateDef)\<`Name`, `DataSchema`\>

Defined in: [packages/email-templates/src/mailer.tsx:87](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L87)

Identity helper that infers and preserves a template def's literal types.

Pure — returns `def` by reference, unchanged. It exists only so the `const` type
parameters capture the literal `name` and the schema's `Type` at the call site;
a bare object literal would widen `name` to `string` and lose the discriminant.

## Type Parameters

### Name

`Name` *extends* `string`

The literal template name; preserved via the `const` modifier.

### DataSchema

`DataSchema` *extends* `Top`

The template's `data` schema.

## Parameters

### def

[`EmailTemplateDef`](../interfaces/EmailTemplateDef)\<`Name`, `DataSchema`\>

The template definition to brand with its inferred literal types.

## Returns

[`EmailTemplateDef`](../interfaces/EmailTemplateDef)\<`Name`, `DataSchema`\>

The same `def` object, typed with its narrowed literals.
