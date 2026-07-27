# Class: FpsScheduler

Defined in: [packages/helpers/src/utils/throttle.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/throttle.ts#L51)

A scheduler class that manages a queue of functions to be executed at a target frame rate.
Each instance maintains its own queue and state, allowing for separate throttling contexts
(e.g., UI operations vs network sync operations).

Relies on `requestAnimationFrame`/`cancelAnimationFrame` and `Date.now()`, so it
only throttles in a browser-like environment. When `NODE_ENV === "test"` (and
`globalThis.__FORCE_RAF_IN_TESTS__` is unset) the frame machinery is bypassed
so callbacks fire eagerly and synchronously — see the individual methods.
Callback identity is the dedupe key: the same function reference queued twice
before a flush runs only once.

## Constructors

### Constructor

&gt; **new FpsScheduler**(`targetFps?`): `FpsScheduler`

Defined in: [packages/helpers/src/utils/throttle.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/throttle.ts#L59)

#### Parameters

##### targetFps?

`number` = `120`

#### Returns

`FpsScheduler`

## Methods

### fpsThrottle()

&gt; **fpsThrottle**(`fn`): \{(): `void`; `cancel?`: `void`; \}

Defined in: [packages/helpers/src/utils/throttle.ts:127](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/throttle.ts#L127)

Creates a throttled version of a function that executes at most once per frame.
The default target frame rate is set by the FpsScheduler instance.
Subsequent calls within the same frame are ignored, ensuring smooth performance
for high-frequency events like mouse movements or scroll events.

In a test environment the original `fn` is returned unchanged (invoking it runs
`fn` immediately, with no throttling); its attached `cancel` clears any pending
scheduler frames.

#### Parameters

##### fn

\{(): `void`; `cancel?`: `void`; \}

The function to throttle, optionally with a cancel method

###### cancel?

#### Returns

A throttled function with an optional cancel method to remove pending calls

\{(): `void`; `cancel?`: `void`; \}

##### cancel()?

&gt; `optional` **cancel**(): `void`

###### Returns

`void`

***

### throttleToNextFrame()

&gt; **throttleToNextFrame**(`fn`): () =&gt; `void`

Defined in: [packages/helpers/src/utils/throttle.ts:174](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/throttle.ts#L174)

Schedules a function to execute on the next animation frame.
If the same function is passed multiple times before the frame executes,
it will only be called once, effectively batching multiple calls.

In a test environment `fn` runs synchronously before returning and the
returned cancel is a no-op (there is nothing pending to cancel).

#### Parameters

##### fn

() =&gt; `void`

The function to execute on the next frame

#### Returns

A cancel function that can prevent execution if called before the next frame

() =&gt; `void`

***

### updateTargetFps()

&gt; **updateTargetFps**(`targetFps`): `void`

Defined in: [packages/helpers/src/utils/throttle.ts:65](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/throttle.ts#L65)

#### Parameters

##### targetFps

`number`

#### Returns

`void`
