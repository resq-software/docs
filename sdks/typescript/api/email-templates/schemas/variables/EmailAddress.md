# Variable: EmailAddress

&gt; `const` **EmailAddress**: `brand`\<`String`, `"EmailAddress"`\>

Defined in: [packages/email-templates/src/schemas.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/schemas.ts#L52)

A single, syntactically-valid recipient email address (branded).

The pattern mirrors `@resq-systems/security`'s `EmailSchema` — one `@`, a
dotted domain, and a 2+ character TLD, or a Punycode/IDN `xn--…` TLD (e.g.
`.xn--p1ai` for `.рф`) so internationalized domains are not rejected. Because
the character classes admit no whitespace or control characters and the check
is anchored (`^…$`), it also rejects the CR/LF that underpins SMTP header
injection: a `to` smuggling `"…\r\nBcc: attacker@evil"` into a provider that
concatenates headers is a type-*and*-runtime error at the boundary, not a
silent extra recipient.

The EmailAddress brand marks a string that has cleared this check, so
a validated address is not interchangeable with a raw `string` downstream
(the `to` field on the decoded mailer payload and the rendered email).
