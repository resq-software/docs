# Variable: emailOrg

&gt; `const` **emailOrg**: `object`

Defined in: [packages/email-templates/src/emails/tokens.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/tokens.ts#L46)

Organization identity for email chrome (header lockup, signatures, legal
footer), derived from the shared `@resq-systems/constants` brand so names,
addresses, and legal URLs live in one place across apps.

## Type Declaration

### brandName

&gt; `readonly` **brandName**: `any` = `brand.name`

### legalName

&gt; `readonly` **legalName**: `any` = `brand.legalName`

### logoUrl

&gt; `readonly` **logoUrl**: `any` = `brand.logo`

### privacyUrl

&gt; `readonly` **privacyUrl**: `any` = `brand.legal.privacyUrl`

### productName

&gt; `readonly` **productName**: `any` = `brand.productName`

### registeredAddress

&gt; `readonly` **registeredAddress**: `any` = `brand.postalAddress`

### supportEmail

&gt; `readonly` **supportEmail**: `any` = `brand.email.support`

### termsUrl

&gt; `readonly` **termsUrl**: `any` = `brand.legal.termsUrl`

### websiteUrl

&gt; `readonly` **websiteUrl**: `any` = `brand.domains.marketing`
