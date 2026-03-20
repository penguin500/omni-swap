# OmniSwap Python SDK

The simplest way to swap any Solana token. Built for bots & AI agents.

## Install

```bash
pip install omniswap
```

Or download directly:
```bash
curl -O https://penguin500.github.io/omniseedai/sdk/python/omniswap.py
```

## Quick Start

```python
from omniswap import OmniSwap

swap = OmniSwap()

# Get quote
quote = swap.quote("SOL", "USDC", amount_sol=1.5)
print(f"Output: {quote['output_human']} USDC")

# Execute swap
result = swap.execute("SOL", "USDC", amount_sol=1.5, private_key="your_key")
print(f"TX: {result['explorer']}")

# Get price
sol = swap.price("SOL")
print(f"SOL: ${sol['priceUsd']}")
```

## For AI Agents

```python
tools = swap.as_agent_tools()  # Returns Claude/GPT tool definitions
```

## Docs

https://penguin500.github.io/omniseedai/docs/
