## PathResult

```cpp
#include <graph.hpp>
```

[Result](resq-Result.md#result) of a shortest path search.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `std::vector< Id >` | [`path`](#path)  | Vertices on the path from start to end. |
| `double` | [`cost`](#cost)  | Total cost of the path. |

---

#### path

```cpp
std::vector< Id > path
```

Vertices on the path from start to end.

---

#### cost

```cpp
double cost
```

Total cost of the path.

