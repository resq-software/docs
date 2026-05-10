# Interface: ExactTimeReportData

Defined in: [exec-time/exec-time.types.ts:50](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/exec-time/exec-time.types.ts#L50)

Data structure containing execution time information.

 ExactTimeReportData

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

> **args**: `unknown`[]

Defined in: [exec-time/exec-time.types.ts:52](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/exec-time/exec-time.types.ts#L52)

The arguments passed to the method

***

### execTime

> **execTime**: `number`

Defined in: [exec-time/exec-time.types.ts:56](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/exec-time/exec-time.types.ts#L56)

The execution time in milliseconds

***

### result

> **result**: `unknown`

Defined in: [exec-time/exec-time.types.ts:54](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/exec-time/exec-time.types.ts#L54)

The return value of the method
