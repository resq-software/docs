# Function: observe()

Overloaded function for observing property changes.
Can be used with or without a custom callback.

## Param

Either the class prototype or a callback function

## Param

The property key (when used without callback)

## Throws

When used with incorrect parameters

## Call Signature

> **observe**(`target`, `propertyKey`): `void`

Defined in: [observer/observer.ts:93](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/observer/observer.ts#L93)

Observe all changes of a property. All assignments will be logged to the console.

### Parameters

#### target

`object`

The class prototype

#### propertyKey

`string` \| `symbol`

The property key

### Returns

`void`

### Example

```typescript
class Counter {
  @observe
  value: number = 0;
}

const counter = new Counter();
counter.value = 5; // Logs: "setting property Counter#value = 5"
counter.value = 10; // Logs: "setting property Counter#value = 10"
```

## Call Signature

> **observe**\<`T`\>(`cb`): `PropertyDecorator`

Defined in: [observer/observer.ts:122](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/observer/observer.ts#L122)

Observe all changes of a property and invoke a provided callback on each assignment.

### Type Parameters

#### T

`T`

The type of the property value

### Parameters

#### cb

[`ObserverCallback`](../../observer.types/type-aliases/ObserverCallback)\<`T`\>

Callback to execute on assignment of observed variable

### Returns

`PropertyDecorator`

The property decorator

### Example

```typescript
class User {
  @observe((value) => {
    console.log('Email changed:', value);
    validateEmail(value);
  })
  email: string = '';

  @observe((value) => {
    metrics.gauge('user.age', value);
  })
  age: number = 0;
}

const user = new User();
user.email = 'test@example.com'; // Logs and validates
user.age = 25; // Records metric
```
