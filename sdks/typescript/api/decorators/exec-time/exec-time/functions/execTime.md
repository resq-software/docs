# Function: execTime()

&gt; **execTime**\<`T`\>(`arg?`): [`ExactTimeReportable`](../../exec-time.types/type-aliases/ExactTimeReportable)\<`T`\>

Defined in: [exec-time/exec-time.ts:86](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/exec-time/exec-time.ts#L86)

Decorator that measures and reports the execution time of methods.
Supports both legacy (TypeScript) and standard (Stage 3) decorator formats.

Detects the protocol at decoration time: given a descriptor it rewrites
`descriptor.value` (legacy form); otherwise it treats the arguments as the
Stage-3 `(value, context)` pair and returns the wrapped method for a `method`
kind. See [execTimeFn](../../exec-time.fn/functions/execTimeFn) for the timing, async, and reporter-resolution
contract (including that rejected async methods are not reported).

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method.

## Parameters

### arg?

`string` \| [`ReportFunction`](../../exec-time.types/type-aliases/ReportFunction)

Optional reporter function or label string.

## Returns

[`ExactTimeReportable`](../../exec-time.types/type-aliases/ExactTimeReportable)\<`T`\>

The decorator function.

## Throws

At decoration time, with message
  `"@execTime is applicable only on methods."`, when the legacy descriptor has
  no method value or the Stage-3 context's `kind` is not `"method"`.

## Example

```typescript
class PerformanceMonitor {
  // Uses default console reporter
  @execTime()
  processData(data: any[]): void {
    // Processing...
  }

  // Uses custom label
  @execTime('Database Query')
  async fetchUsers(): Promise<User[]> {
    return db.users.findAll();
  }

  // Uses custom reporter function
  @execTime((data) => {
    metrics.histogram('method_duration', data.execTime);
    console.log(`${data.execTime}ms: ${data.args.join(', ')}`);
  })
  heavyCalculation(input: number): number {
    return input ** 2;
  }
}
```
