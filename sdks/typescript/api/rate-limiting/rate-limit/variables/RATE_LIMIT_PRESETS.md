# Variable: RATE\_LIMIT\_PRESETS

&gt; `const` **RATE\_LIMIT\_PRESETS**: `object`

Defined in: [rate-limit.ts:315](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L315)

Pre-tuned `(windowMs, maxRequests)` pairs for common traffic shapes.

The presets are deliberately conservative — tighten them per-route
once you have real traffic data:

- `auth` — 5 requests / 15 min. Login, password reset, MFA enrol.
  Tight enough to thwart credential stuffing; loose enough to avoid
  locking out a legitimate user on a flaky network.
- `api`  — 100 requests / minute. General-purpose authenticated API.
- `read` — 200 requests / minute. Idempotent read endpoints (search,
  listing) where caching upstream is feasible.
- `upload` — 20 requests / hour. File ingestion endpoints. Per-hour
  window discourages bulk-uploading abuse without blocking iterative
  user workflows.

## Type Declaration

### api

&gt; `readonly` **api**: `object`

#### api.maxRequests

&gt; `readonly` **maxRequests**: `100` = `100`

#### api.windowMs

&gt; `readonly` **windowMs**: `number`

### auth

&gt; `readonly` **auth**: `object`

#### auth.maxRequests

&gt; `readonly` **maxRequests**: `5` = `5`

#### auth.windowMs

&gt; `readonly` **windowMs**: `number`

### read

&gt; `readonly` **read**: `object`

#### read.maxRequests

&gt; `readonly` **maxRequests**: `200` = `200`

#### read.windowMs

&gt; `readonly` **windowMs**: `number`

### upload

&gt; `readonly` **upload**: `object`

#### upload.maxRequests

&gt; `readonly` **maxRequests**: `20` = `20`

#### upload.windowMs

&gt; `readonly` **windowMs**: `number`

## Example

```ts
const decision = await store.check(
  `user:${userId}`,
  RATE_LIMIT_PRESETS.api.windowMs,
  RATE_LIMIT_PRESETS.api.maxRequests,
);
```
