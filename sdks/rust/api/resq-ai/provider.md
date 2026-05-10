**resq_ai > provider**

# Module: provider

## Contents

**Enums**

- [`Provider`](#provider) - Supported LLM providers.

**Functions**

- [`complete`](#complete) - Send a completion request to the configured provider.

---

## resq_ai::provider::Provider

*Enum*

Supported LLM providers.

**Variants:**
- `Anthropic` - Anthropic Claude API
- `OpenAi` - OpenAI-compatible Chat Completions API
- `Gemini` - Google Gemini API

**Methods:**

- `fn default_model(self: &Self) -> &'static str` - Default model for this provider.
- `fn default_base_url(self: &Self) -> &'static str` - Default base URL for this provider.
- `fn api_key_env_var(self: &Self) -> &'static str` - Environment variable name for the API key.

**Traits:** Eq, Copy

**Trait Implementations:**

- **Deserialize**
  - `fn deserialize<__D>(__deserializer: __D) -> _serde::__private228::Result<Self, <__D as >::Error>`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`
- **Clone**
  - `fn clone(self: &Self) -> Provider`
- **PartialEq**
  - `fn eq(self: &Self, other: &Provider) -> bool`



## resq_ai::provider::complete

*Function*

Send a completion request to the configured provider.

A single [`reqwest::Client`] is reused across calls to benefit from
connection pooling.

# Errors

Returns an error on network failure, auth failure, or empty response.

```rust
fn complete(config: &super::AiConfig, system: &str, user: &str) -> anyhow::Result<String>
```



