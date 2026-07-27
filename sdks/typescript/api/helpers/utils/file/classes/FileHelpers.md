# Class: FileHelpers

Defined in: [packages/helpers/src/utils/file.ts:49](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/file.ts#L49)

Utility class providing helper methods for file and blob operations.

FileHelpers contains static methods for common file operations including
URL fetching, format conversion, and MIME type manipulation. All methods work with
web APIs like fetch, FileReader, and Blob/File objects.

## Example

```ts
// Fetch and convert a remote image to data URL
const dataUrl = await FileHelpers.urlToDataUrl('https://example.com/image.png')

// Convert user-selected file to text
const text = await FileHelpers.blobToText(userFile)

// Change file MIME type
const newFile = FileHelpers.rewriteMimeType(originalFile, 'application/json')
```

## Constructors

### Constructor

&gt; **new FileHelpers**(): `FileHelpers`

#### Returns

`FileHelpers`

## Methods

### blobToDataUrl()

&gt; `static` **blobToDataUrl**(`file`): `Promise`\<`string`\>

Defined in: [packages/helpers/src/utils/file.ts:151](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/file.ts#L151)

Convert a Blob to a base64 encoded data URL.

Converts a Blob object to a base64-encoded data URL using the FileReader API.
This is useful for displaying images or embedding file content directly in HTML.

#### Parameters

##### file

`Blob`

The Blob object to convert

#### Returns

`Promise`\<`string`\>

Promise that resolves to a base64-encoded data URL string

#### Throws

Rejects with the `FileReader` error event if the read
  errors or is aborted.

#### Remarks

If `file` is falsy the read is never started, so the returned promise
  **never settles** (it hangs rather than rejecting) — always pass a real Blob.

#### Example

```ts
const blob = new Blob(['Hello World'], { type: 'text/plain' })
const dataUrl = await FileHelpers.blobToDataUrl(blob)
// Returns: 'data:text/plain;base64,SGVsbG8gV29ybGQ='

// With an image file
const imageDataUrl = await FileHelpers.blobToDataUrl(myImageFile)
// Can be used directly in img src attribute
```

***

### blobToText()

&gt; `static` **blobToText**(`file`): `Promise`\<`string`\>

Defined in: [packages/helpers/src/utils/file.ts:187](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/file.ts#L187)

Convert a Blob to a unicode text string.

Reads the content of a Blob object as a UTF-8 text string using the FileReader API.
This is useful for reading text files or extracting text content from blobs.

#### Parameters

##### file

`Blob`

The Blob object to convert to text

#### Returns

`Promise`\<`string`\>

Promise that resolves to the text content as a string

#### Throws

Rejects with the `FileReader` error event if the read
  errors or is aborted.

#### Remarks

If `file` is falsy the read is never started, so the returned promise
  **never settles** (it hangs rather than rejecting) — always pass a real Blob.

#### Example

```ts
const textBlob = new Blob(['Hello World'], { type: 'text/plain' })
const text = await FileHelpers.blobToText(textBlob)
console.log(text) // 'Hello World'

// With a text file from user input
const content = await FileHelpers.blobToText(myTextFile)
console.log(content) // File content as string
```

***

### rewriteMimeType()

#### Call Signature

&gt; `static` **rewriteMimeType**(`blob`, `newMimeType`): `Blob`

Defined in: [packages/helpers/src/utils/file.ts:223](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/file.ts#L223)

Creates a new Blob or File with a different MIME type.

Creates a copy of the given Blob or File with a new MIME type while preserving
all other properties. If the current MIME type already matches the new one, returns the
original object unchanged. For File objects, preserves the filename.

##### Parameters

###### blob

`Blob`

The Blob or File object to modify

###### newMimeType

`string`

The new MIME type to assign

##### Returns

`Blob`

A new Blob or File with the updated MIME type

##### Example

```ts
// Change a generic blob to a specific image type
const blob = new Blob([imageData])
const imageBlob = FileHelpers.rewriteMimeType(blob, 'image/png')

// Change a file's MIME type while preserving filename
const file = new File([data], 'document.txt', { type: 'text/plain' })
const jsonFile = FileHelpers.rewriteMimeType(file, 'application/json')
console.log(jsonFile.name) // 'document.txt' (preserved)
console.log(jsonFile.type) // 'application/json' (updated)
```

#### Call Signature

&gt; `static` **rewriteMimeType**(`blob`, `newMimeType`): `File`

Defined in: [packages/helpers/src/utils/file.ts:224](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/file.ts#L224)

Creates a new Blob or File with a different MIME type.

Creates a copy of the given Blob or File with a new MIME type while preserving
all other properties. If the current MIME type already matches the new one, returns the
original object unchanged. For File objects, preserves the filename.

##### Parameters

###### blob

`File`

The Blob or File object to modify

###### newMimeType

`string`

The new MIME type to assign

##### Returns

`File`

A new Blob or File with the updated MIME type

##### Example

```ts
// Change a generic blob to a specific image type
const blob = new Blob([imageData])
const imageBlob = FileHelpers.rewriteMimeType(blob, 'image/png')

// Change a file's MIME type while preserving filename
const file = new File([data], 'document.txt', { type: 'text/plain' })
const jsonFile = FileHelpers.rewriteMimeType(file, 'application/json')
console.log(jsonFile.name) // 'document.txt' (preserved)
console.log(jsonFile.type) // 'application/json' (updated)
```

***

### urlToArrayBuffer()

&gt; `static` **urlToArrayBuffer**(`url`): `Promise`\<`ArrayBuffer`\>

Defined in: [packages/helpers/src/utils/file.ts:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/file.ts#L70)

Converts a URL to an ArrayBuffer by fetching the resource.

Fetches the resource at the given URL and returns its content as an ArrayBuffer.
This is useful for loading binary data like images, videos, or other file types.

Performs a network request as a side effect.

#### Parameters

##### url

`string`

The URL of the file to fetch

#### Returns

`Promise`\<`ArrayBuffer`\>

Promise that resolves to the file content as an ArrayBuffer

#### Throws

If the `fetch` fails (network error, CORS, invalid URL);
  rejects the returned promise. HTTP error statuses are *not* thrown — the
  body of a 4xx/5xx response is returned like any other.

#### Example

```ts
const buffer = await FileHelpers.urlToArrayBuffer('https://example.com/image.png')
console.log(buffer.byteLength) // Size of the file in bytes
```

***

### urlToBlob()

&gt; `static` **urlToBlob**(`url`): `Promise`\<`Blob`\>

Defined in: [packages/helpers/src/utils/file.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/file.ts#L95)

Converts a URL to a Blob by fetching the resource.

Fetches the resource at the given URL and returns its content as a Blob object.
Blobs are useful for handling file data in web applications.

Performs a network request as a side effect.

#### Parameters

##### url

`string`

The URL of the file to fetch

#### Returns

`Promise`\<`Blob`\>

Promise that resolves to the file content as a Blob

#### Throws

If the `fetch` fails (network error, CORS, invalid URL);
  rejects the returned promise. HTTP error statuses are not thrown.

#### Example

```ts
const blob = await FileHelpers.urlToBlob('https://example.com/document.pdf')
console.log(blob.type) // 'application/pdf'
console.log(blob.size) // Size in bytes
```

***

### urlToDataUrl()

&gt; `static` **urlToDataUrl**(`url`): `Promise`\<`string`\>

Defined in: [packages/helpers/src/utils/file.ts:121](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/file.ts#L121)

Converts a URL to a data URL by fetching the resource.

Fetches the resource at the given URL and converts it to a base64-encoded data URL.
If the URL is already a data URL, it returns the URL unchanged. This is useful for embedding
resources directly in HTML or CSS.

#### Parameters

##### url

`string`

The URL of the file to convert, or an existing data URL

#### Returns

`Promise`\<`string`\>

Promise that resolves to a data URL string. An input already
  starting with `data:` is returned verbatim without a fetch.

#### Throws

If a non-`data:` URL is fetched and the request fails.

#### Example

```ts
const dataUrl = await FileHelpers.urlToDataUrl('https://example.com/image.jpg')
// Returns: 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEA...'

const existing = await FileHelpers.urlToDataUrl('data:text/plain;base64,SGVsbG8=')
// Returns the same data URL unchanged
```
