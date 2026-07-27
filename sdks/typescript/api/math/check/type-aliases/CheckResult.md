# Type Alias: CheckResult

&gt; **CheckResult** = \{ `ok`: `true`; `sort`: [`Sort`](../../value/type-aliases/Sort); \} \| \{ `errors`: readonly [`SortError`](../../error/classes/SortError)[]; `ok`: `false`; \}

Defined in: [packages/math/src/check.ts:55](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/check.ts#L55)

The outcome of sort-checking, discriminated on CheckResult.ok ok.

- `ok: true` carries the single inferred [Sort](../../value/type-aliases/Sort) of the whole expression.
- `ok: false` carries every [SortError](../../error/classes/SortError) found — the walk aggregates
  diagnostics instead of stopping at the first, so `errors` is non-empty and
  may list several independent mismatches.

Failure is signalled through this value, not by throwing (the sole exception
is `RecursionLimitError` for pathologically deep trees).
