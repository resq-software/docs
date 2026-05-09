### [ResQ\.Storage](./ResQ.Storage.md 'ResQ\.Storage').[PinMetadata](./ResQ.Storage.PinMetadata.md 'ResQ\.Storage\.PinMetadata')

## PinMetadata\(string, string, long, DateTimeOffset, Dictionary\<string,string\>\) Constructor

Represents metadata for a file pinned to IPFS\.

```csharp
public PinMetadata(string Cid, string Name, long SizeBytes, System.DateTimeOffset PinnedAt, System.Collections.Generic.Dictionary<string,string> KeyValues);
```
#### Parameters

<a name='ResQ.Storage.PinMetadata.PinMetadata(string,string,long,System.DateTimeOffset,System.Collections.Generic.Dictionary_string,string_).Cid'></a>

`Cid` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The IPFS Content Identifier\.

<a name='ResQ.Storage.PinMetadata.PinMetadata(string,string,long,System.DateTimeOffset,System.Collections.Generic.Dictionary_string,string_).Name'></a>

`Name` [System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')

The human\-readable name assigned to the pin\.

<a name='ResQ.Storage.PinMetadata.PinMetadata(string,string,long,System.DateTimeOffset,System.Collections.Generic.Dictionary_string,string_).SizeBytes'></a>

`SizeBytes` [System\.Int64](https://learn.microsoft.com/en-us/dotnet/api/system.int64 'System\.Int64')

The size of the pinned content in bytes\.

<a name='ResQ.Storage.PinMetadata.PinMetadata(string,string,long,System.DateTimeOffset,System.Collections.Generic.Dictionary_string,string_).PinnedAt'></a>

`PinnedAt` [System\.DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset 'System\.DateTimeOffset')

UTC timestamp when the content was pinned\.

<a name='ResQ.Storage.PinMetadata.PinMetadata(string,string,long,System.DateTimeOffset,System.Collections.Generic.Dictionary_string,string_).KeyValues'></a>

`KeyValues` [System\.Collections\.Generic\.Dictionary&lt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')[,](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')[System\.String](https://learn.microsoft.com/en-us/dotnet/api/system.string 'System\.String')[&gt;](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2 'System\.Collections\.Generic\.Dictionary\`2')

Dictionary of custom metadata key\-value pairs\.

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
