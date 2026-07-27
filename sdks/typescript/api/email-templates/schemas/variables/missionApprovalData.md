# Variable: missionApprovalData

&gt; `const` **missionApprovalData**: `Struct`\<\{ `approveUrl`: `String`; `expiresInMinutes`: `optional`\<`Number`\>; `missionId`: `NonEmptyString`; `requestedBy`: `optional`\<`String`\>; `severity`: `optional`\<`Literals`\<readonly \[`"info"`, `"warning"`, `"critical"`\]\>\>; `summary`: `optional`\<`String`\>; `title`: `NonEmptyString`; \}\>

Defined in: [packages/email-templates/src/schemas.ts:136](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/schemas.ts#L136)

`data` schema for the mission-approval sign-off request.
