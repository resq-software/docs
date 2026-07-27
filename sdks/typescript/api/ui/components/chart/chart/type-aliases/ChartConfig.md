# Type Alias: ChartConfig

&gt; **ChartConfig** = \{ \[k in string\]: \{ icon?: React.ComponentType; label?: React.ReactNode \} & (\{ color?: never; theme: Record\<keyof typeof THEMES, string\> \} \| \{ color?: string; theme?: never \}) \}

Defined in: [packages/ui/src/components/chart/chart.tsx:67](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/chart/chart.tsx#L67)

Per-series chart configuration, keyed by the data key a Recharts series is
bound to (its `dataKey` or `name`). Each entry carries presentation metadata
for that series plus, at most, one of two mutually-exclusive coloring modes.

The color union is enforced by the type: an entry sets **either** a flat
`color` **or** a per-theme `theme` map (keyed by the `THEMES` names,
`"dark"` | `"light"`), never both — and may set neither, in which case the
series keeps Recharts' own default color. [ChartContainer](../functions/ChartContainer) reads this
map to emit the `--color-<key>` CSS variable each series pulls from; a key or
color that fails the container's allowlist is silently skipped rather than
emitted.
