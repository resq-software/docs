# Variable: GA4\_ID\_PATTERN

> `const` **GA4\_ID\_PATTERN**: `RegExp`

Defined in: [resq.ts:57](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/resq.ts#L57)

Strict GA4 Measurement ID shape per Google's documented format:
`G-` followed by 6–32 uppercase ASCII letters / digits.

Used as a sanitiser before interpolating an env-var-sourced ID into an
inline `<script>` body. Even though `NEXT_PUBLIC_*` values are
build-time controlled, validating with a regex makes the taint flow
provably safe — closes static-analysis warnings (CodeQL
`js/bad-code-sanitization`) for free and prevents accidental
`</script>` / line-terminator escapes.
