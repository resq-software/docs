### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[NeoClientOptions](./ResQ.Blockchain.NeoClientOptions.md 'ResQ\.Blockchain\.NeoClientOptions')

## NeoClientOptions\.MaxRetryAttempts Property

Gets or sets the maximum number of retry attempts for failed transactions\.

```csharp
public int MaxRetryAttempts { get; set; }
```

#### Property Value
[System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')  
The maximum retry attempts\. Default is 3\.

### Example

```csharp
// Retry up to 5 times
options.MaxRetryAttempts = 5;

// Disable retries
options.MaxRetryAttempts = 0;
```

### Remarks
If a blockchain transaction fails due to transient errors \(network issues,
temporary node unavailability\), the client will retry up to this many times
before giving up\. Set to 0 to disable retries\.
