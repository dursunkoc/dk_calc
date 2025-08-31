# dk_calc

A Python project for custom mathematical operations and customer/product management.

## Features
- DK-style mathematical operations (add, subtract, multiply, divide)

## Requirements
- Python 3.12+
- uv

## Setup
0. initialize uv project
   ```sh
   uv init dk_calc
   ```
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd dk_calc
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   uv venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   uv sync
   ```

## Usage
- define mcp server:
  ```json
  {
	"servers": {
		"dk-math": {
			"command": "/Users/ttdkoc/.local/bin/uv",
			"args": [
				"--directory",
				"/Users/ttdkoc/Documents/dev/workspaces/python/dk_calc",
				"run",
				"dk_math.py"
			]
		}
	}
  }
  ```