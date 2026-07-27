# Interface: ObfuscatedLink

Defined in: [packages/helpers/src/browser/html-entities.ts:65](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/html-entities.ts#L65)

Result of [obfuscateLink](../functions/obfuscateLink): a RAW (un-encoded) `href` suitable for
an anchor's `href` attribute, paired with entity-encoded visible text.

Note: `href` is intentionally NOT entity-encoded — browsers require a
literal `mailto:`/`tel:` URI in the attribute. Only `encodedText` is
obfuscated to deter naive scrapers of the rendered DOM.

## Properties

### encodedText

&gt; **encodedText**: `Brand`

Defined in: [packages/helpers/src/browser/html-entities.ts:69](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/html-entities.ts#L69)

Entity-encoded visible link text (see [HtmlEntityEncoded](../type-aliases/HtmlEntityEncoded)).

***

### href

&gt; **href**: `string`

Defined in: [packages/helpers/src/browser/html-entities.ts:67](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/html-entities.ts#L67)

RAW, un-encoded URI for the anchor `href` attribute.
