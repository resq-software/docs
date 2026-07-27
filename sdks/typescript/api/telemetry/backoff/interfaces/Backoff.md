# Interface: Backoff

Defined in: [backoff.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L44)

## Methods

### attempts()

&gt; **attempts**(): `number`

Defined in: [backoff.ts:50](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L50)

Number of delays handed out since the last reset.

#### Returns

`number`

***

### nextDelayMs()

&gt; **nextDelayMs**(): `number`

Defined in: [backoff.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L46)

Delay for the next attempt, advancing the schedule.

#### Returns

`number`

***

### peekDelayMs()

&gt; **peekDelayMs**(): `number`

Defined in: [backoff.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L48)

The delay the next `nextDelayMs()` will return, without advancing.

#### Returns

`number`

***

### reset()

&gt; **reset**(): `void`

Defined in: [backoff.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L52)

Return to the initial delay — call after a successful connect.

#### Returns

`void`
