# @resq-systems/ui/components/alert-dialog/alert-dialog

## Fileoverview

AlertDialog component family — modal confirmation
dialog built on Radix UI's `AlertDialog` primitive. Use this (rather
than `Dialog`) for irreversible, destructive, or otherwise
blocking confirmations. The cancel/action buttons reuse the
shared `Button` component for consistent styling.

Composition: `AlertDialog > AlertDialogTrigger + AlertDialogContent`,
with `AlertDialogContent` wrapping `AlertDialogHeader`
(`AlertDialogTitle` + `AlertDialogDescription`) and
`AlertDialogFooter` (`AlertDialogCancel` + `AlertDialogAction`).

Accessibility: focus trap, escape-to-close, and inert background
via Radix. Title and description are wired through `aria-labelledby`
/ `aria-describedby` automatically.

## Functions

- [AlertDialog](./functions/AlertDialog)
- [AlertDialogAction](./functions/AlertDialogAction)
- [AlertDialogCancel](./functions/AlertDialogCancel)
- [AlertDialogContent](./functions/AlertDialogContent)
- [AlertDialogDescription](./functions/AlertDialogDescription)
- [AlertDialogFooter](./functions/AlertDialogFooter)
- [AlertDialogHeader](./functions/AlertDialogHeader)
- [AlertDialogMedia](./functions/AlertDialogMedia)
- [AlertDialogOverlay](./functions/AlertDialogOverlay)
- [AlertDialogPortal](./functions/AlertDialogPortal)
- [AlertDialogTitle](./functions/AlertDialogTitle)
- [AlertDialogTrigger](./functions/AlertDialogTrigger)
