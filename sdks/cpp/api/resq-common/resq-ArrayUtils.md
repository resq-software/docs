## ArrayUtils

```cpp
#include <array_utils.hpp>
```

Fast operations on sorted uint32_t arrays.

All input arrays MUST be sorted in ascending order. Output arrays are dynamically allocated - caller must free with delete[].

Example: 
```cpp
uint32_t available[] = {1, 3, 5, 7, 9};
uint32_t assigned[] = {2, 3, 4, 5};

uint32_t* free_drones = nullptr;
size_t count = [ArrayUtils::exclude_scalar](#exclude_scalar)(available, 5, assigned, 4, &free_drones);
// free_drones = {1, 7, 9}, count = 3

delete[] free_drones;
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `size_t` | [`and_scalar`](#and_scalar) `static` | Fast intersection (AND) of two sorted arrays. |
| `size_t` | [`or_scalar`](#or_scalar) `static` | Fast union (OR) of two sorted arrays. |
| `size_t` | [`exclude_scalar`](#exclude_scalar) `static` | Exclude elements (A - B): elements in A but not in B. |
| `bool` | [`skip_index_to_id`](#skip_index_to_id) `static` | Binary search with skip-ahead. |
| `bool` | [`arrays_equal`](#arrays_equal) `static` | Check if arrays are equal. |
| `bool` | [`is_sorted`](#is_sorted) `static` | Check if array is sorted. |
| `std::vector< uint32_t >` | [`intersect`](#intersect) `static` | Intersection of two vectors (returns new vector) |
| `std::vector< uint32_t >` | [`union_of`](#union_of) `static` | Union of two vectors (returns new vector) |
| `std::vector< uint32_t >` | [`exclude`](#exclude) `static` | Exclude elements (a - b) (returns new vector) |
| `bool` | [`contains`](#contains) `static` | Check if element exists in sorted array. |
| `bool` | [`contains`](#contains-1) `static` |  |

---

#### and_scalar

`static`

```cpp
static inline size_t and_scalar(const uint32_t * A, size_t lenA, const uint32_t * B, size_t lenB, uint32_t ** out)
```

Fast intersection (AND) of two sorted arrays.

#### Parameters
* `A` First sorted array 

* `lenA` Length of array A 

* `B` Second sorted array 

* `lenB` Length of array B 

* `out` Output array (allocated by function, caller must delete[]) 

#### Returns
Size of intersection (elements in out)

Time complexity: O(lenA + lenB) Space complexity: O(min(lenA, lenB))

---

#### or_scalar

`static`

```cpp
static inline size_t or_scalar(const uint32_t * A, size_t lenA, const uint32_t * B, size_t lenB, uint32_t ** out)
```

Fast union (OR) of two sorted arrays.

#### Returns
Size of union (elements in out)

Time complexity: O(lenA + lenB) Space complexity: O(lenA + lenB)

---

#### exclude_scalar

`static`

```cpp
static inline size_t exclude_scalar(const uint32_t * src, size_t lenSrc, const uint32_t * filter, size_t lenFilter, uint32_t ** out)
```

Exclude elements (A - B): elements in A but not in B.

#### Parameters
* `src` Source array 

* `lenSrc` Length of source 

* `filter` Elements to exclude 

* `lenFilter` Length of filter 

* `out` Output array (allocated by function) 

#### Returns
Size of result

Time complexity: O(lenSrc + lenFilter)

---

#### skip_index_to_id

`static`

```cpp
static inline bool skip_index_to_id(uint32_t & curr_index, const uint32_t * array, uint32_t array_len, uint32_t id)
```

Binary search with skip-ahead.

Searches for 'id' in sorted array. If found, sets curr_index to that index. If not found, sets curr_index to the index of the next larger element.

#### Parameters
* `curr_index` Current index (input/output) 

* `array` Sorted array to search 

* `array_len` Length of array 

* `id` Value to search for 

#### Returns
true if id was found, false otherwise

---

#### arrays_equal

`static`

```cpp
static inline bool arrays_equal(const uint32_t * a, size_t len_a, const uint32_t * b, size_t len_b)
```

Check if arrays are equal.

---

#### is_sorted

`static`

```cpp
static inline bool is_sorted(const uint32_t * array, size_t len)
```

Check if array is sorted.

---

#### intersect

`static`

```cpp
static inline std::vector< uint32_t > intersect(const std::vector< uint32_t > & a, const std::vector< uint32_t > & b)
```

Intersection of two vectors (returns new vector)

---

#### union_of

`static`

```cpp
static inline std::vector< uint32_t > union_of(const std::vector< uint32_t > & a, const std::vector< uint32_t > & b)
```

Union of two vectors (returns new vector)

---

#### exclude

`static`

```cpp
static inline std::vector< uint32_t > exclude(const std::vector< uint32_t > & src, const std::vector< uint32_t > & filter)
```

Exclude elements (a - b) (returns new vector)

---

#### contains

`static`

```cpp
static inline bool contains(const uint32_t * array, size_t len, uint32_t value)
```

Check if element exists in sorted array.

---

#### contains

`static`

```cpp
static inline bool contains(const std::vector< uint32_t > & vec, uint32_t value)
```

