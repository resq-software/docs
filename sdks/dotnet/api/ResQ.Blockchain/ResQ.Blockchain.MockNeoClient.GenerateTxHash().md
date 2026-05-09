### [ResQ\.Blockchain](ResQ.Blockchain.md 'ResQ\.Blockchain').[MockNeoClient](ResQ.Blockchain.MockNeoClient.md 'ResQ\.Blockchain\.MockNeoClient')

## MockNeoClient\.GenerateTxHash\(\) Method

Generates a random transaction hash for mock purposes\.

```csharp
private static string GenerateTxHash();
```

#### Returns
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
A hexadecimal string representing a 32\-byte transaction hash, prefixed with "0x"\.

### Remarks
Uses [System\.Security\.Cryptography\.RandomNumberGenerator](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.randomnumbergenerator 'System\.Security\.Cryptography\.RandomNumberGenerator') to generate cryptographically secure random bytes,
ensuring unique transaction hashes for each mock operation\.
