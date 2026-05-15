# Function: debounceFn()

> **debounceFn**\<`D`, `A`\>(`originalMethod`, `delayMs`): [`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

Defined in: [debounce/debounce.fn.ts:52](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/debounce/debounce.fn.ts#L52)

Wraps a method to debounce its execution.
The method will only execute after the specified delay has passed
since the last time it was called.

## Type Parameters

### D

`D` = `unknown`

The return type of the original method

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to debounce

### delayMs

`number`

The debounce delay in milliseconds

## Returns

[`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

The debounced method

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
