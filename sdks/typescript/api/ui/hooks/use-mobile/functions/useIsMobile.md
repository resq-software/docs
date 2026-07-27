# Function: useIsMobile()

&gt; **useIsMobile**(): `boolean`

Defined in: [packages/ui/src/hooks/use-mobile.ts:49](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/hooks/use-mobile.ts#L49)

Subscribe to a `(max-width: 767px)` `matchMedia` query and return
whether the viewport is currently in the mobile range.

SSR-safe: returns `false` during the first render (before
`useEffect` runs), then re-renders with the real value once the
subscription is active.

Cleanup is automatic — the listener is removed on unmount or on
route changes.

## Returns

`boolean`

`true` when the viewport is &lt; 768 CSS pixels wide.

## Example

```tsx
const isMobile = useIsMobile();
return isMobile ? <Drawer /> : <Sidebar />;
```
