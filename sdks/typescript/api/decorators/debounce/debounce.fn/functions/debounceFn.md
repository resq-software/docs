# Function: debounceFn()

&gt; **debounceFn**\<`D`, `A`\>(`originalMethod`, `delayMs`): [`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

Defined in: [debounce/debounce.fn.ts:69](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/debounce/debounce.fn.ts#L69)

Wraps a method to debounce its execution.
The method will only execute after the specified delay has passed
since the last time it was called.

Effectful and trailing-edge only: each call clears the shared pending
`setTimeout` and arms a new one, so a single wrapper collapses *all* its
calls (regardless of arguments) into the last one. The wrapper returns
`undefined` immediately — the original method's return value is **discarded**,
so this cannot wrap a method whose result the caller needs. The deferred
invocation uses the `this` and arguments of the most recent call; if the
method throws, it throws inside the timer callback (unobservable to the
caller). No `AbortSignal` / cancellation.

## Type Parameters

### D

`D` = `unknown`

The return type of the original method.

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method.

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to debounce.

### delayMs

`number`

The debounce delay in milliseconds.

## Returns

[`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

The debounced wrapper; it always returns `undefined` (`void`), never
  the wrapped method's value.

## Example

```typescript
class SearchService {
  search(query: string): void {
    console.log(`Searching for: ${query}`);
  }
}

const service = new SearchService();
const debouncedSearch = debounceFn(
  service.search.bind(service),
  300
);

// Rapid calls
debouncedSearch('a');
debouncedSearch('ab');
debouncedSearch('abc');

// Only "Searching for: abc" is logged after 300ms
```
