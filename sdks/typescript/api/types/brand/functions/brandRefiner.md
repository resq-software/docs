# Function: brandRefiner()

&gt; **brandRefiner**\<`T`, `B`\>(`predicate`, `label?`): [`BrandRefiner`](../interfaces/BrandRefiner)\<`T`, `B`\>

Defined in: [brand.ts:181](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/brand.ts#L181)

Build a [BrandRefiner](../interfaces/BrandRefiner) — a `{ is, from, coerce, unsafe }` bundle — from
a single predicate. This is the ergonomic way to mint a validated nominal
type: define the type, define the check once, and get a guard, an asserting
constructor, and a total constructor for free.

## Type Parameters

### T

`T`

The carrier type (e.g. `string`, `number`).

### B

`B` *extends* `PropertyKey`

The brand name (e.g. `"Email"`).

## Parameters

### predicate

(`value`) =&gt; `boolean`

Returns `true` when `value` is a valid `B`.

### label?

`string`

Optional human name used in the [BrandRefiner.from](../interfaces/BrandRefiner#from) error
  message. Defaults to generic text so it never leaks the (possibly
  sensitive) offending value.

## Returns

[`BrandRefiner`](../interfaces/BrandRefiner)\<`T`, `B`\>

A refiner bundle for `Brand<T, B>`.

## Example

```ts
export type Email = Brand<string, "Email">;
const Email = brandRefiner<string, "Email">(
  (s) => /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(s),
  "email",
);
export const isEmail = Email.is;   // (s: string) => s is Email
export const toEmail = Email.from; // (s: string) => Email  (throws if invalid)

if (isEmail(input)) sendMail(input); // input: Email inside the block
```
