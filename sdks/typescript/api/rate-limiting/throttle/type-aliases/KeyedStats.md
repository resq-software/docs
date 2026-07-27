# Type Alias: KeyedStats

&gt; **KeyedStats** = *typeof* `KeyedStatsSchema.Type`

Defined in: [throttle.ts:101](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L101)

Key snapshot for a keyed limiter/manager, inferred from
[KeyedStatsSchema](../variables/KeyedStatsSchema).

A read-only, point-in-time copy — the `keys` array is materialised once and
does **not** stay in sync with later mutations. Invariant: `activeKeys`
equals `keys.length` at the moment of capture, i.e. the number of keys with
live state (an evicted or [KeyedThrottle.cancel](../classes/KeyedThrottle#cancel)led key drops out).
