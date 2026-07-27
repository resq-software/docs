# Type Alias: ReportFunction

&gt; **ReportFunction** = (`data`) =&gt; `unknown`

Defined in: [exec-time/exec-time.types.ts:45](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/exec-time/exec-time.types.ts#L45)

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
