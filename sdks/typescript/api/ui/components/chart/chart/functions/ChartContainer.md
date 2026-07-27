# Function: ChartContainer()

&gt; **ChartContainer**(`__namedParameters`): `Element`

Defined in: [packages/ui/src/components/chart/chart.tsx:125](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/chart/chart.tsx#L125)

Wraps a Recharts `ResponsiveContainer` and emits scoped CSS variables from the
`config` map so each series pulls its color from the design system.

Provides `config` on context for descendant [ChartTooltipContent](./ChartTooltipContent) /
[ChartLegendContent](./ChartLegendContent), and renders a scoped `<style>` element (via
[ChartStyle](../variables/ChartStyle)) holding the `--color-<key>` variables — built only from
allowlist-validated keys and colors, so a malicious `config` value cannot
inject arbitrary CSS.

## Parameters

### \_\_namedParameters

`Readonly`\<`React.ComponentProps`\<`"div"`\> & `object`\>

## Returns

`Element`

## See

[ChartStyle](../variables/ChartStyle)
