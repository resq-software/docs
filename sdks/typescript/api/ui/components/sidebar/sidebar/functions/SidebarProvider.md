# Function: SidebarProvider()

&gt; **SidebarProvider**(`defaultOpen`): `Element`

Defined in: [packages/ui/src/components/sidebar/sidebar.tsx:350](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/sidebar/sidebar.tsx#L350)

Root provider for the sidebar family — owns open/collapsed state and exposes
it via [useSidebar](./useSidebar). Supports both controlled (`open` + `onOpenChange`)
and uncontrolled (`defaultOpen`) usage.

Effects: every open-state change writes the `sidebar_state` cookie
(`document.cookie`, one-week max-age) so the state survives reloads, and while
mounted it registers a global `keydown` listener that toggles the sidebar on
⌘B / Ctrl+B (removed on unmount).

## Parameters

### defaultOpen

`Readonly`\<`React.ComponentProps`\<`"div"`\> & `object`\>

Initial open state when uncontrolled. Defaults to `true`.

## Returns

`Element`
