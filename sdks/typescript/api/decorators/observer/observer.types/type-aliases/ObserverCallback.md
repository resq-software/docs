# Type Alias: ObserverCallback\<T\>

&gt; **ObserverCallback**\<`T`\> = (`value`) =&gt; `unknown`

Defined in: [observer/observer.types.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/observer/observer.types.ts#L44)

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
