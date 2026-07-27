# Function: SidebarMenuSkeleton()

&gt; **SidebarMenuSkeleton**(`showIcon`): `Element`

Defined in: [packages/ui/src/components/sidebar/sidebar.tsx:662](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/sidebar/sidebar.tsx#L662)

Loading placeholder for a menu item. Its text bar takes a random width
(50–90%) chosen once per mount via `Math.random`, so successive renders and
snapshots are non-deterministic by design.

## Parameters

### showIcon

`Readonly`\<`React.ComponentProps`\<`"div"`\> & `object`\>

Also render a square icon placeholder before the text bar.

## Returns

`Element`
