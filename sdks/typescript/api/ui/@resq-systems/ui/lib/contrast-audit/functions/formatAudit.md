# Function: formatAudit()

&gt; **formatAudit**(`audit`): `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:548](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L548)

Render a [ThemeAudit](../interfaces/ThemeAudit) as a multi-line plain-text report
suitable for CLI output, CI logs, or vitest assertion messages.

## Parameters

### audit

[`ThemeAudit`](../interfaces/ThemeAudit)

## Returns

`string`

## Example

**output**

```
DARK MODE:
  PASS 12.45:1 (min 4.5) | foreground on background
  FAIL  3.20:1 (min 4.5) | muted-foreground on surface
```
