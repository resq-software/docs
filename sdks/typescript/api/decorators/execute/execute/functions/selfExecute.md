# Function: selfExecute()

&gt; **selfExecute**\<`T`\>(`constructor`): `T`

Defined in: [execute/execute.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/execute/execute.ts#L83)

Class decorator that automatically instantiates the class when decorated.
Creates an instance immediately and returns the constructor.

The instantiation is a **side effect that runs at decoration time** — i.e. as
the class's module is evaluated — so the constructor's effects (registering
listeners, singleton wiring, telemetry init) fire on import. The created
instance is discarded, not returned or retained here; only what the
constructor does persists (e.g. a static singleton it stores on itself). The
constructor is returned **unchanged**, so the class's own type is preserved.
Anything the constructor throws propagates out of module evaluation.

## Type Parameters

### T

`T` *extends* (...`args`) =&gt; `object`

The class constructor type; the `new (...args: never[]) => object`
  bound requires a constructor callable with no required arguments.

## Parameters

### constructor

`T`

The class constructor.

## Returns

`T`

The constructor (with the instance created as a side effect).

## Throws

Whatever `constructor` throws, at decoration/module-load time.

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
