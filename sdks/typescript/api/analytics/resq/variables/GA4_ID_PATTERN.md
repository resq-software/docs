# Variable: GA4\_ID\_PATTERN

&gt; `const` **GA4\_ID\_PATTERN**: `RegExp`

Defined in: [resq.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/resq.ts#L83)

Strict GA4 Measurement ID shape per Google's documented format:
`G-` followed by 6–32 uppercase ASCII letters / digits.

Used as a sanitizer before interpolating an env-var-sourced ID into an
inline `<script>` body. Even though `NEXT_PUBLIC_*` values are
build-time controlled, validating with a regex makes the taint flow
provably safe — closes static-analysis warnings (CodeQL
`js/bad-code-sanitization`) for free and prevents accidental
`</script>` / line-terminator escapes.
