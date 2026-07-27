# Function: byLevel()

&gt; **byLevel**(...`levels`): (`entry`) =&gt; `boolean`

Defined in: [transports.ts:165](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/transports.ts#L165)

Predicate factory for [createFilterTransport](./createFilterTransport): matches entries whose
`level` is one of `levels`.

## Parameters

### levels

...[`LogLevelString`](../../logger.types/type-aliases/LogLevelString)[]

The levels to admit.

## Returns

A predicate that is `true` only for entries at one of `levels`.

(`entry`) =&gt; `boolean`
