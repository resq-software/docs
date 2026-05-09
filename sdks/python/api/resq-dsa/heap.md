<a id="resq_dsa.heap"></a>

# resq\_dsa.heap

Bounded heap data structure for top-k queries.

This module provides a bounded min-heap implementation for maintaining
the k smallest (or largest) elements from a stream of data.

<a id="resq_dsa.heap.Callable"></a>

## Callable

<a id="resq_dsa.heap.Generic"></a>

## Generic

<a id="resq_dsa.heap.TypeVar"></a>

## TypeVar

<a id="resq_dsa.heap.T"></a>

#### T

<a id="resq_dsa.heap.BoundedHeap"></a>

## BoundedHeap Objects

```python
class BoundedHeap(Generic[T])
```

Bounded min-heap for tracking top-k elements by distance.

Maintains a fixed-size heap that keeps only the k smallest elements
according to a provided distance/cost function. Useful for k-nearest
neighbors, top-k queries, and streaming data processing.

**Attributes**:

- `_limit` - Maximum number of elements to maintain.
- `_dist` - Function to compute distance/score for elements.
- `_data` - Internal heap storage.
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> for i in [5, 2, 8, 1, 9]:
  ...     heap.insert(i)
  >>> heap.to_sorted()
  [1, 2, 5]

<a id="resq_dsa.heap.BoundedHeap.__init__"></a>

#### BoundedHeap.\_\_init\_\_

```python
def __init__(limit: int, dist: Callable[[T], float]) -> None
```

Initialize the bounded heap.

**Arguments**:

- `limit` - Maximum number of elements to maintain.
- `dist` - Function to compute the distance/score for ranking.
  

**Raises**:

- `ValueError` - If limit is less than 1.
  

**Example**:

  >>> heap = BoundedHeap(limit=5, dist=lambda x: abs(x - 10))

<a id="resq_dsa.heap.BoundedHeap.insert"></a>

#### BoundedHeap.insert

```python
def insert(entry: T) -> None
```

Insert an element into the heap.

If the heap is not full, the element is added. If the heap is full
and the new element has a lower distance than the current maximum,
the maximum is replaced with the new element.

**Arguments**:

- `entry` - The element to insert.
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> heap.insert(5)
  >>> heap.insert(2)

<a id="resq_dsa.heap.BoundedHeap.peek"></a>

#### BoundedHeap.peek

```python
def peek() -> T | None
```

Return the element with minimum distance without removing it.

**Returns**:

  The element with lowest distance, or None if heap is empty.
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> heap.insert(5)
  >>> heap.peek()
  5

<a id="resq_dsa.heap.BoundedHeap.to_sorted"></a>

#### BoundedHeap.to\_sorted

```python
def to_sorted() -> list[T]
```

Return the heap contents sorted by distance.

**Returns**:

  List of elements sorted by distance (ascending).
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> heap.insert(5)
  >>> heap.insert(2)
  >>> heap.to_sorted()
  [2, 5]

<a id="resq_dsa.heap.BoundedHeap.size"></a>

#### BoundedHeap.size

```python
@property
def size() -> int
```

Return the current number of elements in the heap.

**Returns**:

  Number of elements currently stored.
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> heap.insert(1)
  >>> heap.insert(2)
  >>> heap.size
  2
