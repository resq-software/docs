# Function: toCookieDomain()

&gt; **toCookieDomain**(`host`): `any`

Defined in: [resq.ts:177](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/resq.ts#L177)

Smart constructor for [CookieDomain](../type-aliases/CookieDomain). Normalizes, then validates:

1. trims surrounding whitespace,
2. lowercases (hostnames are case-insensitive per RFC 3986 §3.2.2),
3. strips a trailing dot (FQDN root form),
4. prepends the leading dot when missing.

Pure and total: never throws. A single-label host (`"localhost"`), an empty
or whitespace-only string, or a non-string short-circuits to the `null`
sentinel rather than an error.

## Parameters

### host

`string` \| `null` \| `undefined`

A host or cookie domain, with or without a leading dot
  (`"resq.software"`, `".resq.software"`, `"App.Example.com."`). `null` /
  `undefined` short-circuit to `null`.

## Returns

`any`

The branded, normalized [CookieDomain](../type-aliases/CookieDomain), or the `null` sentinel
  when the input is not a valid multi-label host.

## Example

```ts
toCookieDomain("App.Example.com."); // → branded ".app.example.com"
toCookieDomain(".resq.software"); // → branded ".resq.software"
toCookieDomain("localhost"); // → null (single label)
```
