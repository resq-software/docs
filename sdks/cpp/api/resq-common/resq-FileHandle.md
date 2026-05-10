## FileHandle

```cpp
#include <file_utils.hpp>
```

RAII file handle that ensures closure.

Example: 
```cpp
{
    auto file = [FileHandle::open](#open)("data.txt", std::ios::out);
    if (file.is_open()) {
        file.stream() << "Hello, World!\n";
    }
}  // File automatically closed here
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`FileHandle`](#filehandle-1)  | Defaulted constructor. |
|  | [`FileHandle`](#filehandle-2)  | Deleted constructor. |
|  | [`FileHandle`](#filehandle-3) |  |
| `bool` | [`is_open`](#is_open) `const` |  |
| `std::fstream &` | [`stream`](#stream) |  |

---

#### FileHandle

```cpp
FileHandle() = default
```

Defaulted constructor.

---

#### FileHandle

```cpp
FileHandle(const FileHandle &) = delete
```

Deleted constructor.

---

#### FileHandle

`inline`

```cpp
inline FileHandle(FileHandle && other) noexcept
```

---

#### is_open

`const`

```cpp
inline bool is_open() const
```

---

#### stream

`inline`

```cpp
inline std::fstream & stream()
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `FileHandle` | [`open`](#open) `static` |  |

---

#### open

`static`

```cpp
static inline FileHandle open(const std::string & path, std::ios::openmode mode)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `std::fstream` | [`stream_`](#stream_)  |  |

---

#### stream_

```cpp
std::fstream stream_
```

