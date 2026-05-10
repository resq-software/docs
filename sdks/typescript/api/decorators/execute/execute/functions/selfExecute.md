# Function: selfExecute()

> **selfExecute**\<`T`\>(`constructor`): `T`

Defined in: [execute/execute.ts:76](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/execute/execute.ts#L76)

Class decorator that automatically instantiates the class when decorated.
Creates an instance immediately and returns the constructor.

## Type Parameters

### T

`T` *extends* (...`args`) => `object`

The type of the class constructor

## Parameters

### constructor

`T`

The class constructor

## Returns

`T`

The constructor (with instance created as side effect)

## Example

```typescript
@selfExecute
class AutoStartService {
  private timer: NodeJS.Timeout;

  constructor() {
    console.log('Service auto-started');
    this.timer = setInterval(() => this.tick(), 1000);
  }

  tick(): void {
    console.log('Tick');
  }
}

// Service is already running when this module loads
```
