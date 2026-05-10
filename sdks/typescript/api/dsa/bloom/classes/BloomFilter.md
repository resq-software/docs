# Class: BloomFilter

Defined in: [bloom.ts:17](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/bloom.ts#L17)

Copyright 2026 ResQ Software

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Constructors

### Constructor

> **new BloomFilter**(`capacity`, `errorRate?`): `BloomFilter`

Defined in: [bloom.ts:22](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/bloom.ts#L22)

#### Parameters

##### capacity

`number`

##### errorRate?

`number` = `0.01`

#### Returns

`BloomFilter`

## Methods

### add()

> **add**(`item`): `void`

Defined in: [bloom.ts:45](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/bloom.ts#L45)

#### Parameters

##### item

`string`

#### Returns

`void`

***

### has()

> **has**(`item`): `boolean`

Defined in: [bloom.ts:52](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/bloom.ts#L52)

#### Parameters

##### item

`string`

#### Returns

`boolean`
