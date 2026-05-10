# Type Alias: ReportFunction

> **ReportFunction** = (`data`) => `unknown`

Defined in: [exec-time/exec-time.types.ts:31](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/exec-time/exec-time.types.ts#L31)

Function type for reporting execution time data.

## Parameters

### data

[`ExactTimeReportData`](../interfaces/ExactTimeReportData.md)

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
