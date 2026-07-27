# Function: MissionApprovalEmail()

&gt; **MissionApprovalEmail**(`__namedParameters`): `Element`

Defined in: [packages/email-templates/src/emails/mission-approval.tsx:36](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/mission-approval.tsx#L36)

Approver sign-off request for a ResQ Systems mission / plan execution.

## Parameters

### \_\_namedParameters

#### approveUrl

`string` = `"https://app.example.com/missions/approve"`

#### expiresInMinutes?

`number`

#### missionId

`string`

#### requestedBy?

`string`

#### severity?

`"info"` \| `"warning"` \| `"critical"`

#### summary?

`string`

#### title

`string`

## Returns

`Element`
