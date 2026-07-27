# Variable: decodeEmailPayload

&gt; `const` **decodeEmailPayload**: (`input`) =&gt; \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `code`: `string`; `expiresInMinutes?`: `number`; `firstName?`: `string`; \}; `name`: `"otp"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} \| \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `firstName`: `string`; `verifyUrl?`: `string`; \}; `name`: `"welcome"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} \| \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `expiresInMinutes?`: `number`; `firstName?`: `string`; `resetUrl`: `string`; \}; `name`: `"password-reset"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} \| \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `actionLabel?`: `string`; `actionUrl?`: `string`; `body`: `string`; `severity?`: `"info"` \| `"success"` \| `"warning"` \| `"error"`; `title`: `string`; \}; `name`: `"notification"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} \| \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `dashboardUrl`: `string`; `detectedAt?`: `string`; `incidentId`: `string`; `location?`: `string`; `severity`: `"info"` \| `"warning"` \| `"critical"`; `summary`: `string`; `title`: `string`; \}; `name`: `"incident-alert"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} \| \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `changedAt?`: `string`; `firstName?`: `string`; `secureAccountUrl?`: `string`; \}; `name`: `"password-changed"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} \| \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `at?`: `string`; `device?`: `string`; `firstName?`: `string`; `ipAddress?`: `string`; `location?`: `string`; `secureAccountUrl?`: `string`; \}; `name`: `"new-device-login"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} \| \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `approveUrl`: `string`; `expiresInMinutes?`: `number`; `missionId`: `string`; `requestedBy?`: `string`; `severity?`: `"info"` \| `"warning"` \| `"critical"`; `summary?`: `string`; `title`: `string`; \}; `name`: `"mission-approval"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} \| \{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `acceptUrl`: `string`; `expiresInDays?`: `number`; `inviterName?`: `string`; `orgName`: `string`; `orgRole?`: `string`; \}; `name`: `"org-invitation"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \} = `resqMailer.decode`

Defined in: [packages/email-templates/src/contract.ts:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/contract.ts#L58)

Validate an untrusted `{ name, to, data }` payload at the system boundary.

Validate an untrusted payload against the contract union and return the
narrowed [Payload](../../mailer/interfaces/Mailer#payload).

## Parameters

### input

`unknown`

Untrusted `{ name, to, data }` value from the boundary.

## Returns

The validated, branded payload.

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `code`: `string`; `expiresInMinutes?`: `number`; `firstName?`: `string`; \}; `name`: `"otp"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.code

&gt; `readonly` **code**: `string` = `S.NonEmptyString`

##### data.expiresInMinutes?

&gt; `readonly` `optional` **expiresInMinutes?**: `number`

##### data.firstName?

&gt; `readonly` `optional` **firstName?**: `string`

#### name

&gt; `readonly` **name**: `"otp"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

***

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `firstName`: `string`; `verifyUrl?`: `string`; \}; `name`: `"welcome"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.firstName

&gt; `readonly` **firstName**: `string` = `S.NonEmptyString`

##### data.verifyUrl?

&gt; `readonly` `optional` **verifyUrl?**: `string`

#### name

&gt; `readonly` **name**: `"welcome"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

***

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `expiresInMinutes?`: `number`; `firstName?`: `string`; `resetUrl`: `string`; \}; `name`: `"password-reset"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.expiresInMinutes?

&gt; `readonly` `optional` **expiresInMinutes?**: `number`

##### data.firstName?

&gt; `readonly` `optional` **firstName?**: `string`

##### data.resetUrl

&gt; `readonly` **resetUrl**: `string` = `HttpUrl`

#### name

&gt; `readonly` **name**: `"password-reset"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

***

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `actionLabel?`: `string`; `actionUrl?`: `string`; `body`: `string`; `severity?`: `"info"` \| `"success"` \| `"warning"` \| `"error"`; `title`: `string`; \}; `name`: `"notification"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.actionLabel?

&gt; `readonly` `optional` **actionLabel?**: `string`

##### data.actionUrl?

&gt; `readonly` `optional` **actionUrl?**: `string`

##### data.body

&gt; `readonly` **body**: `string` = `S.NonEmptyString`

##### data.severity?

&gt; `readonly` `optional` **severity?**: `"info"` \| `"success"` \| `"warning"` \| `"error"`

##### data.title

&gt; `readonly` **title**: `string` = `S.NonEmptyString`

#### name

&gt; `readonly` **name**: `"notification"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

***

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `dashboardUrl`: `string`; `detectedAt?`: `string`; `incidentId`: `string`; `location?`: `string`; `severity`: `"info"` \| `"warning"` \| `"critical"`; `summary`: `string`; `title`: `string`; \}; `name`: `"incident-alert"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.dashboardUrl

&gt; `readonly` **dashboardUrl**: `string` = `HttpUrl`

