# Type Alias: ColorTokens

&gt; **ColorTokens** = `Record`\<`string`, `string`\>

Defined in: [packages/ui/src/lib/contrast-audit.ts:34](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L34)

Token map for a single theme: token name → CSS color string.
Token names are the bare custom-property identifier without the
`--` prefix (e.g. `"foreground"`, not `"--foreground"`).
