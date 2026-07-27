# Type Alias: ObserverCallback\<T\>

&gt; **ObserverCallback**\<`T`\> = (`value`) =&gt; `unknown`

Defined in: [observer/observer.types.ts:44](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/observer/observer.types.ts#L44)

Callback invoked whenever an observed property is assigned a new value. Any
return value is ignored.

## Type Parameters

### T

`T`

The type of the property value.

## Parameters

### value

`T`

The newly assigned value.

## Returns

`unknown`

Any value; the return is ignored.

## Example

```ts
const onCountChange: ObserverCallback<number> = (newValue) => {
  console.log(`Count is now: ${newValue}`);
};

const onNameChange: ObserverCallback<string> = (newValue) => {
  if (newValue.length < 3) {
    console.warn("Name is too short!");
  }
};
```
