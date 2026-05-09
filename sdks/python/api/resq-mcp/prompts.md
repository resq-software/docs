<a id="resq_mcp.prompts"></a>

# resq\_mcp.prompts

MCP prompt templates for the ResQ server.

<a id="resq_mcp.prompts.re"></a>

## re

<a id="resq_mcp.prompts.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.prompts.mcp"></a>

## mcp

<a id="resq_mcp.prompts.incident_response_plan"></a>

#### incident\_response\_plan

```python
@mcp.prompt()
def incident_response_plan(incident_id: str) -> str
```

Generate a structured prompt template for incident response planning.

Provides a framework for AI agents or human operators to systematically
analyze incidents and develop comprehensive response plans using
available MCP tools and resources.

Template Sections:
1. Situation Summary: Analyze current state and severity
2. Asset Allocation: Review and assign available resources
3. Risk Assessment: Evaluate hazards and constraints

**Arguments**:

- `incident_id` - The incident identifier to analyze (e.g., "INC-123").
  

**Returns**:

- `str` - Formatted prompt template with:
  - Analysis instructions
  - Tool references (get_deployment_strategy, resq://drones/active)
  - Expected output format
  

**Example**:

  >>> prompt = incident_response_plan("INC-456")
  >>> # Use with LLM:
  >>> response = llm.complete(prompt)
  >>> # LLM will call tools and produce structured response
  
  Use Cases:
  - AI-assisted crisis coordination (Spoon OS agent)
  - Human operator decision support
  - Training scenario generation
  - Post-incident plan review
  
  Integration:
  Prompt references MCP tools and resources that the LLM can call:
  - get_deployment_strategy(incident_id) -> OptimizationStrategy
  - resq://drones/active -> Fleet status
  - Additional sector/swarm status tools as needed
