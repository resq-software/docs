### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage')

## PinMetadata Class

Represents metadata for a file pinned to IPFS\.

```csharp
public record PinMetadata : System.IEquatable<ResQ.Storage.PinMetadata>
```

Inheritance [System\.Object](https://learn.microsoft.com/en-us/dotnet/api/system.object 'System\.Object') &#129106; PinMetadata

Implements [System\.IEquatable&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')[PinMetadata](./ResQ.Storage.PinMetadata.md 'ResQ\.Storage\.PinMetadata')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1 'System\.IEquatable\`1')

### Example

```csharp
var pins = await storageClient.ListPinsAsync("evidence-");
foreach (var pin in pins)
{
    Console.WriteLine($"{pin.Name}: {pin.Cid}");
    foreach (var kv in pin.KeyValues)
    {
        Console.WriteLine($"  {kv.Key}: {kv.Value}");
    }
}
```

### Remarks
Pin metadata provides information about files that have been pinned to IPFS
through the Pinata service\. This includes the CID, custom metadata key\-value
pairs, and pinning information\. Pinned files are guaranteed to remain available
on the IPFS network as long as they remain pinned\.

| Constructors | |
| :--- | :--- |
| [PinMetadata\(string, string, long, DateTimeOffset, Dictionary&lt;string,string&gt;\)](./ResQ.Storage.PinMetadata.PinMetadata(string,string,long,System.DateTimeOffset,System.Collections.Generic.Dictionary_string,string_).md 'ResQ\.Storage\.PinMetadata\.PinMetadata\(string, string, long, System\.DateTimeOffset, System\.Collections\.Generic\.Dictionary\<string,string\>\)') | Represents metadata for a file pinned to IPFS\. |

| Properties | |
| :--- | :--- |
| [Cid](./ResQ.Storage.PinMetadata.Cid.md 'ResQ\.Storage\.PinMetadata\.Cid') | The IPFS Content Identifier\. |
| [KeyValues](./ResQ.Storage.PinMetadata.KeyValues.md 'ResQ\.Storage\.PinMetadata\.KeyValues') | Dictionary of custom metadata key\-value pairs\. |
| [Name](./ResQ.Storage.PinMetadata.Name.md 'ResQ\.Storage\.PinMetadata\.Name') | The human\-readable name assigned to the pin\. |
| [PinnedAt](./ResQ.Storage.PinMetadata.PinnedAt.md 'ResQ\.Storage\.PinMetadata\.PinnedAt') | UTC timestamp when the content was pinned\. |
| [SizeBytes](./ResQ.Storage.PinMetadata.SizeBytes.md 'ResQ\.Storage\.PinMetadata\.SizeBytes') | The size of the pinned content in bytes\. |
