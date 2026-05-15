# Function: execTime()

> **execTime**\<`T`\>(`arg?`): `any`

Defined in: [exec-time/exec-time.ts:81](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/exec-time/exec-time.ts#L81)

Decorator that measures and reports the execution time of methods.
Supports both legacy (TypeScript) and standard (Stage 3) decorator formats.

## Type Parameters

### T

`T` = `any`

## Parameters

### arg?

`string` \| [`ReportFunction`](../../exec-time.types/type-aliases/ReportFunction)

Optional reporter function or label string

## Returns

`any`

The decorator function

## Throws

When applied to a non-method property

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
