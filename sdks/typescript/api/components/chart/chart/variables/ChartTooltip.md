# Variable: ChartTooltip

> `const` **ChartTooltip**: (`outsideProps`) => `Element` \| `null` = `RechartsPrimitive.Tooltip`

Defined in: [packages/ui/src/components/chart/chart.tsx:138](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/components/chart/chart.tsx#L138)

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
