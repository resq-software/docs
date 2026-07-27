# Class: Timers

Defined in: [packages/helpers/src/utils/timers.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/timers.ts#L52)

A utility class for managing timeouts, intervals, and animation frames with context-based organization and automatic cleanup.
Helps prevent memory leaks by organizing timers into named contexts that can be cleared together.

Browser-only: schedules through `window.setTimeout` / `window.setInterval` /
`window.requestAnimationFrame`, so it requires a `window` global. Each schedule
call mutates the instance's internal per-context registries; [dispose](#dispose) and
[disposeAll](#disposeall) cancel and forget them.

## Example

```ts
const timers = new Timers()

// Set timers with context organization
timers.setTimeout('ui', () => console.log('Auto save'), 5000)
timers.setInterval('ui', () => console.log('Refresh'), 1000)
timers.requestAnimationFrame('ui', () => console.log('Render'))

// Clear all timers for a context
timers.dispose('ui')

// Or get context-bound functions
const uiTimers = timers.forContext('ui')
uiTimers.setTimeout(() => console.log('Contextual timeout'), 1000)
```

## Constructors

### Constructor

&gt; **new Timers**(): `Timers`

Defined in: [packages/helpers/src/utils/timers.ts:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/timers.ts#L66)

Creates a new Timers instance with bound methods for safe callback usage.

#### Returns

`Timers`

#### Example

```ts
const timers = new Timers()
// Methods are pre-bound, safe to use as callbacks
element.addEventListener('click', timers.dispose)
```

## Methods

### dispose()

&gt; **dispose**(`contextId`): `void`

Defined in: [packages/helpers/src/utils/timers.ts:162](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/timers.ts#L162)

Disposes of all timers associated with the specified context.
Clears all timeouts, intervals, and animation frames for the given context ID.

#### Parameters

##### contextId

`string`

The context identifier whose timers should be cleared.

#### Returns

`void`

#### Example

```ts
const timers = new Timers()
timers.setTimeout('ui', () => console.log('timeout'), 1000)
timers.setInterval('ui', () => console.log('interval'), 500)

// Clear all 'ui' context timers
timers.dispose('ui')
```

***

### disposeAll()

&gt; **disposeAll**(): `void`

Defined in: [packages/helpers/src/utils/timers.ts:192](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/timers.ts#L192)

Disposes of all timers across all contexts.
Clears every timeout, interval, and animation frame managed by this instance.

Caveat: iteration is driven by the timeout registry's keys, so only contexts
that registered at least one timeout via [setTimeout](#settimeout) are visited. A
context that registered *only* intervals or animation frames (never a
timeout) is not cleared by this method — dispose it explicitly with
[dispose](#dispose).

#### Returns

`void`

#### Example

```ts
const timers = new Timers()
timers.setTimeout('ui', () => console.log('ui'), 1000)
timers.setTimeout('background', () => console.log('bg'), 2000)

// Clear everything
timers.disposeAll()
```

***

### forContext()

&gt; **forContext**(`contextId`): `object`

Defined in: [packages/helpers/src/utils/timers.ts:218](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/timers.ts#L218)

Returns an object with timer methods bound to a specific context.
Convenient for getting context-specific timer functions without repeatedly passing the contextId.

#### Parameters

##### contextId

`string`

The context identifier to bind the returned methods to.

#### Returns

`object`

An object with setTimeout, setInterval, requestAnimationFrame, and dispose methods bound to the context.

##### dispose

&gt; **dispose**: () =&gt; `void`

###### Returns

`void`

##### requestAnimationFrame

&gt; **requestAnimationFrame**: (`callback`) =&gt; `number`

###### Parameters

###### callback

`FrameRequestCallback`

###### Returns

`number`

##### setInterval

&gt; **setInterval**: (`handler`, `timeout?`, ...`args`) =&gt; `number`

###### Parameters

###### handler

`TimerHandler`

###### timeout?

`number`

###### args

...`unknown`[]

###### Returns

`number`

##### setTimeout

&gt; **setTimeout**: (`handler`, `timeout?`, ...`args`) =&gt; `number`

###### Parameters

###### handler

`TimerHandler`

###### timeout?

`number`

###### args

...`unknown`[]

###### Returns

`number`

#### Example

```ts
const timers = new Timers()
const uiTimers = timers.forContext('ui')

// These are equivalent to calling timers.setTimeout('ui', ...)
uiTimers.setTimeout(() => console.log('timeout'), 1000)
uiTimers.setInterval(() => console.log('interval'), 500)
uiTimers.requestAnimationFrame(() => console.log('frame'))

// Dispose only this context
uiTimers.dispose()
```

***

### requestAnimationFrame()

&gt; **requestAnimationFrame**(`contextId`, `callback`): `number`

Defined in: [packages/helpers/src/utils/timers.ts:140](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/timers.ts#L140)

Requests an animation frame that will be tracked under the specified context.

#### Parameters

##### contextId

`string`

The context identifier to group this animation frame under.

##### callback

`FrameRequestCallback`

The function to execute on the next animation frame.

#### Returns

`number`

The request ID that can be used with cancelAnimationFrame.

#### Example

```ts
const timers = new Timers()
const id = timers.requestAnimationFrame('render', () => draw())
// Animation frame will be automatically cancelled when 'render' context is disposed
```

***

### setInterval()

&gt; **setInterval**(`contextId`, `handler`, `timeout?`, ...`args`): `number`

Defined in: [packages/helpers/src/utils/timers.ts:115](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/timers.ts#L115)

Creates an interval that will be tracked under the specified context.

#### Parameters

##### contextId

`string`

The context identifier to group this timer under.

##### handler

`TimerHandler`

The function to execute repeatedly.

##### timeout?

`number`

The delay in milliseconds between executions (default: 0).

##### args

...`unknown`[]

Additional arguments to pass to the handler.

#### Returns

`number`

The interval ID that can be used with clearInterval.

#### Example

```ts
const timers = new Timers()
const id = timers.setInterval('refresh', () => updateData(), 1000)
// Interval will be automatically cleared when 'refresh' context is disposed
```

***

### setTimeout()

&gt; **setTimeout**(`contextId`, `handler`, `timeout?`, ...`args`): `number`

Defined in: [packages/helpers/src/utils/timers.ts:88](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/timers.ts#L88)

Creates a timeout that will be tracked under the specified context.

#### Parameters

##### contextId

`string`

The context identifier to group this timer under.

##### handler

`TimerHandler`

The function to execute when the timeout expires.

##### timeout?

`number`

The delay in milliseconds (default: 0).

##### args

...`unknown`[]

Additional arguments to pass to the handler.

#### Returns

`number`

The timer ID that can be used with clearTimeout.

#### Example

```ts
const timers = new Timers()
const id = timers.setTimeout('autosave', () => save(), 5000)
// Timer will be automatically cleared when 'autosave' context is disposed
```
