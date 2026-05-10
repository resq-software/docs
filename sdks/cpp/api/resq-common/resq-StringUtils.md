## StringUtils

```cpp
#include <string_utils.hpp>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `size_t` | [`split`](#split) `static` | Split string by delimiter with optional trimming. |
| `size_t` | [`split`](#split-1) `static` | Split string by single character delimiter (faster) |
| `std::string` | [`trim`](#trim) `static` | Trim whitespace from both ends. |
| `std::string` | [`ltrim`](#ltrim) `static` | Trim whitespace from left. |
| `std::string` | [`rtrim`](#rtrim) `static` | Trim whitespace from right. |
| `std::string` | [`join`](#join) `static` | Join strings with delimiter. |
| `std::string` | [`to_lower`](#to_lower) `static` | Convert string to lowercase. |
| `std::string` | [`to_upper`](#to_upper) `static` | Convert string to uppercase. |
| `bool` | [`starts_with`](#starts_with) `static` | Check if string starts with prefix. |
| `bool` | [`ends_with`](#ends_with) `static` | Check if string ends with suffix. |
| `bool` | [`contains`](#contains-2) `static` | Check if string contains substring. |
| `std::string` | [`replace_all`](#replace_all) `static` | Replace all occurrences of 'from' with 'to'. |
| `void` | [`split_respecting_quotes`](#split_respecting_quotes) `static` | Split keeping quoted sections intact. |
| `std::string` | [`remove_whitespace`](#remove_whitespace) `static` | Remove all whitespace from string. |
| `std::string` | [`pad_left`](#pad_left) `static` | Pad string to width with fill character. |
| `std::string` | [`pad_right`](#pad_right) `static` |  |
| `std::string` | [`escape_json`](#escape_json) `static` | Escape special characters for JSON. |

---

#### split

`static`

```cpp
static inline size_t split(const std::string & s, std::vector< std::string > & result, const std::string & delim, bool keep_empty, bool trim_space)
```

Split string by delimiter with optional trimming.

#### Parameters
* `s` Input string 

* `result` Output vector (appends to existing elements) 

* `delim` Delimiter string 

* `keep_empty` Keep empty tokens 

* `trim_space` Trim whitespace from each token 

#### Returns
Number of characters processed

Example: 
```cpp
std::vector<std::string> parts;
[StringUtils::split](#split)("drone1,drone2, drone3", parts, ",");
// parts = {"drone1", "drone2", "drone3"}
```

---

#### split

`static`

```cpp
static inline size_t split(const std::string & s, std::vector< std::string > & result, char delim, bool keep_empty, bool trim_space)
```

Split string by single character delimiter (faster)

---

#### trim

`static`

```cpp
static inline std::string trim(const std::string & s)
```

Trim whitespace from both ends.

---

#### ltrim

`static`

```cpp
static inline std::string ltrim(const std::string & s)
```

Trim whitespace from left.

---

#### rtrim

`static`

```cpp
static inline std::string rtrim(const std::string & s)
```

Trim whitespace from right.

---

#### join

`static`

```cpp
static inline std::string join(const std::vector< std::string > & parts, const std::string & delimiter)
```

Join strings with delimiter.

Example: 
```cpp
std::vector<std::string> ids = {"DRONE-1", "DRONE-2", "DRONE-3"};
std::string csv = [StringUtils::join](#join)(ids, ", ");
// csv = "DRONE-1, DRONE-2, DRONE-3"
```

---

#### to_lower

`static`

```cpp
static inline std::string to_lower(const std::string & s)
```

Convert string to lowercase.

---

#### to_upper

`static`

```cpp
static inline std::string to_upper(const std::string & s)
```

Convert string to uppercase.

---

#### starts_with

`static`

```cpp
static inline bool starts_with(std::string_view s, std::string_view prefix)
```

Check if string starts with prefix.

---

#### ends_with

`static`

```cpp
static inline bool ends_with(std::string_view s, std::string_view suffix)
```

Check if string ends with suffix.

---

#### contains

`static`

```cpp
static inline bool contains(std::string_view s, std::string_view substr)
```

Check if string contains substring.

---

#### replace_all

`static`

```cpp
static inline std::string replace_all(std::string s, const std::string & from, const std::string & to)
```

Replace all occurrences of 'from' with 'to'.

---

#### split_respecting_quotes

`static`

```cpp
static inline void split_respecting_quotes(const std::string & s, std::vector< std::string > & result, char delimiter, char quote_char)
```

Split keeping quoted sections intact.

Example: 
```cpp
std::vector<std::string> parts;
[StringUtils::split_respecting_quotes](#split_respecting_quotes)("field1,\"value,with,commas\",field3", parts, ',', '"');
// parts = {"field1", "value,with,commas", "field3"}
```

---

#### remove_whitespace

`static`

```cpp
static inline std::string remove_whitespace(const std::string & s)
```

Remove all whitespace from string.

---

#### pad_left

`static`

```cpp
static inline std::string pad_left(const std::string & s, size_t width, char fill)
```

Pad string to width with fill character.

---

#### pad_right

`static`

```cpp
static inline std::string pad_right(const std::string & s, size_t width, char fill)
```

---

#### escape_json

`static`

```cpp
static inline std::string escape_json(const std::string & s)
```

Escape special characters for JSON.

