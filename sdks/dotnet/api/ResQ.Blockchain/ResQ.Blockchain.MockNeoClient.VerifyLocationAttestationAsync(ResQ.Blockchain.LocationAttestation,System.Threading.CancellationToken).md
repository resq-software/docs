### [ResQ\.Blockchain](ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\.VerifyLocationAttestationAsync\(LocationAttestation, CancellationToken\) Method

Verifies a location attestation in mock mode\.

```csharp
public System.Threading.Tasks.Task<bool> VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation attestation, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.MockNeoClient.VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).attestation'></a>

`attestation` [LocationAttestation](ResQ.Blockchain.LocationAttestation.md 'ResQ\.Blockchain\.LocationAttestation')

The location attestation to verify\.

<a name='ResQ.Blockchain.MockNeoClient.VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

Implements [VerifyLocationAttestationAsync\(LocationAttestation, CancellationToken\)](ResQ.Blockchain.INeoClient.VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).md 'ResQ\.Blockchain\.INeoClient\.VerifyLocationAttestationAsync\(ResQ\.Blockchain\.LocationAttestation, System\.Threading\.CancellationToken\)')

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
True if the attestation has a non\-empty signature; false otherwise\.

### Example

```csharp
// Valid attestation (has signature)
var valid = new LocationAttestation(..., Signature: "0xabc...");
var isValid = await mockClient.VerifyLocationAttestationAsync(valid);
// Returns: true

// Invalid attestation (no signature)
var invalid = new LocationAttestation(..., Signature: "");
var isInvalid = await mockClient.VerifyLocationAttestationAsync(invalid);
// Returns: false
```

### Remarks
In mock mode, verification simply checks that a signature is present\.
No actual cryptographic verification is performed\. This allows testing
of both valid and invalid attestation scenarios by providing or omitting
the signature field\.
