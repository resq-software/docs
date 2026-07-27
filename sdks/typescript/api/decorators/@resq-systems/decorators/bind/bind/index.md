# @resq-systems/decorators/bind/bind

## Fileoverview

`@bind` decorator — auto-bind a class method to its instance so
`this` stays correct even when the method is detached and passed as a
callback. Binds lazily on first access.

## Example

```typescript
class EventHandler {
  private count = 0;

  @bind
  handleClick(event: MouseEvent): void {
    this.count++; // `this` correctly refers to the EventHandler instance.
    console.log(`Clicked ${this.count} times`);
  }
}

const handler = new EventHandler();
// Works correctly even when passed as a bare callback.
button.addEventListener("click", handler.handleClick);
```

## Functions

- [bind](./functions/bind)
