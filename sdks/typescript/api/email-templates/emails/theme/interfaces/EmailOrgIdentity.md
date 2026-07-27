# Interface: EmailOrgIdentity

Defined in: [packages/email-templates/src/emails/theme.tsx:54](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L54)

Organization identity rendered into email chrome (header, signature, footer).

All `*Url` fields are absolute URLs. [EmailOrgIdentity.registeredAddress](#registeredaddress)
leads with the legal entity name, so it stands alone as a complete CAN-SPAM
postal line without a separate `legalName` line in the footer.

## Properties

### brandName

&gt; **brandName**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L56)

Short brand name used in sign-offs, e.g. "— The &#123;brandName&#125; team".

***

### legalName

&gt; **legalName**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L60)

Full legal entity name.

***

### logoUrl

&gt; **logoUrl**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L72)

Absolute URL of the header logo image.

***

### privacyUrl

&gt; **privacyUrl**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L70)

Absolute URL of the Privacy page.

***

### productName

&gt; **productName**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L58)

Product name shown in the header lockup beside the logo.

***

### registeredAddress

&gt; **registeredAddress**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L62)

Registered postal address, prefixed with the legal name; a complete CAN-SPAM line.

***

### supportEmail

&gt; **supportEmail**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L64)

Support inbox address, rendered as a `mailto:` link.

***

### termsUrl

&gt; **termsUrl**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L68)

Absolute URL of the Terms page.

***

### websiteUrl

&gt; **websiteUrl**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L66)

Marketing/website URL (absolute). Never used as an unsubscribe target.
