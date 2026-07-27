# Interface: EvaluateOptions

Defined in: [packages/math/src/evaluate.ts:56](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/evaluate.ts#L56)

Options to configure execution boundaries and limits.

## Properties

### maxDepth?

&gt; `readonly` `optional` **maxDepth?**: `number`

Defined in: [packages/math/src/evaluate.ts:58](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/evaluate.ts#L58)

Maximum recursion depth before a [RecursionLimitError](../../error/classes/RecursionLimitError) is thrown. Defaults to 200.

***

### maxSteps?

&gt; `readonly` `optional` **maxSteps?**: `number`

Defined in: [packages/math/src/evaluate.ts:60](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/evaluate.ts#L60)

Maximum evaluation steps before an [ExecutionLimitError](../../error/classes/ExecutionLimitError) is thrown. Defaults to 10000.
