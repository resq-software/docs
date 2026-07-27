# Variable: missionApprovalTemplate

&gt; `const` **missionApprovalTemplate**: [`EmailTemplateDef`](../../mailer/interfaces/EmailTemplateDef)\<`"mission-approval"`, `Struct`\<\{ `approveUrl`: `String`; `expiresInMinutes`: `optional`\<`Number`\>; `missionId`: `NonEmptyString`; `requestedBy`: `optional`\<`String`\>; `severity`: `optional`\<`Literals`\<readonly \[`"info"`, `"warning"`, `"critical"`\]\>\>; `summary`: `optional`\<`String`\>; `title`: `NonEmptyString`; \}\>\>

Defined in: [packages/email-templates/src/templates.tsx:104](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/templates.tsx#L104)

Mission-approval sign-off request template.
