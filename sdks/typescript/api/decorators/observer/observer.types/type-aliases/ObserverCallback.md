# Type Alias: ObserverCallback\<T\>

> **ObserverCallback**\<`T`\> = (`value`) => `unknown`

Defined in: [observer/observer.types.ts:38](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/observer/observer.types.ts#L38)

Callback function type for property observers.
Called whenever the observed property value changes.

## Type Parameters

### T

`T`

The type of the property value

## Parameters

### value

`T`

The new value of the property

## Returns

`unknown`

Can return any value (typically void)

## Example

```typescript
const onCountChange: ObserverCallback<number> = (newValue) => {
  console.log(`Count is now: ${newValue}`);
};

const onNameChange: ObserverCallback<string> = (newValue) => {
  if (newValue.length < 3) {
    console.warn('Name is too short!');
  }
};
```
