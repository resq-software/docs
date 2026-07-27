# Function: assertHasDataSlot()

&gt; **assertHasDataSlot**(`element`, `componentName`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:539](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L539)

Throw when the rendered React element is missing a `data-slot`
attribute. The design system uses `data-slot` as the stable hook
for Performance API Element Timing instrumentation; without it,
field RUM can't time the component.

## Parameters

### element

`unknown`

### componentName

`string`

## Returns

`void`

## Throws

When `element` is not a React-like element or its root has
  no `data-slot` prop.
