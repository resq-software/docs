<a id="resq_dsa.count_min"></a>

# resq\_dsa.count\_min

Count-Min Sketch probabilistic data structure.

This module provides a Count-Min Sketch implementation for frequency
estimation of elements in a data stream. Useful for top-k queries and
heavy hitter detection with sub-linear space.

<a id="resq_dsa.count_min.math"></a>

## math

<a id="resq_dsa.count_min.CountMinSketch"></a>

## CountMinSketch Objects

```python
class CountMinSketch()
```

Probabilistic data structure for frequency estimation.

The Count-Min Sketch uses multiple hash tables to estimate the count
of elements in a stream with guaranteed error bounds. It provides
an upper bound on frequencies (never underestimates, but may overestimate).

**Attributes**:

- `_w` - Number of columns in the sketch (width).
- `_d` - Number of rows in the sketch (depth).
- `_table` - The hash table storage.
  

**Example**:

  >>> sketch = CountMinSketch(epsilon=0.1, delta=0.01)
  >>> sketch.increment("item1")
  >>> sketch.increment("item1")
  >>> sketch.increment("item2")
  >>> sketch.estimate("item1")  # Returns at least 2
  2
  >>> sketch.estimate("item2")  # Returns at least 1
  1

<a id="resq_dsa.count_min.CountMinSketch.__init__"></a>

#### CountMinSketch.\_\_init\_\_

```python
def __init__(epsilon: float, delta: float) -> None
```

Initialize the Count-Min Sketch.

**Arguments**:

- `epsilon` - Error parameter. The error in estimation is at most epsilon
  with probability delta. Must be in (0, 1).
- `delta` - Confidence parameter. Must be in (0, 1).
  

**Raises**:

- `ValueError` - If epsilon or delta are not in (0, 1).
  

**Example**:

  >>> sketch = CountMinSketch(epsilon=0.1, delta=0.01)

<a id="resq_dsa.count_min.CountMinSketch.increment"></a>

#### CountMinSketch.increment

```python
def increment(key: str, count: int = 1) -> None
```

Increment the count for a key.

**Arguments**:

- `key` - The key to increment.
- `count` - Amount to increment by (default: 1).
  

**Example**:

  >>> sketch = CountMinSketch(epsilon=0.1, delta=0.01)
  >>> sketch.increment("error")
  >>> sketch.increment("error", 5)

<a id="resq_dsa.count_min.CountMinSketch.estimate"></a>

#### CountMinSketch.estimate

```python
def estimate(key: str) -> int
```

Estimate the count for a key.

Returns the minimum across all hash table rows, providing an
upper bound on the true count.

**Arguments**:

- `key` - The key to estimate.
  

**Returns**:

  Estimated count (upper bound).
  

**Example**:

  >>> sketch = CountMinSketch(epsilon=0.1, delta=0.01)
  >>> sketch.increment("event")
  >>> sketch.estimate("event")
  1
