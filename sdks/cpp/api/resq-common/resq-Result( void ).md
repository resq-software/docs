## Result&lt; void >

```cpp
#include <result.hpp>
```

Specialization for void (operation succeeded with no return value)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`Result`](#result-6)  | Deleted constructor. |
| `bool` | [`is_ok`](#is_ok-1) `const` |  |
| `bool` | [`is_err`](#is_err-1) `const` |  |
| `const std::string &` | [`error`](#error-1) `const` |  |
| `uint32_t` | [`code`](#code-1) `const` |  |
| `void` | [`unwrap`](#unwrap-2) `const` |  |
|  | [`operator bool`](#operatorbool-1) `const` `explicit` |  |

---

#### Result

```cpp
Result() = delete
```

Deleted constructor.

---

#### is_ok

`const`

```cpp
inline bool is_ok() const noexcept
```

---

#### is_err

`const`

```cpp
inline bool is_err() const noexcept
```

---

#### error

`const`

```cpp
inline const std::string & error() const noexcept
```

---

#### code

`const`

```cpp
inline uint32_t code() const noexcept
```

---

#### unwrap

`const`

```cpp
inline void unwrap() const
```

---

#### operator bool

`const` `explicit`

```cpp
inline explicit operator bool() const noexcept
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `Result` | [`Ok`](#ok-2) `static` |  |
| `Result` | [`Err`](#err-1) `static` |  |

---

#### Ok

`static`

```cpp
static inline Result Ok()
```

---

#### Err

`static`

```cpp
static inline Result Err(uint32_t code, std::string_view msg)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`is_ok_`](#is_ok_-1)  |  |
| `std::string` | [`error_msg_`](#error_msg_-1)  |  |
| `uint32_t` | [`error_code_`](#error_code_-1)  |  |

---

#### is_ok_

```cpp
bool is_ok_
```

---

#### error_msg_

```cpp
std::string error_msg_
```

---

#### error_code_

```cpp
uint32_t error_code_
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`Result`](#result-7) |  |

---

#### Result

`inline`

```cpp
inline Result(bool ok, std::string msg, uint32_t code)
```

