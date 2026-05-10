## FileUtils

```cpp
#include <file_utils.hpp>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`directory_exists`](#directory_exists) `static` `inline` | Check if directory exists. |
| `bool` | [`file_exists`](#file_exists) `static` `inline` | Check if file exists. |
| `bool` | [`path_exists`](#path_exists) `static` `inline` | Check if path exists (file or directory) |
| `Result< void >` | [`create_directory`](#create_directory) `static` `inline` | Create directory (and parent directories if needed) |
| `Result< void >` | [`copy_directory`](#copy_directory) `static` `inline` | Copy directory (recursive) Uses hard links when possible for efficiency (like Typesense) |
| `Result< void >` | [`move_path`](#move_path) `static` `inline` | Move/rename path (works for files and directories) |
| `Result< void >` | [`delete_path`](#delete_path) `static` `inline` | Delete path (file or directory) |
| `Result< size_t >` | [`file_size`](#file_size) `static` `inline` | Get file size in bytes. |
| `Result< std::vector< std::string > >` | [`list_files`](#list_files) `static` `inline` | List files in directory. |
| `Result< std::string >` | [`read_file`](#read_file) `static` `inline` | Read entire file into string. |
| `Result< std::vector< std::string > >` | [`read_lines`](#read_lines) `static` `inline` | Read file into vector of lines. |
| `Result< void >` | [`write_file`](#write_file) `static` `inline` | Write string to file (overwrites existing) |
| `Result< void >` | [`append_file`](#append_file) `static` `inline` | Append string to file. |
| `std::string` | [`get_extension`](#get_extension) `static` `inline` | Get file extension (without dot) |
| `std::string` | [`get_filename`](#get_filename) `static` `inline` | Get filename without directory. |
| `std::string` | [`get_directory`](#get_directory) `static` `inline` | Get directory path. |
| `Result< std::string >` | [`absolute_path`](#absolute_path) `static` `inline` | Get absolute path. |
| `Result< std::string >` | [`current_directory`](#current_directory) `static` `inline` | Get current working directory. |

---

#### directory_exists

`static` `inline`

```cpp
static inline bool directory_exists(const std::string & dir_path) noexcept
```

Check if directory exists.

---

#### file_exists

`static` `inline`

```cpp
static inline bool file_exists(const std::string & file_path) noexcept
```

Check if file exists.

---

#### path_exists

`static` `inline`

```cpp
static inline bool path_exists(const std::string & path) noexcept
```

Check if path exists (file or directory)

---

#### create_directory

`static` `inline`

```cpp
static inline Result< void > create_directory(const std::string & dir_path)
```

Create directory (and parent directories if needed)

---

#### copy_directory

`static` `inline`

```cpp
static inline Result< void > copy_directory(const std::string & from_path, const std::string & to_path)
```

Copy directory (recursive) Uses hard links when possible for efficiency (like Typesense)

---

#### move_path

`static` `inline`

```cpp
static inline Result< void > move_path(const std::string & from_path, const std::string & to_path)
```

Move/rename path (works for files and directories)

---

#### delete_path

`static` `inline`

```cpp
static inline Result< void > delete_path(const std::string & path, bool recursive)
```

Delete path (file or directory)

#### Parameters
* `recursive` If true, delete directory contents recursively

---

#### file_size

`static` `inline`

```cpp
static inline Result< size_t > file_size(const std::string & file_path)
```

Get file size in bytes.

---

#### list_files

`static` `inline`

```cpp
static inline Result< std::vector< std::string > > list_files(const std::string & dir_path, const std::string & pattern)
```

List files in directory.

#### Parameters
* `pattern` Optional glob pattern (e.g., "*.txt")

---

#### read_file

`static` `inline`

```cpp
static inline Result< std::string > read_file(const std::string & file_path)
```

Read entire file into string.

---

#### read_lines

`static` `inline`

```cpp
static inline Result< std::vector< std::string > > read_lines(const std::string & file_path)
```

Read file into vector of lines.

---

#### write_file

`static` `inline`

```cpp
static inline Result< void > write_file(const std::string & file_path, const std::string & content)
```

Write string to file (overwrites existing)

---

#### append_file

`static` `inline`

```cpp
static inline Result< void > append_file(const std::string & file_path, const std::string & content)
```

Append string to file.

---

#### get_extension

`static` `inline`

```cpp
static inline std::string get_extension(const std::string & file_path)
```

Get file extension (without dot)

---

#### get_filename

`static` `inline`

```cpp
static inline std::string get_filename(const std::string & file_path)
```

Get filename without directory.

---

#### get_directory

`static` `inline`

```cpp
static inline std::string get_directory(const std::string & file_path)
```

Get directory path.

---

#### absolute_path

`static` `inline`

```cpp
static inline Result< std::string > absolute_path(const std::string & path)
```

Get absolute path.

---

#### current_directory

`static` `inline`

```cpp
static inline Result< std::string > current_directory()
```

Get current working directory.

