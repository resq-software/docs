# Function: validatePriorityItem()

&gt; **validatePriorityItem**(`input`): \{ `dueDate`: `string`; `id`: `string`; `priority?`: `number`; \} \| `null`

Defined in: [priority-queue.ts:547](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L547)

Validates and decodes a priority-item input object against its schema.

## Parameters

### input

`unknown`

Untrusted input to validate.

## Returns

\{ `dueDate`: `string`; `id`: `string`; `priority?`: `number`; \} \| `null`

The validated item with schema defaults applied, or `null` if the
  input is invalid.
