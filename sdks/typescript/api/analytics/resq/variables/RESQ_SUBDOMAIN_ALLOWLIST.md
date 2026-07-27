# Variable: RESQ\_SUBDOMAIN\_ALLOWLIST

&gt; `const` **RESQ\_SUBDOMAIN\_ALLOWLIST**: readonly \[`"resq.software"`, `"research.resq.software"`, `"viz.resq.software"`\]

Defined in: [resq.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/resq.ts#L46)

Cross-subdomain allow-list for GA4 cross-domain linking.

Pass to `AnalyticsConfig.ga4.domains` so gtag adds `?_gl=` decorators
to outbound links between these hosts and stops counting cross-subdomain
navigation as referral traffic.

Note: the linker only works *within a single GA4 property*. ResQ runs
a property per subdomain by deliberate operator choice, which means the
decorator is a no-op in practice — included anyway so the moment you
consolidate to a single property (or roll up via GA4 360), it just
works.
