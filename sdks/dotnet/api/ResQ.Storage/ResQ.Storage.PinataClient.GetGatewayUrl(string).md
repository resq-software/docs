### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinataClient](./ResQ.Storage.PinataClient.md 'ResQ\.Storage\.PinataClient')

## PinataClient\.GetGatewayUrl\(string\) Method

Gets the gateway URL for accessing content by CID\.

```csharp
public string GetGatewayUrl(string cid);
```
#### Parameters

<a name='ResQ.Storage.PinataClient.GetGatewayUrl(string).cid'></a>

`cid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The IPFS Content Identifier\.

Implements [GetGatewayUrl\(string\)](./ResQ.Storage.IStorageClient.GetGatewayUrl(string).md 'ResQ\.Storage\.IStorageClient\.GetGatewayUrl\(string\)')

#### Returns
[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')  
The full URL to access the content through the configured gateway\.

#### Exceptions

[System\.ArgumentNullException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentnullexception 'System\.ArgumentNullException')  
Thrown when cid is null or empty\.

### Example

```csharp
var gatewayUrl = storage.GetGatewayUrl("Qmabc123...");
Console.WriteLine($"Access at: {gatewayUrl}");
// Output: https://gateway.pinata.cloud/ipfs/Qmabc123...
```

### Remarks
The returned URL can be used in web browsers or HTTP clients to retrieve the content\.
The gateway URL is constructed from the configured [GatewayUrl](./ResQ.Storage.PinataOptions.GatewayUrl.md 'ResQ\.Storage\.PinataOptions\.GatewayUrl')\.
