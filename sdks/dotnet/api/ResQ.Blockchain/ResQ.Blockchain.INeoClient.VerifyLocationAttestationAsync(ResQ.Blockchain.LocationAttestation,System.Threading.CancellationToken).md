### [ResQ\.Blockchain](./ResQ.Blockchain.md 'ResQ\.Blockchain').[INeoClient](./ResQ.Blockchain.INeoClient.md 'ResQ\.Blockchain\.INeoClient')

## INeoClient\.VerifyLocationAttestationAsync\(LocationAttestation, CancellationToken\) Method

Verifies a location attestation signature on the blockchain\.

```csharp
System.Threading.Tasks.Task<bool> VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation attestation, System.Threading.CancellationToken cancellationToken=default(System.Threading.CancellationToken));
```
#### Parameters

<a name='ResQ.Blockchain.INeoClient.VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).attestation'></a>

`attestation` [LocationAttestation](./ResQ.Blockchain.LocationAttestation.md 'ResQ\.Blockchain\.LocationAttestation')

The location attestation to verify\.

<a name='ResQ.Blockchain.INeoClient.VerifyLocationAttestationAsync(ResQ.Blockchain.LocationAttestation,System.Threading.CancellationToken).cancellationToken'></a>

`cancellationToken` [System\.Threading\.CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken 'System\.Threading\.CancellationToken')

Cancellation token for the operation\.

#### Returns
[System\.Threading\.Tasks\.Task&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')[System\.Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean 'System\.Boolean')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1 'System\.Threading\.Tasks\.Task\`1')  
True if the attestation signature is valid and matches the drone's registered public key;
false otherwise\.

#### Exceptions

[System\.OperationCanceledException](https://learn.microsoft.com/en-us/dotnet/api/system.operationcanceledexception 'System\.OperationCanceledException')  
Thrown when the operation is cancelled\.

### Example

```csharp
var isValid = await neoClient.VerifyLocationAttestationAsync(attestation);
if (isValid)
{
    Console.WriteLine("Location attestation verified");
}
else
{
    Console.WriteLine("WARNING: Invalid attestation signature!");
}
```

### Remarks
This method verifies that the location data was signed by the legitimate drone
and has not been tampered with\. It checks the signature against the drone's
public key stored on the blockchain\.
