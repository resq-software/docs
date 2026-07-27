# Type Alias: ThreatType

&gt; **ThreatType** = `"xss"` \| `"sql_injection"` \| `"nosql_injection"` \| `"command_injection"` \| `"path_traversal"` \| `"homoglyph"`

Defined in: [validators.ts:201](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L201)

The closed set of threat categories the validators recognize. Serves as the
discriminant of [ThreatFinding](../interfaces/ThreatFinding) (its `type` field) and drives the
exhaustive `switch` in [getThreatErrorMessage](../functions/getThreatErrorMessage) — adding a variant here
without a matching `case` there becomes a compile error via `assertNever`.
Add new categories here when adding a new detector.
