# Variable: EmailSchema

&gt; `const` **EmailSchema**: `String`

Defined in: [sanitize.ts:130](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L130)

Schema for email address validation.

Accepts a 2+ character alphabetic TLD or a Punycode/IDN `xn--…` TLD (e.g.
`.xn--p1ai` for `.рф`) so internationalized domains are not rejected. Kept in
sync with `@resq-systems/email-templates`'s `EmailAddress` brand.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)
