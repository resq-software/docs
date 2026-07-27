# Function: useSidebar()

&gt; **useSidebar**(): `SidebarContextProps`

Defined in: [packages/ui/src/components/sidebar/sidebar.tsx:520](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/sidebar/sidebar.tsx#L520)

Read the sidebar's open/collapsed state and toggles from context.

## Returns

`SidebarContextProps`

The active SidebarContextProps — `open`/`state`, the mobile
  flag, and the `setOpen`/`toggleSidebar` actions.

## Throws

When called outside a [SidebarProvider](./SidebarProvider) (the context is
  `null`). Render the component tree under a provider to satisfy this.
