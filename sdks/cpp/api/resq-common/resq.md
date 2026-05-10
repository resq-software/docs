# resq

Copyright 2026 ResQ Software.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
```
http://www.apache.org/licenses/LICENSE-2.0
```
 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
```
http://www.apache.org/licenses/LICENSE-2.0
```
 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Geographic utilities for drone navigation

Provides geospatial calculations for drone swarm coordination, including distance calculations and coordinate validation.

:::note
All coordinates use WGS84 coordinate system 

:::

:::note
Distances are calculated in meters

:::

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
```
http://www.apache.org/licenses/LICENSE-2.0
```
 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

No-Fly Zone (NFZ) and geofencing utilities

Provides geofencing functionality for FAA Part 107 compliance:

* No-fly zone polygon definitions

* Point-in-polygon checking

* Path/line segment intersection detection

This module implements AV-03 (Geofencing) control from the compliance catalog. Used by strategic-dtsop to reject flight plans intersecting NFZ polygons.

:::note
All coordinates use WGS84 coordinate system 

:::

### Classes

| Name | Description |
|------|-------------|
| [`ArrayUtils`](./resq-ArrayUtils.md#arrayutils) | Fast operations on sorted uint32_t arrays. |
| [`FileHandle`](./resq-FileHandle.md#filehandle) | RAII file handle that ensures closure. |
| [`Result`](./resq-Result.md#result) | [Result](./resq-Result.md#result) type representing either success (Ok) or failure (Err) |
| [`Result< void >`](resq-Result( void ).md#resultvoid) | Specialization for void (operation succeeded with no return value) |
| [`FileUtils`](./resq-FileUtils.md#fileutils) |  |
| [`StringUtils`](./resq-StringUtils.md#stringutils) |  |

### Variables

| Return | Name | Description |
|--------|------|-------------|
| `constexpr const char *` | [`RESQ_COMMON_VERSION`](#resq_common_version)  |  |

---

#### RESQ_COMMON_VERSION

```cpp
constexpr const char * RESQ_COMMON_VERSION = "1.0.0"
```

