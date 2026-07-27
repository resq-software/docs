# @resq-systems/ui/lib/contrast-audit

## Fileoverview

Multi-format WCAG contrast-ratio checker supporting hex, rgb(),
hsl(), oklch(), oklab(), lab(), lch(), and CSS named colors. Used by
contrast-audit.test.ts to keep every design-token pair compliant.

## Interfaces

- [ContrastPair](./interfaces/ContrastPair)
- [ContrastResult](./interfaces/ContrastResult)
- [LinearRGB](./interfaces/LinearRGB)
- [ThemeAudit](./interfaces/ThemeAudit)

## Type Aliases

- [ColorTokens](./type-aliases/ColorTokens)

## Variables

- [DEFAULT\_PAIRS](./variables/DEFAULT_PAIRS)

## Functions

- [auditTheme](./functions/auditTheme)
- [contrastRatio](./functions/contrastRatio)
- [extractTokensFromCSS](./functions/extractTokensFromCSS)
- [formatAudit](./functions/formatAudit)
- [relativeLuminance](./functions/relativeLuminance)
- [runContrastAudit](./functions/runContrastAudit)
- [toLinearRGB](./functions/toLinearRGB)
