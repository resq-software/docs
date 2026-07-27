# Interface: PriorityRequestItem

Defined in: [priority-queue.ts:460](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L460)

A schedulable request with a deadline and priority level, used by the
queue factory helpers below.

## Properties

### deadline

&gt; **deadline**: `Date`

Defined in: [priority-queue.ts:464](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L464)

Response deadline

***

### id

&gt; **id**: `string`

Defined in: [priority-queue.ts:462](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L462)

Request ID

***

### metadata?

&gt; `optional` **metadata?**: `Record`\<`string`, `unknown`\>

Defined in: [priority-queue.ts:470](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L470)

Additional metadata

***

### priority

&gt; **priority**: `number`

Defined in: [priority-queue.ts:466](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L466)

Priority level (1 = highest)

***

### status

&gt; **status**: `string`

Defined in: [priority-queue.ts:468](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L468)

Request status
