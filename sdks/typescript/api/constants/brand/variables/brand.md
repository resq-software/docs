# Variable: brand

&gt; `const` **brand**: `object`

Defined in: [brand.ts:33](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/constants/src/brand.ts#L33)

ResQ Systems brand identity — names, domains, contact addresses, and legal
details shared across apps (marketing site, dashboard, transactional email).

The postal address is ResQ Systems, Inc.'s public Delaware registered-agent
address (already public on the DE filing), included so commercial email stays
CAN-SPAM compliant by default.

## Type Declaration

### company

&gt; `readonly` **company**: `object`

#### company.locations

&gt; `readonly` **locations**: readonly \[`"Long Island, New York"`\]

#### company.stage

&gt; `readonly` **stage**: `"Pre-Seed"` = `"Pre-Seed"`

### description

&gt; `readonly` **description**: `"The decentralized kinetic operating system for autonomous disaster response. Mesh-networked coordination when infrastructure fails."` = `"The decentralized kinetic operating system for autonomous disaster response. Mesh-networked coordination when infrastructure fails."`

Long-form product description (metadata, manifest, store listings).

### domains

&gt; `readonly` **domains**: `object`

Absolute `https://` origins with no trailing slash, so a caller can append
a path directly (`` `${brand.domains.marketing}/pricing` ``). `marketing`
is the apex domain; the others are subdomains of it.

#### domains.app

&gt; `readonly` **app**: `"https://app.resq.software"` = `"https://app.resq.software"`

#### domains.docs

&gt; `readonly` **docs**: `"https://docs.resq.software"` = `"https://docs.resq.software"`

#### domains.marketing

&gt; `readonly` **marketing**: `"https://resq.software"` = `"https://resq.software"`

#### domains.status

&gt; `readonly` **status**: `"https://status.resq.software"` = `"https://status.resq.software"`

### email

&gt; `readonly` **email**: `object`

#### email.contact

&gt; `readonly` **contact**: `"contact@resq.software"` = `"contact@resq.software"`

General contact / inbound inquiries.

#### email.engineer

&gt; `readonly` **engineer**: `"engineer@resq.software"` = `"engineer@resq.software"`

Engineering / automation address — matches the CI commit author.

#### email.from

&gt; `readonly` **from**: `"ResQ Systems <updates@send.resq.software>"` = `"ResQ Systems <updates@send.resq.software>"`

RFC 5322 display-name form (`Name <addr>`) for use as a message `From`
header verbatim. Sends from the `send.resq.software` subdomain — the
DKIM/SPF-authenticated envelope domain — which differs from the apex
reply mailboxes such as [brand.email.contact](#email) and [brand.email.security](#email).

#### email.research

&gt; `readonly` **research**: `"research@resq.software"` = `"research@resq.software"`

Research, press, and partnership inquiries.

#### email.security

&gt; `readonly` **security**: `"security@resq.software"` = `"security@resq.software"`

Security & vulnerability reports; the address to publish in `security.txt`.

#### email.support

&gt; `readonly` **support**: `"contact@resq.software"` = `"contact@resq.software"`

General support address. Currently an alias of [brand.email.contact](#email) — there
is no dedicated `support@` mailbox — so replies land in the same inbox.

### legal

&gt; `readonly` **legal**: `object`

#### legal.privacyUrl

&gt; `readonly` **privacyUrl**: `"https://resq.software/legal/privacy"` = `"https://resq.software/legal/privacy"`

#### legal.termsUrl

&gt; `readonly` **termsUrl**: `"https://resq.software/legal/terms"` = `"https://resq.software/legal/terms"`

### legalName

&gt; `readonly` **legalName**: `"ResQ Systems, Inc."` = `"ResQ Systems, Inc."`

Registered legal entity.

### logo

&gt; `readonly` **logo**: `"https://resq.software/logo.png"` = `"https://resq.software/logo.png"`

### name

&gt; `readonly` **name**: `"ResQ Systems"` = `"ResQ Systems"`

Short brand name.

### postalAddress

&gt; `readonly` **postalAddress**: `"ResQ Systems, Inc., 131 Continental Dr, Suite 305, Newark, DE 19713, USA"` = `"ResQ Systems, Inc., 131 Continental Dr, Suite 305, Newark, DE 19713, USA"`

### productName

&gt; `readonly` **productName**: `"ResQ Tactical OS"` = `"ResQ Tactical OS"`

Product name (marketing / app title).

### socials

&gt; `readonly` **socials**: `object`

#### socials.github

&gt; `readonly` **github**: `"https://github.com/resq-software"` = `"https://github.com/resq-software"`

#### socials.linkedin

&gt; `readonly` **linkedin**: `"https://www.linkedin.com/company/resq-systems-inc"` = `"https://www.linkedin.com/company/resq-systems-inc"`

#### socials.x

&gt; `readonly` **x**: `"https://x.com/resqsystems_inc"` = `"https://x.com/resqsystems_inc"`

#### socials.xHandle

&gt; `readonly` **xHandle**: `"@resqsystems_inc"` = `"@resqsystems_inc"`

The `@handle` form for `twitter:creator`/`site` meta (matches the `x` profile).

### tagline

&gt; `readonly` **tagline**: `"autonomous drone disaster response"` = `"autonomous drone disaster response"`

One-line positioning tagline.
