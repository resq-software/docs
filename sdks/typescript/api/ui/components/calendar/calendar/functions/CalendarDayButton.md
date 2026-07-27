# Function: CalendarDayButton()

&gt; **CalendarDayButton**(`__namedParameters`): `Element`

Defined in: [packages/ui/src/components/calendar/calendar.tsx:189](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/calendar/calendar.tsx#L189)

Renders one day cell as a button, reflecting today/selected/range-edge states.

Moves DOM focus to its own button whenever react-day-picker marks the day as
`modifiers.focused`, keeping keyboard navigation in sync with the rendered
grid.

## Parameters

### \_\_namedParameters

`Readonly`\<`React.ComponentProps`\<*typeof* `DayButton`\> & `object`\>

## Returns

`Element`
