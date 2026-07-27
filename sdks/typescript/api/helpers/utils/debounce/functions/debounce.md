# Function: debounce()

&gt; **debounce**\<`T`, `U`\>(`callback`, `wait`): \{(...`args`): `Promise`\<`U`\>; `cancel`: `void`; \}

Defined in: [packages/helpers/src/utils/debounce.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/debounce.ts#L83)

## Type Parameters

### T

`T` *extends* `unknown`[]

### U

`U`

## Parameters

### callback

(...`args`) =&gt; `Awaitable`\<`U`\>

### wait

`number`

## Returns

\{(...`args`): `Promise`\<`U`\>; `cancel`: `void`; \}

### cancel()

&gt; **cancel**(): `void`

#### Returns

`void`
