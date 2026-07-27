# Type Alias: HtmlEntityEncoded

&gt; **HtmlEntityEncoded** = `Brand`\<`string`, `"HtmlEntityEncoded"`\>

Defined in: [packages/helpers/src/browser/html-entities.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/html-entities.ts#L38)

A string whose every character has been replaced by its decimal HTML
character reference (e.g. `"a"` → `"&#97;"`); safe to embed as text content
in HTML.

The brand guarantees the string was produced by full entity-encoding (every
code point escaped), not merely typed as encoded. Mint one through the
exported [obfuscateLink](../functions/obfuscateLink) — its `encodedText` field carries this brand;
the encoder itself is internal, so callers cannot brand an arbitrary string
without going through it.
