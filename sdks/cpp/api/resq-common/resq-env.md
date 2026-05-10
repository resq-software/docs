# env

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `std::string` | [`get_env_or`](#get_env_or) `inline` | Get environment variable with default value. |
| `double` | [`get_env_double`](#get_env_double) `inline` | Get environment variable as double with default. |
| `int` | [`get_env_int`](#get_env_int) `inline` | Get environment variable as int with default. |
| `bool` | [`get_env_bool`](#get_env_bool) `inline` | Get environment variable as bool with default. |
| `bool` | [`validate_url_env`](#validate_url_env) `inline` | Validate that a URL environment variable has a valid HTTP(S) scheme. |

---

#### get_env_or

`inline`

```cpp
inline std::string get_env_or(const char * name, const char * default_value)
```

Get environment variable with default value.

#### Parameters
* `name` Environment variable name 

* `default_value` Default value if not set or empty 

#### Returns
The environment variable value or default

---

#### get_env_double

`inline`

```cpp
inline double get_env_double(const char * name, double default_value)
```

Get environment variable as double with default.

#### Parameters
* `name` Environment variable name 

* `default_value` Default value if not set, empty, or unparseable 

#### Returns
Parsed double or default

---

#### get_env_int

`inline`

```cpp
inline int get_env_int(const char * name, int default_value)
```

Get environment variable as int with default.

#### Parameters
* `name` Environment variable name 

* `default_value` Default value if not set, empty, or unparseable 

#### Returns
Parsed int or default

---

#### get_env_bool

`inline`

```cpp
inline bool get_env_bool(const char * name, bool default_value)
```

Get environment variable as bool with default.

Accepts: "true", "1", "yes" (case-insensitive) as true. Accepts: "false", "0", "no" (case-insensitive) as false.

#### Parameters
* `name` Environment variable name 

* `default_value` Default value if not set, empty, or unrecognized 

#### Returns
Parsed bool or default

---

#### validate_url_env

`inline`

```cpp
inline bool validate_url_env(const char * env_name, bool required)
```

Validate that a URL environment variable has a valid HTTP(S) scheme.

#### Parameters
* `env_name` Name of the environment variable 

* `required` If true, the variable must be set and non-empty 

#### Returns
true if validation passes (or variable is optional and unset)

