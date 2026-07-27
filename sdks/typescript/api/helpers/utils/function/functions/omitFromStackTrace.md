# Function: omitFromStackTrace()

&gt; **omitFromStackTrace**\<`Args`, `Return`\>(`fn`): (...`args`) =&gt; `Return`

Defined in: [packages/helpers/src/utils/function.ts:53](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/function.ts#L53)

**`Internal`**

When a function is wrapped in `omitFromStackTrace`, if it throws an error the stack trace won't
include the function itself or any stack frames above it. Useful for assertion-style function
where the error will ideally originate from the call-site rather than within the implementation
of the assert fn.

Only works in platforms that support `Error.captureStackTrace` (ie v8).

The wrapper re-throws the *same* error instance (identity preserved, so
`instanceof` checks still hold); it only rewrites the error's `stack` when the
thrown value is an `Error` and `Error.captureStackTrace` exists — non-`Error`
throws and non-V8 runtimes pass through untouched. The wrapped function is
otherwise transparent: same arguments, same return value.

## Type Parameters

### Args

`Args` *extends* `unknown`[]

The wrapped function's positional argument tuple.

### Return

`Return`

The wrapped function's return type, forwarded unchanged.

## Parameters

### fn

(...`args`) =&gt; `Return`

The function to wrap and exclude from stack traces

## Returns

A wrapped version of the function that omits itself from error stack traces

(...`args`) =&gt; `Return`

## Example

```ts
const assertPositive = omitFromStackTrace((value: number) => {
  if (value <= 0) throw new Error('Value must be positive')
  return value
})

assertPositive(-1) // Error stack trace will point to this line, not inside assertPositive
```
