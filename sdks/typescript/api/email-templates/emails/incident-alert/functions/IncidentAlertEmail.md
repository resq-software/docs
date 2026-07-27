# Function: IncidentAlertEmail()

&gt; **IncidentAlertEmail**(`__namedParameters`): `Element`

Defined in: [packages/email-templates/src/emails/incident-alert.tsx:37](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/incident-alert.tsx#L37)

Incident / dispatch alert for ResQ Systems disaster-response operators.

## Parameters

### \_\_namedParameters

#### dashboardUrl

`string` = `"https://app.resq.software/incidents"`

#### detectedAt?

`string`

#### incidentId

`string`

#### location?

`string`

#### severity

`"info"` \| `"warning"` \| `"critical"` = `"warning"`

#### summary

`string`

#### title

`string`

## Returns

`Element`
