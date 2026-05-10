## Result

```cpp
#include <result.hpp>
```

[Result](#result) type representing either success (Ok) or failure (Err)

Example usage: 
```cpp
Result<int> parse_port(const std::string& s) {
    if (s.empty()) {
        return [Result<int>::Err](#err)(400, "Port cannot be empty");
    }
    int port = std::stoi(s);
    if (port < 1 || port > 65535) {
        return [Result<int>::Err](#err)(400, "Port must be in range [1, 65535]");
    }
    return [Result<int>::Ok](#ok)(port);
}

auto result = parse_port("8080");
if (result.is_ok()) {
    int port = result.unwrap();
    // Use port...
} else {
    spdlog::error("Parse failed: {} (code={})", result.error(), result.code());
}
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`Result`](#result-1)  | Deleted constructor. |
|  | [`Result`](#result-2) |  |
|  | [`Result`](#result-3) |  |
| `bool` | [`is_ok`](#is_ok) `const` | Check if result is successful. |
| `bool` | [`is_err`](#is_err) `const` | Check if result is an error. |
| `const T &` | [`unwrap`](#unwrap) `const` | Get the value (throws if error) Use [is_ok()](#is_ok) to check first, or use [unwrap_or()](#unwrap_or) |
| `T &` | [`unwrap`](#unwrap-1) |  |
| `T` | [`unwrap_or`](#unwrap_or) `const` | Get the value or a default. |
| `T` | [`unwrap_or_else`](#unwrap_or_else) `const` | Get the value or compute from error. |
| `const std::string &` | [`error`](#error) `const` | Get error message. |
| `uint32_t` | [`code`](#code) `const` | Get error code. |
| `auto` | [`map`](#map) `const` | Map the value if Ok, preserve error if Err. |
|  | [`operator bool`](#operatorbool) `const` `explicit` | Convert to bool (true if Ok) |

---

#### Result

```cpp
Result() = delete
```

Deleted constructor.

---

#### Result

`inline`

```cpp
inline Result(const Result & other)
```

---

#### Result

`inline`

```cpp
inline Result(Result && other) noexcept
```

---

#### is_ok

`const`

```cpp
inline bool is_ok() const noexcept
```

Check if result is successful.

---

#### is_err

`const`

```cpp
inline bool is_err() const noexcept
```

Check if result is an error.

---

#### unwrap

`const`

```cpp
inline const T & unwrap() const
```

Get the value (throws if error) Use [is_ok()](#is_ok) to check first, or use [unwrap_or()](#unwrap_or)

---

#### unwrap

`inline`

```cpp
inline T & unwrap()
```

---

#### unwrap_or

`const`

```cpp
inline T unwrap_or(const T & default_value) const
```

Get the value or a default.

---

#### unwrap_or_else

`const`

```cpp
template<typename F> inline T unwrap_or_else(F && op) const
```

Get the value or compute from error.

---

#### error

`const`

```cpp
inline const std::string & error() const noexcept
```

Get error message.

---

#### code

`const`

```cpp
inline uint32_t code() const noexcept
```

Get error code.

---

#### map

`const`

```cpp
template<typename F> inline auto map(F && func) const
```

Map the value if Ok, preserve error if Err.

---

#### operator bool

`const` `explicit`

```cpp
inline explicit operator bool() const noexcept
```

Convert to bool (true if Ok)

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `Result` | [`Ok`](#ok) `static` | Create a successful result. |
| `Result` | [`Ok`](#ok-1) `static` |  |
| `Result` | [`Err`](#err) `static` | Create an error result. |

---

#### Ok

`static`

```cpp
static inline Result Ok(const T & value)
```

Create a successful result.

---

#### Ok

`static`

```cpp
static inline Result Ok(T && value)
```

---

#### Err

`static`

```cpp
static inline Result Err(uint32_t code, std::string_view msg)
```

Create an error result.

#### Parameters
* `code` Error code (use HTTP-style: 400=bad request, 404=not found, 500=internal error) 

* `msg` Human-readable error message

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `T` | [`value_`](#value_)  |  |
| `bool` | [`is_ok_`](#is_ok_)  |  |
| `std::string` | [`error_msg_`](#error_msg_)  |  |
| `uint32_t` | [`error_code_`](#error_code_)  |  |

---

#### value_

```cpp
T value_
```

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
|  | [`Result`](#result-4) |  |
|  | [`Result`](#result-5) |  |

---

#### Result

`inline`

```cpp
inline Result(const T & value, bool ok, std::string msg, uint32_t code)
```

---

#### Result

`inline`

```cpp
inline Result(T && value, bool ok, std::string msg, uint32_t code)
```

