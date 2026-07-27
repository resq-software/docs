# Variable: incidentAlertTemplate

&gt; `const` **incidentAlertTemplate**: [`EmailTemplateDef`](../../mailer/interfaces/EmailTemplateDef)\<`"incident-alert"`, `Struct`\<\{ `dashboardUrl`: `String`; `detectedAt`: `optional`\<`String`\>; `incidentId`: `NonEmptyString`; `location`: `optional`\<`String`\>; `severity`: `Literals`\<readonly \[`"info"`, `"warning"`, `"critical"`\]\>; `summary`: `NonEmptyString`; `title`: `NonEmptyString`; \}\>\>

Defined in: [packages/email-templates/src/templates.tsx:80](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/templates.tsx#L80)

Incident / dispatch alert template.
