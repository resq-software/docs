# Interface: EmailMessage

Defined in: [packages/email-templates/src/emails/theme.tsx:208](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L208)

Per-send message policy carried through context to the legal footer.

The unsubscribe affordance renders only when [EmailMessage.category](#category) is
`"marketing"` **and** [EmailMessage.unsubscribeUrl](#unsubscribeurl) is set; a marketing
send with no `unsubscribeUrl` simply omits it (there is no homepage fallback).

## Properties

### category

&gt; **category**: `"transactional"` \| `"marketing"`

Defined in: [packages/email-templates/src/emails/theme.tsx:210](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L210)

Compliance class; defaults to `transactional`.

***

### unsubscribeUrl?

&gt; `optional` **unsubscribeUrl?**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:212](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L212)

Absolute unsubscribe/preferences URL; only consulted for `marketing` sends.
