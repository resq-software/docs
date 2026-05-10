# time

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`to_proto_timestamp`](#to_proto_timestamp) | Convert std::chrono::system_clock::time_point to google::protobuf::Timestamp. |
| `std::chrono::system_clock::time_point` | [`from_proto_timestamp`](#from_proto_timestamp) | Convert google::protobuf::Timestamp to std::chrono::system_clock::time_point. |

---

#### to_proto_timestamp

`inline`

```cpp
inline void to_proto_timestamp(const std::chrono::system_clock::time_point & from, google::protobuf::Timestamp * to)
```

Convert std::chrono::system_clock::time_point to google::protobuf::Timestamp.

---

#### from_proto_timestamp

`inline`

```cpp
inline std::chrono::system_clock::time_point from_proto_timestamp(const google::protobuf::Timestamp & from)
```

Convert google::protobuf::Timestamp to std::chrono::system_clock::time_point.

