# Type Alias: ReportFunction

&gt; **ReportFunction** = (`data`) =&gt; `unknown`

Defined in: [exec-time/exec-time.types.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/exec-time/exec-time.types.ts#L45)

Function type for reporting execution time data.

Invoked once per timed call with the measured [ExactTimeReportData](../interfaces/ExactTimeReportData). Any
returned value is ignored (the signature allows non-`void` only for
convenience), and it runs for its side effect — logging, metrics — after the
method settles.

## Parameters

### data

[`ExactTimeReportData`](../interfaces/ExactTimeReportData)

The execution time report data.

## Returns

`unknown`

Any value (typically `void`); the caller discards it.

## Example

```typescript
const customReporter: ReportFunction = (data) => {
  console.log(`Method took ${data.execTime}ms with args:`, data.args);
  metrics.timing('method.duration', data.execTime);
};
```
