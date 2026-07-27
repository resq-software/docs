# Variable: registry

&gt; `const` **registry**: `Record`\<`"otp"` \| `"welcome"` \| `"password-reset"` \| `"notification"` \| `"incident-alert"` \| `"password-changed"` \| `"new-device-login"` \| `"mission-approval"` \| `"org-invitation"`, [`EmailRegistryEntry`](../../mailer/interfaces/EmailRegistryEntry)\> = `resqMailer.registry`

Defined in: [packages/email-templates/src/registry.tsx:30](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/registry.tsx#L30)

Maps each built-in template `name` to its `{ subject, render }`. Derived from
the default mailer, so it always matches the contract.
