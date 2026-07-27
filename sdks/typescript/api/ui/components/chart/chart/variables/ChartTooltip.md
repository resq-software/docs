# Variable: ChartTooltip

&gt; `const` **ChartTooltip**: (`outsideProps`) =&gt; `Element` \| `null` = `RechartsPrimitive.Tooltip`

Defined in: [packages/ui/src/components/chart/chart.tsx:204](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/chart/chart.tsx#L204)

Recharts `Tooltip` re-export; render [ChartTooltipContent](../functions/ChartTooltipContent) as its content.

The Tooltip component displays a floating box with data values when hovering over or clicking on chart elements.

It can be configured to show information for individual data points or for all points at a specific axis coordinate.
The appearance and content of the tooltip can be customized via props.

## Parameters

### outsideProps

`TooltipProps`\<`ValueType`, `NameType`\>

## Returns

`Element` \| `null`

## See

 - [Tooltip event type and shared prop wiki page](https://github.com/recharts/recharts/wiki/Tooltip-event-type-and-shared-prop)
 - [Active index replacement when migrating from Recharts v2 to v3](https://recharts.github.io/en-US/guide/activeIndex/)

## Consumes

CartesianChartContext

## Consumes

PolarChartContext

## Consumes

TooltipEntrySettings
