# Variable: RATE\_LIMIT\_PRESETS

> `const` **RATE\_LIMIT\_PRESETS**: `object`

Defined in: [rate-limit.ts:256](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L256)

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

> `readonly` **api**: `object`

#### api.maxRequests

> `readonly` **maxRequests**: `100` = `100`

#### api.windowMs

> `readonly` **windowMs**: `number`

### auth

> `readonly` **auth**: `object`

#### auth.maxRequests

> `readonly` **maxRequests**: `5` = `5`

#### auth.windowMs

> `readonly` **windowMs**: `number`

### read

> `readonly` **read**: `object`

#### read.maxRequests

> `readonly` **maxRequests**: `200` = `200`

#### read.windowMs

> `readonly` **windowMs**: `number`

### upload

> `readonly` **upload**: `object`

#### upload.maxRequests

> `readonly` **maxRequests**: `20` = `20`

#### upload.windowMs

> `readonly` **windowMs**: `number`

## Example

```ts
const decision = await store.check(
  `user:${userId}`,
  RATE_LIMIT_PRESETS.api.windowMs,
  RATE_LIMIT_PRESETS.api.maxRequests,
);
```
