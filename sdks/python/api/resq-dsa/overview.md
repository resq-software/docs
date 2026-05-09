<a id="resq_dsa"></a>

# resq\_dsa

ResQ Data Structures and Algorithms Library.

This package provides performant data structures and algorithms
commonly used in the ResQ disaster response system.

Classes:
BoundedHeap: Bounded min-heap for top-k queries.
Graph: Directed weighted graph with pathfinding algorithms.
Trie: Prefix tree for efficient string operations.
BloomFilter: Probabilistic set membership structure.
CountMinSketch: Probabilistic frequency estimation.

Functions:
rabin_karp: Rabin-Karp string pattern matching algorithm.

**Example**:

  >>> from resq_dsa import BoundedHeap, Trie, BloomFilter
  >>> trie = Trie()
  >>> trie.insert("disaster")
  >>> bloom = BloomFilter(capacity=1000)
  >>> bloom.add("emergency")
  >>> bloom.has("emergency")
  True

<a id="resq_dsa.BloomFilter"></a>

## BloomFilter

<a id="resq_dsa.CountMinSketch"></a>

## CountMinSketch

<a id="resq_dsa.Graph"></a>

## Graph

<a id="resq_dsa.BoundedHeap"></a>

## BoundedHeap

<a id="resq_dsa.Trie"></a>

## Trie

<a id="resq_dsa.rabin_karp"></a>

## rabin\_karp
