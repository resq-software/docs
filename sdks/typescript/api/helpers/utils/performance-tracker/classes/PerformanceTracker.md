# Class: PerformanceTracker

Defined in: [packages/helpers/src/utils/performance-tracker.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/performance-tracker.ts#L51)

A utility class for measuring and tracking frame rate performance during operations.
Provides visual feedback in the browser console with color-coded FPS indicators.

Requires a browser-like environment: relies on `requestAnimationFrame`,
`cancelAnimationFrame`, and `performance.now()`. Not concurrency-safe within one
instance — [start](#start) resets counters, so overlapping start/stop pairs on the
same tracker measure only the most recent run.

## Example

```ts
const tracker = new PerformanceTracker()

tracker.start('render')
renderShapes()
tracker.stop() // Logs performance info to console

// Check if tracking is active
if (tracker.isStarted()) {
  console.log('Still tracking performance')
}
```

## Constructors

### Constructor

&gt; **new PerformanceTracker**(): `PerformanceTracker`

#### Returns

`PerformanceTracker`

## Methods

### isStarted()

&gt; **isStarted**(): `boolean`

Defined in: [packages/helpers/src/utils/performance-tracker.ts:150](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/performance-tracker.ts#L150)

Checks whether performance tracking is currently active.

#### Returns

`boolean`

True if tracking is in progress, false otherwise

#### Example

```ts
if (!tracker.isStarted()) {
  tracker.start('new-operation')
}
```

***

### recordFrame()

&gt; **recordFrame**(): `void`

Defined in: [packages/helpers/src/utils/performance-tracker.ts:63](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/performance-tracker.ts#L63)

Records animation frames to calculate frame rate.
Called automatically during performance tracking.

#### Returns

`void`

***

### start()

&gt; **start**(`name`): `void`

Defined in: [packages/helpers/src/utils/performance-tracker.ts:82](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/performance-tracker.ts#L82)

Starts performance tracking for a named operation.

#### Parameters

##### name

`string`

A descriptive name for the operation being tracked

#### Returns

`void`

#### Example

```ts
tracker.start('canvas-render')
// ... perform rendering operations
tracker.stop()
```

***

### stop()

&gt; **stop**(): `void`

Defined in: [packages/helpers/src/utils/performance-tracker.ts:115](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/performance-tracker.ts#L115)

Stops performance tracking and logs results to the console.

Displays the operation name, frame rate, and uses color coding:
- Green background: \> 55 FPS (good performance)
- Yellow background: 30-55 FPS (moderate performance)
- Red background: \< 30 FPS (poor performance)

Side effect: writes one styled line to the console (`console.debug`) and
cancels the pending animation frame. Must be preceded by a [start](#start)
call.

#### Returns

`void`

#### Throws

If called before [start](#start) — the operation name is
  still the empty string, so capitalising its first character dereferences
  `undefined`.

#### Example

```ts
tracker.start('interaction')
handleUserInteraction()
tracker.stop() // Logs: "Perf Interaction 60 fps"
```
