# Function: NotificationEmail()

&gt; **NotificationEmail**(`__namedParameters`): `Element`

Defined in: [packages/email-templates/src/emails/notification.tsx:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/notification.tsx#L38)

Generic notification / alert email with an optional call-to-action.

## Parameters

### \_\_namedParameters

#### actionLabel?

`string`

#### actionUrl?

`string`

#### body

`string`

#### severity?

`"info"` \| `"success"` \| `"warning"` \| `"error"` = `"info"`

#### title

`string`

## Returns

`Element`
