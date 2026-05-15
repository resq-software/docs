# Interface: PathResult\<T\>

Defined in: [graph.ts:57](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/graph.ts#L57)

Path result from shortest path algorithms

## Type Parameters

### T

`T`

## Properties

### distance

> **distance**: `number`

Defined in: [graph.ts:61](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/graph.ts#L61)

Total distance/weight of the path

***

### found

> **found**: `boolean`

Defined in: [graph.ts:63](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/graph.ts#L63)

Whether a path was found

***

### path

> **path**: `T`[]

Defined in: [graph.ts:59](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/graph.ts#L59)

Ordered list of vertices in the path
