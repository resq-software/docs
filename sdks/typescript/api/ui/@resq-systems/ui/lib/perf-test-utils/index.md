# @resq-systems/ui/lib/perf-test-utils

## Fileoverview

Shared utilities for component performance regression tests,
covering all six Storybook Performance plugin categories plus Element Timing
instrumentation checks.

Categories:
  1. Frame Timing        — transition-all, heavy animations, will-change abuse
  2. Layout & Stability  — CLS contributors, forced reflows, style writes
  3. React Performance   — re-render guards, memo boundaries, key hygiene
  4. DOM Nodes           — tree size, nesting depth
  5. Style Writes        — inline styles, dynamic className churn
  6. Input Responsiveness — passive listeners, debounce patterns

## Interfaces

- [PerfBudget](./interfaces/PerfBudget)
- [PerfViolation](./interfaces/PerfViolation)
- [ReactLikeElement](./interfaces/ReactLikeElement)

## Variables

- [DIV\_ONCLICK\_RE](./variables/DIV_ONCLICK_RE)
- [ICON\_BUTTON\_NO\_LABEL\_RE](./variables/ICON_BUTTON_NO_LABEL_RE)

## Functions

- [assertClassNameMerging](./functions/assertClassNameMerging)
- [assertFontCompliance](./functions/assertFontCompliance)
- [assertHasDataSlot](./functions/assertHasDataSlot)
- [assertInteractiveHasFocusVisible](./functions/assertInteractiveHasFocusVisible)
- [assertNoForcedReflowTriggers](./functions/assertNoForcedReflowTriggers)
- [assertNoGenericRadius](./functions/assertNoGenericRadius)
- [assertNoLayoutTransitions](./functions/assertNoLayoutTransitions)
- [assertNoRawHexInClassNames](./functions/assertNoRawHexInClassNames)
- [assertNoTransitionAll](./functions/assertNoTransitionAll)
- [assertReducedMotion](./functions/assertReducedMotion)
- [assertRenderedNoGenericRadius](./functions/assertRenderedNoGenericRadius)
- [assertRenderedNoTransitionAll](./functions/assertRenderedNoTransitionAll)
- [assertSSRSafe](./functions/assertSSRSafe)
- [collectClassNames](./functions/collectClassNames)
- [collectRenderedViolations](./functions/collectRenderedViolations)
- [collectSourceViolations](./functions/collectSourceViolations)
- [collectUnsizedMedia](./functions/collectUnsizedMedia)
- [countElementNodes](./functions/countElementNodes)
- [countInlineStyles](./functions/countInlineStyles)
- [formatViolationReport](./functions/formatViolationReport)
- [groupByCategory](./functions/groupByCategory)
- [hasBlockingViolations](./functions/hasBlockingViolations)
- [measureNestingDepth](./functions/measureNestingDepth)
