# Function: obfuscateLink()

&gt; **obfuscateLink**(`opts`): [`ObfuscatedLink`](../interfaces/ObfuscatedLink)

Defined in: [packages/helpers/src/browser/html-entities.ts:97](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/html-entities.ts#L97)

Obfuscates and encodes a contact hyperlink (such as mailto or tel).

The returned `href` is a RAW URI (browsers need a literal `mailto:` /
`tel:` value in the attribute); only the visible `encodedText` is
entity-encoded to deter naive DOM scrapers.

## Parameters

### opts

Configuration options for link obfuscation.

#### address

`string`

The contact address (email or phone number).

#### params?

`Record`\<`string`, `string`\>

Optional query parameters (used for `mailto` links).

#### scheme

`"mailto"` \| `"tel"`

The URI scheme (`"mailto"` or `"tel"`).

#### text?

`string`

Optional visible link text; defaults to the address.

## Returns

[`ObfuscatedLink`](../interfaces/ObfuscatedLink)

An object containing the RAW `href` and entity-encoded `encodedText`.

## Throws

If required fields are missing or invalid.

## See

 - https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#security_and_privacy
 - https://github.com/resq-software/resQ

## Example

```ts
const { href, encodedText } = obfuscateLink({
  scheme: 'mailto',
  address: 'jane.doe@example.com',
  text: 'Contact Jane'
});
```
