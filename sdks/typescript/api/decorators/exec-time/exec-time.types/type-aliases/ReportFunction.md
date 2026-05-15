# Type Alias: ReportFunction

> **ReportFunction** = (`data`) => `unknown`

Defined in: [exec-time/exec-time.types.ts:31](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/exec-time/exec-time.types.ts#L31)

Function type for reporting execution time data.

## Parameters

### data

[`ExactTimeReportData`](../interfaces/ExactTimeReportData)

The execution time report data

## Returns

`unknown`

Can return any value (typically void)

## Example

```typescript
const customReporter: ReportFunction = (data) => {
  console.log(`Method took ${data.execTime}ms with args:`, data.args);
  metrics.timing('method.duration', data.execTime);
};
```
