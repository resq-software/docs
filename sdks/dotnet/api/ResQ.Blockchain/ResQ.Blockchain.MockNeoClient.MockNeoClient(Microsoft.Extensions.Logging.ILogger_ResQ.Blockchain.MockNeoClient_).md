---
sidebarTitle: 'MockNeoClient(MockNeoClient_)'
---

### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\(ILogger\<MockNeoClient\>\) Constructor

Initializes a new instance of the [MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient') class\.

```csharp
public MockNeoClient(Microsoft.Extensions.Logging.ILogger<ResQ.Blockchain.MockNeoClient> logger);
```
#### Parameters

<a name='ResQ.Blockchain.MockNeoClient.MockNeoClient(Microsoft.Extensions.Logging.ILogger_ResQ.Blockchain.MockNeoClient_).logger'></a>

`logger` [Microsoft\.Extensions\.Logging\.ILogger&lt;](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1 'Microsoft\.Extensions\.Logging\.ILogger\`1')[MockNeoClient](./ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1 'Microsoft\.Extensions\.Logging\.ILogger\`1')

The logger instance for recording mock operations\.

### Example

```csharp
var logger = loggerFactory.CreateLogger<MockNeoClient>();
var client = new MockNeoClient(logger);
```

### Remarks
The mock client starts with a default block height of 1,000,000 and maintains
an empty event store that gets populated as events are recorded\.
