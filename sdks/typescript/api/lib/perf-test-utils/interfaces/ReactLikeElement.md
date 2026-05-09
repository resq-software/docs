# Interface: ReactLikeElement

Defined in: [packages/ui/src/lib/perf-test-utils.ts:23](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L23)

Minimal shape of a React element for tree-walking assertions.

## Properties

### props?

> `optional` **props?**: `object`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:25](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L25)

#### Index Signature

\[`key`: `string`\]: `unknown`

#### children?

> `optional` **children?**: `ReactChildren`

#### className?

> `optional` **className?**: `string`

#### style?

> `optional` **style?**: `Record`\<`string`, `unknown`\>

***

### type

> **type**: `string` \| \&#123; `$$typeof?`: `symbol`; \&#125; \| ((...`args`) => `unknown`)

Defined in: [packages/ui/src/lib/perf-test-utils.ts:24](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L24)