##### data.detectedAt?

&gt; `readonly` `optional` **detectedAt?**: `string`

##### data.incidentId

&gt; `readonly` **incidentId**: `string` = `S.NonEmptyString`

##### data.location?

&gt; `readonly` `optional` **location?**: `string`

##### data.severity

&gt; `readonly` **severity**: `"info"` \| `"warning"` \| `"critical"`

##### data.summary

&gt; `readonly` **summary**: `string` = `S.NonEmptyString`

##### data.title

&gt; `readonly` **title**: `string` = `S.NonEmptyString`

#### name

&gt; `readonly` **name**: `"incident-alert"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

***

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `changedAt?`: `string`; `firstName?`: `string`; `secureAccountUrl?`: `string`; \}; `name`: `"password-changed"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.changedAt?

&gt; `readonly` `optional` **changedAt?**: `string`

##### data.firstName?

&gt; `readonly` `optional` **firstName?**: `string`

##### data.secureAccountUrl?

&gt; `readonly` `optional` **secureAccountUrl?**: `string`

#### name

&gt; `readonly` **name**: `"password-changed"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

***

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `at?`: `string`; `device?`: `string`; `firstName?`: `string`; `ipAddress?`: `string`; `location?`: `string`; `secureAccountUrl?`: `string`; \}; `name`: `"new-device-login"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.at?

&gt; `readonly` `optional` **at?**: `string`

##### data.device?

&gt; `readonly` `optional` **device?**: `string`

##### data.firstName?

&gt; `readonly` `optional` **firstName?**: `string`

##### data.ipAddress?

&gt; `readonly` `optional` **ipAddress?**: `string`

##### data.location?

&gt; `readonly` `optional` **location?**: `string`

##### data.secureAccountUrl?

&gt; `readonly` `optional` **secureAccountUrl?**: `string`

#### name

&gt; `readonly` **name**: `"new-device-login"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

***

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `approveUrl`: `string`; `expiresInMinutes?`: `number`; `missionId`: `string`; `requestedBy?`: `string`; `severity?`: `"info"` \| `"warning"` \| `"critical"`; `summary?`: `string`; `title`: `string`; \}; `name`: `"mission-approval"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.approveUrl

&gt; `readonly` **approveUrl**: `string` = `HttpUrl`

##### data.expiresInMinutes?

&gt; `readonly` `optional` **expiresInMinutes?**: `number`

##### data.missionId

&gt; `readonly` **missionId**: `string` = `S.NonEmptyString`

##### data.requestedBy?

&gt; `readonly` `optional` **requestedBy?**: `string`

##### data.severity?

&gt; `readonly` `optional` **severity?**: `"info"` \| `"warning"` \| `"critical"`

##### data.summary?

&gt; `readonly` `optional` **summary?**: `string`

##### data.title

&gt; `readonly` **title**: `string` = `S.NonEmptyString`

#### name

&gt; `readonly` **name**: `"mission-approval"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

***

### Type Literal

\{ `category?`: `"transactional"` \| `"marketing"`; `data`: \{ `acceptUrl`: `string`; `expiresInDays?`: `number`; `inviterName?`: `string`; `orgName`: `string`; `orgRole?`: `string`; \}; `name`: `"org-invitation"`; `to`: `string` & `Brand`\<`"EmailAddress"`\>; `unsubscribeUrl?`: `string`; \}

#### category?

&gt; `readonly` `optional` **category?**: `"transactional"` \| `"marketing"`

Compliance class for this send; defaults to `transactional`.

#### data

&gt; `readonly` **data**: `object`

##### data.acceptUrl

&gt; `readonly` **acceptUrl**: `string` = `HttpUrl`

##### data.expiresInDays?

&gt; `readonly` `optional` **expiresInDays?**: `number`

##### data.inviterName?

&gt; `readonly` `optional` **inviterName?**: `string`

##### data.orgName

&gt; `readonly` **orgName**: `string` = `S.NonEmptyString`

##### data.orgRole?

&gt; `readonly` `optional` **orgRole?**: `string`

#### name

&gt; `readonly` **name**: `"org-invitation"`

#### to

&gt; `readonly` **to**: `string` & `Brand`\<`"EmailAddress"`\>

#### unsubscribeUrl?

&gt; `readonly` `optional` **unsubscribeUrl?**: `string`

Unsubscribe/preferences URL, surfaced in the legal footer for `marketing`.

## Throws

If `input` matches no template variant — bad
  `name`, a malformed/header-injecting `to`, or `data` failing its schema.

## Param

**input**

Untrusted value to validate against the built-in contract.

## Returns

The validated, branded [EmailPayload](./EmailPayload).

## Throws

If `input` matches no built-in template variant —
  unknown `name`, malformed/header-injecting `to`, or `data` failing its schema.
