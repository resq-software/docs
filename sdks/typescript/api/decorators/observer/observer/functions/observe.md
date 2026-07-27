# Function: observe()

Implementation for the observe overloads: usable directly as a
decorator or as a decorator factory that takes a custom callback.

## Template

**T**

The type of the property value.

## Param

**targetOrCb**

Either the class prototype (direct decorator use) or a
callback function (factory use).

## Param

**propertyKey**

The property key, present only for direct decorator use.

## Throws

If called with an unsupported argument combination.

## Call Signature

&gt; **observe**(`target`, `propertyKey`): `void`

Defined in: [observer/observer.ts:82](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/observer/observer.ts#L82)

Observe every assignment to a property, logging each new value to the console.

Redefines the property on `target` (the prototype) with a getter/setter pair via
`Object.defineProperty`, and writes to `console.log` on every assignment. The
backing value is held in a single closure shared by the prototype, so all
instances read and write the same slot rather than getting per-instance storage.

### Parameters

#### target

`object`

The class prototype.

#### propertyKey

`string` \| `symbol`

The property key.

### Returns

`void`

### Example

```ts
class Counter {
  @observe
  value: number = 0;
}

const counter = new Counter();
counter.value = 5; // Logs: "setting property Counter#value = 5".
counter.value = 10; // Logs: "setting property Counter#value = 10".
```

## Call Signature

&gt; **observe**\<`T`\>(`cb`): `PropertyDecorator`

Defined in: [observer/observer.ts:115](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/observer/observer.ts#L115)

Observe every assignment to a property and invoke `cb` with each new value.

The returned decorator redefines the property on the prototype via
`Object.defineProperty`; `cb` runs synchronously inside the setter, so a throw
from `cb` propagates to the assigning code. As with the default form, the
backing value lives in one closure shared across all instances of the class.

### Type Parameters

#### T

`T`

The type of the property value.

### Parameters

#### cb

[`ObserverCallback`](../../observer.types/type-aliases/ObserverCallback)\<`T`\>

Callback to run on each assignment of the observed property.

### Returns

`PropertyDecorator`

The property decorator.

### Example

```ts
class User {
  @observe((value) => {
    console.log("Email changed:", value);
    validateEmail(value);
  })
  email: string = "";

  @observe((value) => {
    metrics.gauge("user.age", value);
  })
  age: number = 0;
}

const user = new User();
user.email = "test@example.com"; // Logs and validates.
user.age = 25; // Records a metric.
```
