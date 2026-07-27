# Function: cn()

&gt; **cn**(...`inputs`): `string`

Defined in: [packages/ui/src/lib/utils.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/utils.ts#L38)

Compose Tailwind class names with intelligent conflict resolution.

Pipes `inputs` through `clsx` (handles arrays, objects, and
conditional values) and then `tailwind-merge` (deduplicates
conflicting Tailwind utilities, e.g. `px-2 px-4` → `px-4`). This
is the canonical class-name combiner used by every component in
`@resq-systems/ui` and is exported so consumers can match the same
conventions in their own components.

## Parameters

### inputs

...`ClassValue`[]

Any combination of strings, arrays, objects, or
  conditional values supported by `clsx`.

## Returns

`string`

A merged, conflict-free Tailwind class string.

## Example

```ts
cn("px-2", "px-4");                                   // "px-4"
cn("text-foreground", isError && "text-destructive"); // last truthy wins
cn("rounded", { "ring-2": focused });
cn(baseClasses, variant && variantClasses, className);
```
