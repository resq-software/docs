# Function: SidebarMenuButton()

&gt; **SidebarMenuButton**(`tooltip`): `Element`

Defined in: [packages/ui/src/components/sidebar/sidebar.tsx:602](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/sidebar/sidebar.tsx#L602)

Primary nav-item button. Must render under a [SidebarProvider](./SidebarProvider) — it
reads state via [useSidebar](./useSidebar), which throws otherwise.

## Parameters

### tooltip

`Readonly`\<`React.ComponentProps`\<`"button"`\> & `VariantProps`\<*typeof* `sidebarMenuButtonVariants`\> & `object`\>

When set, wraps the button in a tooltip that is shown *only*
  while the sidebar is collapsed on desktop. A `string` is treated as the
  tooltip label; an object is spread onto the underlying `TooltipContent`.

## Returns

`Element`
