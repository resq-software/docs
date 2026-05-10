**bin_explorer > analysis**

# Module: analysis

## Contents

**Structs**

- [`AnalyzeOptions`](#analyzeoptions) - Analysis options for a single binary input.
- [`BinaryAnalyzer`](#binaryanalyzer) - Analyzer for parsing binary metadata and optional disassembly.
- [`BinaryReport`](#binaryreport) - Structured report generated for a binary.
- [`DisassemblyCoverage`](#disassemblycoverage) - Summary counters for disassembly backend coverage.
- [`FunctionBackendCoverage`](#functionbackendcoverage) - Backend assignment for a specific function.
- [`FunctionReport`](#functionreport) - Function-level analysis.
- [`Instruction`](#instruction) - Machine instruction row.
- [`SectionInfo`](#sectioninfo) - Section metadata.
- [`SymbolInfo`](#symbolinfo) - Symbol metadata.

---

## bin_explorer::analysis::AnalyzeOptions

*Struct*

Analysis options for a single binary input.

**Fields:**
- `include_disassembly: bool` - Include machine-level disassembly when available.
- `max_functions: usize` - Maximum number of functions to disassemble.
- `max_symbols: usize` - Maximum number of symbols to include in report.
- `max_instructions_per_function: usize` - Maximum instructions per function.

**Trait Implementations:**

- **Default**
  - `fn default() -> Self`
- **Clone**
  - `fn clone(self: &Self) -> AnalyzeOptions`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## bin_explorer::analysis::BinaryAnalyzer

*Struct*

Analyzer for parsing binary metadata and optional disassembly.

**Unit Struct**

**Methods:**

- `fn analyze_path(path: &Path, options: &AnalyzeOptions) -> Result<BinaryReport>` - Analyze a binary file and return a normalized report.

**Trait Implementations:**

- **Default**
  - `fn default() -> BinaryAnalyzer`



## bin_explorer::analysis::BinaryReport

*Struct*

Structured report generated for a binary.

**Fields:**
- `path: std::path::PathBuf` - Input path.
- `format: String` - File format (elf, pe, macho, wasm, ...).
- `architecture: String` - CPU architecture.
- `endianness: String` - Endianness.
- `entry: u64` - Entrypoint virtual address.
- `size_bytes: u64` - Binary size in bytes.
- `sections: Vec<SectionInfo>` - Section inventory.
- `symbols: Vec<SymbolInfo>` - Symbol inventory.
- `functions: Vec<FunctionReport>` - Per-function disassembly.
- `disassembly_backend: Option<String>` - Backend used for disassembly generation.
- `disassembly_attempts: Vec<String>` - Attempt log for disassembly backends (success/fallback diagnostics).
- `disassembly_coverage: Option<DisassemblyCoverage>` - Coverage summary for per-function disassembly backend assignment.
- `function_backend_coverage: Vec<FunctionBackendCoverage>` - Per-function backend assignment and instruction counts.
- `warnings: Vec<String>` - Non-fatal diagnostics from tooling.

**Trait Implementations:**

- **Deserialize**
  - `fn deserialize<__D>(__deserializer: __D) -> _serde::__private228::Result<Self, <__D as >::Error>`
- **Serialize**
  - `fn serialize<__S>(self: &Self, __serializer: __S) -> _serde::__private228::Result<<__S as >::Ok, <__S as >::Error>`
- **Clone**
  - `fn clone(self: &Self) -> BinaryReport`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## bin_explorer::analysis::DisassemblyCoverage

*Struct*

Summary counters for disassembly backend coverage.

**Fields:**
- `total_functions: usize` - Number of functions considered for disassembly.
- `functions_with_instructions: usize` - Number of functions that have at least one decoded instruction.
- `capstone_functions: usize` - Number of functions populated from Capstone.
- `objdump_functions: usize` - Number of functions populated from objdump fallback.
- `missing_functions: usize` - Number of functions with zero instructions after all backends.

**Trait Implementations:**

- **Default**
  - `fn default() -> DisassemblyCoverage`
- **Deserialize**
  - `fn deserialize<__D>(__deserializer: __D) -> _serde::__private228::Result<Self, <__D as >::Error>`
- **Serialize**
  - `fn serialize<__S>(self: &Self, __serializer: __S) -> _serde::__private228::Result<<__S as >::Ok, <__S as >::Error>`
- **Clone**
  - `fn clone(self: &Self) -> DisassemblyCoverage`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## bin_explorer::analysis::FunctionBackendCoverage

*Struct*

Backend assignment for a specific function.

**Fields:**
- `name: String` - Function name.
- `backend: String` - Backend used (`capstone`, `objdump`, or `none`).
- `instruction_count: usize` - Number of instructions captured for this function.

**Trait Implementations:**

- **Serialize**
  - `fn serialize<__S>(self: &Self, __serializer: __S) -> _serde::__private228::Result<<__S as >::Ok, <__S as >::Error>`
- **Clone**
  - `fn clone(self: &Self) -> FunctionBackendCoverage`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`
- **Deserialize**
  - `fn deserialize<__D>(__deserializer: __D) -> _serde::__private228::Result<Self, <__D as >::Error>`



## bin_explorer::analysis::FunctionReport

*Struct*

Function-level analysis.

**Fields:**
- `name: String` - Function symbol name.
- `address: u64` - Start address.
- `size: u64` - Declared symbol size.
- `instructions: Vec<Instruction>` - Disassembled instructions.

**Trait Implementations:**

- **Deserialize**
  - `fn deserialize<__D>(__deserializer: __D) -> _serde::__private228::Result<Self, <__D as >::Error>`
- **Serialize**
  - `fn serialize<__S>(self: &Self, __serializer: __S) -> _serde::__private228::Result<<__S as >::Ok, <__S as >::Error>`
- **Clone**
  - `fn clone(self: &Self) -> FunctionReport`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## bin_explorer::analysis::Instruction

*Struct*

Machine instruction row.

**Fields:**
- `address: u64` - Instruction address.
- `text: String` - Disassembled opcode + operands.

**Trait Implementations:**

- **Deserialize**
  - `fn deserialize<__D>(__deserializer: __D) -> _serde::__private228::Result<Self, <__D as >::Error>`
- **Serialize**
  - `fn serialize<__S>(self: &Self, __serializer: __S) -> _serde::__private228::Result<<__S as >::Ok, <__S as >::Error>`
- **Clone**
  - `fn clone(self: &Self) -> Instruction`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## bin_explorer::analysis::SectionInfo

*Struct*

Section metadata.

**Fields:**
- `name: String` - Section name.
- `address: u64` - Load address.
- `size: u64` - Raw size.
- `kind: String` - Canonical kind.

**Trait Implementations:**

- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`
- **Deserialize**
  - `fn deserialize<__D>(__deserializer: __D) -> _serde::__private228::Result<Self, <__D as >::Error>`
- **Serialize**
  - `fn serialize<__S>(self: &Self, __serializer: __S) -> _serde::__private228::Result<<__S as >::Ok, <__S as >::Error>`
- **Clone**
  - `fn clone(self: &Self) -> SectionInfo`



## bin_explorer::analysis::SymbolInfo

*Struct*

Symbol metadata.

**Fields:**
- `name: String` - Symbol name.
- `address: u64` - Address.
- `size: u64` - Size in bytes.
- `kind: String` - Symbol kind.
- `is_global: bool` - Whether symbol is externally visible.

**Trait Implementations:**

- **Deserialize**
  - `fn deserialize<__D>(__deserializer: __D) -> _serde::__private228::Result<Self, <__D as >::Error>`
- **Serialize**
  - `fn serialize<__S>(self: &Self, __serializer: __S) -> _serde::__private228::Result<<__S as >::Ok, <__S as >::Error>`
- **Clone**
  - `fn clone(self: &Self) -> SymbolInfo`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



