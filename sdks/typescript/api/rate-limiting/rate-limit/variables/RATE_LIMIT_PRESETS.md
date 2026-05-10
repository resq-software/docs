# Variable: RATE\_LIMIT\_PRESETS

> `const` **RATE\_LIMIT\_PRESETS**: `object`

Defined in: [rate-limit.ts:139](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L139)

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
