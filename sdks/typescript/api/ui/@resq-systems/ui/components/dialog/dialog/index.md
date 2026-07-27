# @resq-systems/ui/components/dialog/dialog

## Fileoverview

Dialog component family — modal overlay built on
Radix UI's `Dialog` primitive. Use for content-bearing modals
(forms, detail views, confirmations); use `AlertDialog` instead
for destructive action gates.

Composition: `Dialog > DialogTrigger + DialogContent`, with
`DialogHeader > (DialogTitle + DialogDescription)`,
`DialogFooter`, and an auto-rendered close button using the
shared `Button` component.

Per `STYLE_GUIDE.md`, `DialogTitle` renders `font-display`.

Accessibility: focus trap, escape-to-close, scroll-lock, and
`aria-labelledby` / `aria-describedby` wiring all handled by Radix.

## Functions

- [Dialog](./functions/Dialog)
- [DialogClose](./functions/DialogClose)
- [DialogContent](./functions/DialogContent)
- [DialogDescription](./functions/DialogDescription)
- [DialogFooter](./functions/DialogFooter)
- [DialogHeader](./functions/DialogHeader)
- [DialogOverlay](./functions/DialogOverlay)
- [DialogPortal](./functions/DialogPortal)
- [DialogTitle](./functions/DialogTitle)
- [DialogTrigger](./functions/DialogTrigger)
