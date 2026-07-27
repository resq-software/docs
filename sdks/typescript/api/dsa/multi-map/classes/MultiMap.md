# Class: MultiMap\<K, V\>

Defined in: [multi-map.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L52)

A map that associates each key with an **ordered list of values** rather than
a single value. Setting the same key repeatedly appends instead of
overwriting, and iteration yields `[key, values]` entries.

Zero-dependency; backed by a native `Map<K, V[]>`, so key equality follows
`SameValueZero` semantics.

## Example

```ts
const byZone = new MultiMap<string, string>();
byZone.set("north", "drone-1");
byZone.set("north", "drone-2");
byZone.get("north"); // → ["drone-1", "drone-2"]
byZone.hasValue("north", "drone-2"); // → true
```

## Type Parameters

### K

`K`

The key type.

### V

`V`

The value type.

## Constructors

### Constructor

&gt; **new MultiMap**\<`K`, `V`\>(): `MultiMap`\<`K`, `V`\>

#### Returns

`MultiMap`\<`K`, `V`\>

## Accessors

### size

#### Get Signature

&gt; **get** **size**(): `number`

Defined in: [multi-map.ts:104](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L104)

The number of distinct keys.

##### Returns

`number`

## Methods

### \[iterator\]()

&gt; **\[iterator\]**(): `IterableIterator`\<\[`K`, `V`[]\]\>

Defined in: [multi-map.ts:109](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L109)

Iterate `[key, values]` entries, one per distinct key.

#### Returns

`IterableIterator`\<\[`K`, `V`[]\]\>

***

### clear()

&gt; **clear**(): `void`

Defined in: [multi-map.ts:128](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L128)

Remove all keys and values.

#### Returns

`void`

***

### delete()

&gt; **delete**(`key`, `value`): `void`

Defined in: [multi-map.ts:80](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L80)

Remove every occurrence of `value` from `key`'s list, keeping the remaining
values. The key itself is dropped once its list becomes empty, so
[has](#has) reports `false` afterwards (no lingering empty lists).

#### Parameters

##### key

`K`

##### value

`V`

#### Returns

`void`

***

### deleteAll()

&gt; **deleteAll**(`key`): `void`

Defined in: [multi-map.ts:94](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L94)

Remove `key` and every value stored under it.

#### Parameters

##### key

`K`

#### Returns

`void`

***

### get()

&gt; **get**(`key`): `V`[]

Defined in: [multi-map.ts:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L66)

#### Parameters

##### key

`K`

#### Returns

`V`[]

The values stored under `key`, or an empty array if none.

***

### has()

&gt; **has**(`key`): `boolean`

Defined in: [multi-map.ts:71](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L71)

#### Parameters

##### key

`K`

#### Returns

`boolean`

`true` if `key` has at least one value.

***

### hasValue()

&gt; **hasValue**(`key`, `value`): `boolean`

Defined in: [multi-map.ts:99](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L99)

#### Parameters

##### key

`K`

##### value

`V`

#### Returns

`boolean`

`true` if `value` is stored under `key`.

***

### keys()

&gt; **keys**(): `IterableIterator`\<`K`\>

Defined in: [multi-map.ts:114](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L114)

#### Returns

`IterableIterator`\<`K`\>

An iterator over the distinct keys.

***

### set()

&gt; **set**(`key`, `value`): `void`

Defined in: [multi-map.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L56)

Append `value` to the list stored under `key`.

#### Parameters

##### key

`K`

##### value

`V`

#### Returns

`void`

***

### values()

&gt; **values**(): `V`[]

Defined in: [multi-map.ts:119](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/multi-map.ts#L119)

#### Returns

`V`[]

A flat list of every value across all keys, in key-insertion order.
