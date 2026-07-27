# Function: validatePriorityItem()

&gt; **validatePriorityItem**(`input`): \{ `dueDate`: `string`; `id`: `string`; `priority?`: `number`; \} \| `null`

Defined in: [priority-queue.ts:547](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L547)

Validates and decodes a priority-item input object against its schema.

## Parameters

### input

`unknown`

Untrusted input to validate.

## Returns

\{ `dueDate`: `string`; `id`: `string`; `priority?`: `number`; \} \| `null`

The validated item with schema defaults applied, or `null` if the
  input is invalid.
