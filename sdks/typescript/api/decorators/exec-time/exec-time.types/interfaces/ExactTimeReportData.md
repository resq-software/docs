# Interface: ExactTimeReportData

Defined in: [exec-time/exec-time.types.ts:63](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/exec-time/exec-time.types.ts#L63)

Data structure containing execution time information.

A snapshot handed to a [ReportFunction](../type-aliases/ReportFunction) after one invocation. For an
async method the report is taken after the promise resolves, so [result](#result)
is the fulfilled value and [execTime](#exectime) spans until resolution.

## Example

```typescript
const reportData: ExactTimeReportData = {
  args: [42, 'test'],
  result: 'success',
  execTime: 150
};
```

## Properties

### args

&gt; **args**: `unknown`[]

Defined in: [exec-time/exec-time.types.ts:65](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/exec-time/exec-time.types.ts#L65)

The exact positional arguments the timed method was called with.

***

### execTime

&gt; **execTime**: `number`

Defined in: [exec-time/exec-time.types.ts:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/exec-time/exec-time.types.ts#L72)

Elapsed wall-clock time in **milliseconds** (`Date.now` deltas, integer ms
resolution), measured from just before the call to just after it settles.

***

### result

&gt; **result**: `unknown`

Defined in: [exec-time/exec-time.types.ts:67](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/exec-time/exec-time.types.ts#L67)

The method's return value — the resolved value for an async method.
