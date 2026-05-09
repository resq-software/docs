### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[NeoClientOptions](./ResQ.Blockchain.NeoClientOptions.md 'ResQ\.Blockchain\.NeoClientOptions')

## NeoClientOptions\.ConfirmationTimeoutSeconds Property

Gets or sets the timeout for waiting for transaction confirmation\.

```csharp
public int ConfirmationTimeoutSeconds { get; set; }
```

#### Property Value
[System\.Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32 'System\.Int32')  
The timeout in seconds\. Default is 30 seconds\.

### Example

```csharp
// Wait up to 60 seconds for confirmation
options.ConfirmationTimeoutSeconds = 60;
```

### Remarks
This defines how long the client will wait for a transaction to be confirmed
on the blockchain before timing out\. Increase this value if operating on a
network with slower block times or high congestion\.
