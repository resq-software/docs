# Function: evaluate()

&gt; **evaluate**(`expr`, `env?`, `stack?`, `options?`): [`Value`](../../value/type-aliases/Value)

Defined in: [packages/math/src/evaluate.ts:97](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/evaluate.ts#L97)

Evaluate a compiled expression to a concrete [Value](../../value/type-aliases/Value).

## Parameters

### expr

[`CompiledExpr`](../../ast/type-aliases/CompiledExpr)

The compiled expression to evaluate.

### env?

[`Env`](../type-aliases/Env) = `...`

Global free variables. Defaults to empty.

### stack?

readonly [`Value`](../../value/type-aliases/Value)[] = `[]`

The stack of active bound lexical variables (top at the end).

### options?

[`EvaluateOptions`](../interfaces/EvaluateOptions)

Configure step and depth limits to prevent DoS.

## Returns

[`Value`](../../value/type-aliases/Value)

The computed value.

Pure with respect to its arguments: `stack` is copied before use and `env` is
only read, so neither is mutated. Results do, however, depend on the shared
operator registry — a prior registerBinary (or sibling) call can change
what this returns for the same inputs. Failure is always a thrown `Error`
subclass, never a resolved error value.

## Throws

If a `free_var` is absent from `env`.

## Throws

If a `bound_var` index falls outside the live stack — a sign of a malformed compiled tree.

## Throws

If an operand has the wrong sort: a binder `domain` that is not a `set`, or a binder body of the wrong sort (`∑`/`∏` need `num`, `∀`/`∃` need `bool`), a non-`func` in a call position, or a non-`record` in a member access.

## Throws

If no operator instance is registered for the operand sorts.

## Throws

If an operation is sort-valid but mathematically invalid (division/modulo by zero, `√` of a negative, factorial out of range, or a missing record property).

## Throws

If the evaluated-step count exceeds `maxSteps`.

## Throws

If recursion depth exceeds `maxDepth`.
