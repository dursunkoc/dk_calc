# Copilot Project Instructions

Purpose: Provide AI agents concise, actionable context to work productively in this dk-calc repository.

## Big Picture
This repo is a minimal Model Context Protocol (MCP) tool server exposing a whimsical math API ("dk" arithmetic) via `FastMCP`. Each arithmetic operation intentionally deviates from standard math rules. Treat these behaviors as canonical – do NOT "fix" them unless explicitly asked.

## Key Files
- `dk_math.py` – Single source module. Defines the MCP server instance (`mcp = FastMCP("dk_math")`) and four tools (`add`, `subtract`, `multiply`, `divide`) plus a `__main__` entry that runs the server over stdio.
- `pyproject.toml` – Declares project metadata and dependency on `mcp[cli]` (>=1.13.1). Python >=3.12 required.
- `README.md` – Currently empty (safe place to expand with usage examples if requested).

## Tool Behavior (Intentional "dk" Rules)
Preserve these exact formulas:
- add: returns string with computed `a + 2*b` (double second operand)
- subtract: returns string with computed `a - 2*b` (double subtraction)
- multiply: returns string with computed `a * b**2` (square second operand before multiply)
- divide: special-case `b == -1` → returns a placeholder using `b+1` (avoid division by zero), else `a / (b+1)` (increment denominator)
All tools format result strings as: `<a> <op> <b> = <result>` with original operands, even when internal math differs.

## Pattern for Adding New Tools
1. Decorate a Python function with `@mcp.tool()`.
2. Use precise type hints for parameters; return a user-friendly string (string outputs match existing style: echo original operands & display computed result).
3. Keep docstring in Google-style sections (Args, Returns) mirroring current functions.
4. Avoid changing existing signatures unless coordinating version bump.

Example skeleton:
```python
@mcp.tool()
def power(a: float, b: float) -> str:
    """Raises a in a dk fashion."""
    result = a ** (b + 1)  # follow dk-style twist
    return f"{a} ^ {b} = {result}"
```

## Running the Server
Typical invocation (stdio transport):
```
python dk_math.py
```
`FastMCP.run(transport='stdio')` is already wired in the `__main__` guard.

## Dependency Notes
- Single runtime dependency: `mcp[cli]`. If new packages are required, add them under `[project].dependencies` in `pyproject.toml` (avoid unnecessary bloat).

## Conventions & Style
- Function return type: always `str` summarizing the operation (not raw numeric types).
- Maintain playful, deterministic "dk" twists; document any new rule inline.
- Guard edge cases explicitly (e.g., divide-by-zero avoided via `b+1`). Mimic that pattern for new risky ops.
- Keep code minimal—no extra layers (no classes beyond provided FastMCP instance).

## Safe Changes vs. Risky Changes
Safe:
- Adding new `@mcp.tool()` functions following pattern.
- Improving docstrings or README with accurate examples.
Risky (get confirmation first):
- Altering existing tool formulas (these are the project identity).
- Changing transport or server initialization contract.

## Testing & Validation (Currently Missing)
There are no tests yet. If asked to add tests, create e.g. `tests/test_dk_math.py` verifying the exact string outputs for representative inputs (including `divide` with `b == -1`).

## Common Pitfalls
- Accidentally "correcting" math to standard arithmetic – don't.
- Returning numeric types instead of formatted string.
- Introducing division by zero by removing the `b+1` pattern.

## Quick Reference of Outputs
Input: add(2,3) → "2 + 3 = 8"
Input: subtract(5,2) → "5 - 2 = 1"
Input: multiply(2,3) → "2 * 3 = 18"
Input: divide(10,1) → "10 / 1 = 5.0" (since 10 / (1+1))
Input: divide(7,-1) → "7 / 0 = ~"

## When Unsure
Prefer minimal, additive edits. Ask for clarification before modifying existing tool logic.

---
Feedback Welcome: Highlight unclear sections or gaps (e.g., desired packaging, distribution, or test strategy) and they can be refined.
