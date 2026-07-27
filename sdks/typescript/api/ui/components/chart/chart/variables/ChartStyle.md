# Variable: ChartStyle

&gt; `const` **ChartStyle**: `MemoExoticComponent`\<(`__namedParameters`) =&gt; `Element` \| `null`\>

Defined in: [packages/ui/src/components/chart/chart.tsx:177](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/chart/chart.tsx#L177)

Injects a scoped `<style>` tag defining each series' color CSS variables;
auto-rendered by [ChartContainer](../functions/ChartContainer).

Renders nothing (returns `null`) when no config entry defines a `color` or
`theme`. The emitted CSS is assembled only from keys and colors that pass the
`SAFE_KEY_RE` / `SAFE_COLOR_RE` allowlists, which is why the
`dangerouslySetInnerHTML` here is safe.
