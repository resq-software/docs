# Interface: ReactLikeElement

Defined in: [packages/ui/src/lib/perf-test-utils.ts:23](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L23)

Minimal shape of a React element for tree-walking assertions.

## Properties

### props?

> `optional` **props?**: `object`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:25](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L25)

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

Defined in: [packages/ui/src/lib/perf-test-utils.ts:24](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L24)
