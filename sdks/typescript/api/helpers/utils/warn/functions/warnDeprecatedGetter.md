# Function: warnDeprecatedGetter()

&gt; **warnDeprecatedGetter**(`name`): `void`

Defined in: [packages/helpers/src/utils/warn.ts:54](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/warn.ts#L54)

**`Internal`**

Issues a deprecation warning for deprecated getter properties, advising users to use
the equivalent getter method instead. The warning is shown only once per property name.

Delegates to [warnOnce](./warnOnce), so it inherits the same logger side effect and
process-lifetime dedup: the composed message (which suggests `get<Name>`) is
logged at most once.

## Parameters

### name

`string`

The name of the deprecated property (e.g., 'viewport')

## Returns

`void`

## Example

```ts
// Inside a class with deprecated property access
get viewport() {
  warnDeprecatedGetter('viewport')
  return this.getViewport()
}

// Usage will show: "[helpers] Using 'viewport' is deprecated and will be removed..."
// But only the first time it's accessed
```
