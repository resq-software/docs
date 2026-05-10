**resq_ai > config**

# Module: config

## Contents

**Structs**

- [`AiConfig`](#aiconfig) - AI configuration.

**Functions**

- [`load_config`](#load_config) - Load config with cascade: env vars -> ~/.resq/ai.toml -> .resq/ai.toml.

---

## resq_ai::config::AiConfig

*Struct*

AI configuration.

**Fields:**
- `provider: crate::provider::Provider` - Selected provider.
- `model: String` - Model identifier.
- `base_url: Option<String>` - Base URL override.
- `max_tokens: u32` - Max tokens in response.
- `timeout_secs: u64` - HTTP request timeout in seconds.

**Methods:**

- `fn api_key(self: &Self) -> &str` - Access the API key.

**Trait Implementations:**

- **Debug**
  - `fn fmt(self: &Self, f: & mut fmt::Formatter) -> fmt::Result`



## resq_ai::config::load_config

*Function*

Load config with cascade: env vars -> ~/.resq/ai.toml -> .resq/ai.toml.

# Errors

Returns an error if no API key is found for the selected provider.

```rust
fn load_config() -> anyhow::Result<AiConfig>
```



