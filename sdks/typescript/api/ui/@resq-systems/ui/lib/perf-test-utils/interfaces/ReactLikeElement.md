# Interface: ReactLikeElement

Defined in: [packages/ui/src/lib/perf-test-utils.ts:23](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L23)

Minimal shape of a React element for tree-walking assertions.

## Properties

### props?

&gt; `optional` **props?**: `object`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:25](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L25)

#### Index Signature

\[`key`: `string`\]: `unknown`

#### children?

&gt; `optional` **children?**: `ReactChildren`

#### className?

&gt; `optional` **className?**: `string`

#### style?

&gt; `optional` **style?**: `Record`\<`string`, `unknown`\>

***

### type

&gt; **type**: `string` \| ((...`args`) =&gt; `unknown`) \| \{ `$$typeof?`: `symbol`; \}

Defined in: [packages/ui/src/lib/perf-test-utils.ts:24](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L24)
