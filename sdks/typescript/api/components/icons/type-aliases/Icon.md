# Type Alias: Icon

> **Icon** = `React.ForwardRefExoticComponent`\<[`IconProps`](../interfaces/IconProps.md)\>

Defined in: node\_modules/@phosphor-icons/react/dist/lib/types.d.ts:10

ResQ icon system — powered by @phosphor-icons/react.

All icons follow the Phosphor naming convention (`*Icon` suffix).
The `weight` prop controls stroke weight: "thin" | "light" | "regular" | "bold" | "fill" | "duotone".
Default weight is "light" (matches the ResQ design system baseline).

Re-exported types:
- `Icon`       — the base ForwardRefExoticComponent type for all icons
- `IconProps`  — props accepted by every icon (weight, size, color, className, …)
- `IconWeight` — the union of allowed weight strings

Server Components: import from `@resq-sw/ui/icons/ssr` instead to avoid
the React.createContext call at module-init time.
