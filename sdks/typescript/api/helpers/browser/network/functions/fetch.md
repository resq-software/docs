# Function: fetch()

&gt; **fetch**(`input`, `init?`): `Promise`\<`Response`\>

Defined in: [packages/helpers/src/browser/network.ts:39](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/network.ts#L39)

**`Internal`**

Just a wrapper around `window.fetch` that sets the `referrerPolicy` to `strict-origin-when-cross-origin`.

Performs a network request (side effect). `init` is spread after the default
`referrerPolicy`, so a caller-supplied `init.signal` is forwarded and native
cancellation is honoured — but a caller-supplied `referrerPolicy` also
overrides the secure default. Failure surfaces as a rejected promise, exactly
as `window.fetch` rejects.

## Parameters

### input

`RequestInfo` \| `URL`

A Request object or string containing the URL to fetch

### init?

`RequestInit`

Optional request initialization options

## Returns

`Promise`\<`Response`\>

Promise that resolves to the Response object
