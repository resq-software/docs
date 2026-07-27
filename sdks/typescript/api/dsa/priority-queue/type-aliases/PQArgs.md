# Type Alias: PQArgs\<T\>

&gt; **PQArgs**\<`T`\> = \[`T`\] *extends* \[`Comparable`\] ? \[[`PQOptions`](./PQOptions)\<`T`\>\] : \[[`PQOptions`](./PQOptions)\<`T`\>\]

Defined in: [priority-queue.ts:74](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L74)

Constructor/factory argument tuple derived from [PQOptions](./PQOptions). The tuple
makes the options argument optional for Comparable elements but
required for non-comparable ones, so `new PriorityQueue<Task>()` (object
element, no comparator) is a compile error while `new PriorityQueue<number>()`
keeps working.

## Type Parameters

### T

`T`
