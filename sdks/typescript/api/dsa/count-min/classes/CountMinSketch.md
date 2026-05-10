# Class: CountMinSketch

Defined in: [count-min.ts:17](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/count-min.ts#L17)

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

> **new CountMinSketch**(`epsilon`, `delta`): `CountMinSketch`

Defined in: [count-min.ts:22](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/count-min.ts#L22)

#### Parameters

##### epsilon

`number`

##### delta

`number`

#### Returns

`CountMinSketch`

## Methods

### estimate()

> **estimate**(`key`): `number`

Defined in: [count-min.ts:51](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/count-min.ts#L51)

#### Parameters

##### key

`string`

#### Returns

`number`

***

### increment()

> **increment**(`key`, `count?`): `void`

Defined in: [count-min.ts:43](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/count-min.ts#L43)

#### Parameters

##### key

`string`

##### count?

`number` = `1`

#### Returns

`void`
