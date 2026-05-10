# Variable: RESQ\_SUBDOMAIN\_ALLOWLIST

> `const` **RESQ\_SUBDOMAIN\_ALLOWLIST**: readonly `string`[]

Defined in: [resq.ts:40](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/resq.ts#L40)

Cross-subdomain allow-list for GA4 cross-domain linking.

Pass to `AnalyticsConfig.ga4.domains` so gtag adds `?_gl=` decorators
to outbound links between these hosts and stops counting cross-subdomain
navigation as referral traffic.

Note: the linker only works *within a single GA4 property*. ResQ runs
a property per subdomain by deliberate operator choice, which means the
decorator is a no-op in practice — included anyway so the moment you
consolidate to a single property (or roll up via GA4 360), it just
works.
