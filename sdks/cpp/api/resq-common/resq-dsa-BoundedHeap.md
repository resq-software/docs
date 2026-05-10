## BoundedHeap

```cpp
#include <heap.hpp>
```

Bounded heap for top-K element selection.

A priority queue that maintains a fixed maximum size. When capacity is reached, new elements only replace the worst element if they are better (have lower distance according to the provided function).

#### Parameters
* `T` Type of elements stored in the heap

limit_ >= 1 

dist_ must not throw or mutate state

:::note
Provides O(log n) insert and O(1) peek 

:::

:::note
Memory: O(limit_) elements maximum 

:::

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`BoundedHeap`](#boundedheap-1) | Construct a bounded heap. |
| `void` | [`insert`](#insert) | Insert an element into the heap. |
| `const T *` | [`peek`](#peek) `const` | Peek at the worst (highest-distance) element in the heap. |
| `std::vector< T >` | [`to_sorted`](#to_sorted) `const` | Extract all elements sorted by distance. |
| `std::size_t` | [`size`](#size) `const` | Get current number of elements in heap. |
| `bool` | [`empty`](#empty) `const` | Check if heap is empty. |

---

#### BoundedHeap

`inline`

```cpp
inline BoundedHeap(std::size_t limit, DistFn dist)
```

Construct a bounded heap.

#### Parameters
* `limit` Maximum number of elements to retain 

* `dist` Distance function - lower values are preferred

#### Exceptions
* `std::invalid_argument` If limit &lt; 1

Heap is empty and ready for inserts

---

#### insert

`inline`

```cpp
inline void insert(T entry)
```

Insert an element into the heap.

If heap is not full, adds element. If heap is full, only adds element if it is better than the current worst (root).

#### Parameters
* `entry` Element to insert

If heap was not full, element is in heap 

If heap was full and entry is better than root, root is replaced 

Heap property is maintained after insert

---

#### peek

`const`

```cpp
inline const T * peek() const
```

Peek at the worst (highest-distance) element in the heap.

#### Returns
Pointer to root element (max distance), or nullptr if empty

:::note
The returned pointer is invalid after [insert()](#insert) or destruction 

:::

---

#### to_sorted

`const`

```cpp
inline std::vector< T > to_sorted() const
```

Extract all elements sorted by distance.

#### Returns
Vector of elements sorted from best to worst

:::note
Returns copy of elements; original heap is unchanged 

:::

---

#### size

`const`

```cpp
inline std::size_t size() const
```

Get current number of elements in heap.

#### Returns
Number of elements (0 to limit_)

---

#### empty

`const`

```cpp
inline bool empty() const
```

Check if heap is empty.

### Public Types

| Name | Description |
|------|-------------|
| [`DistFn`](#distfn)  | Distance function type. |

---

#### DistFn

```cpp
std::function< double(const T &)> DistFn()
```

Distance function type.

Takes a reference to an element and returns a distance value. Lower values are considered "better" (closer to target).

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `std::vector< T >` | [`data_`](#data_)  | Internal heap storage. |
| `std::size_t` | [`limit_`](#limit_)  | Maximum capacity. |
| `DistFn` | [`dist_`](#dist_)  | Distance evaluation function. |

---

#### data_

```cpp
std::vector< T > data_
```

Internal heap storage.

---

#### limit_

```cpp
std::size_t limit_
```

Maximum capacity.

---

#### dist_

```cpp
DistFn dist_
```

Distance evaluation function.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`sift_up`](#sift_up) | Restore heap property by moving element up. |
| `void` | [`sift_down`](#sift_down) | Restore heap property by moving element down. |

---

#### sift_up

`inline`

```cpp
inline void sift_up(std::size_t i)
```

Restore heap property by moving element up.

---

#### sift_down

`inline`

```cpp
inline void sift_down(std::size_t i)
```

Restore heap property by moving element down.

