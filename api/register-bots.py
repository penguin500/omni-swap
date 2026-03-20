"""
OmniSwap Bot Discovery & Registration Script
=============================================
Registers OmniSwap API on major bot directories, DeFi aggregators,
and AI agent marketplaces so bots worldwide can find and use it.

Run: python register-bots.py
"""
import requests
import json
import time

OMNISWAP_INFO = {
    "name": "OmniSwap",
    "description": "Solana Token Swap API for Bots & AI Agents. Best prices via Jupiter aggregator. 0.5% platform fee. Python + JS SDKs.",
    "url": "https://penguin500.github.io/omni-swap/",
    "docs": "https://penguin500.github.io/omni-swap/docs/",
    "api_base": "https://omniswap-api.workers.dev",
    "openapi": "https://penguin500.github.io/omni-swap/api/openapi.json",
    "mcp_manifest": "https://penguin500.github.io/omni-swap/api/mcp-manifest.json",
    "sdk_python": "https://penguin500.github.io/omni-swap/sdk/python/omniswap.py",
    "sdk_js": "https://penguin500.github.io/omni-swap/sdk/js/omniswap.js",
    "chain": "solana",
    "category": "defi",
    "tags": ["swap", "dex", "solana", "jupiter", "bot-api", "agent-tools", "trading"],
    "fee": "0.5% per swap (50 bps)",
    "fee_wallet": "4CaTPEr4k17fsb6reefxRSaFg4jDUnSe29by3qpERZPn",
}

# ============================================================
# STEP 1: Submit to DeFi & Bot Directories
# ============================================================

DIRECTORIES = [
    {
        "name": "DeFi Llama",
        "url": "https://defillama.com/docs/api",
        "action": "Submit protocol via GitHub PR to github.com/DefiLlama/DefiLlama-Adapters",
        "manual": True,
    },
    {
        "name": "DappRadar",
        "url": "https://dappradar.com/submit-dapp",
        "action": "Submit at dappradar.com/submit-dapp with OmniSwap details",
        "manual": True,
    },
    {
        "name": "DeFi Pulse",
        "url": "https://defipulse.com/submit",
        "action": "Submit DeFi protocol listing",
        "manual": True,
    },
    {
        "name": "Solana DApp Store",
        "url": "https://dappstore.app/submit",
        "action": "Submit to Solana mobile DApp store",
        "manual": True,
    },
    {
        "name": "Awesome Solana (GitHub)",
        "url": "https://github.com/avareum/awesome-solana",
        "action": "PR to add OmniSwap under DeFi/DEX tools",
        "manual": True,
    },
    {
        "name": "RapidAPI",
        "url": "https://rapidapi.com/hub",
        "action": "List OmniSwap API on RapidAPI marketplace (huge bot audience)",
        "manual": True,
    },
    {
        "name": "APIs.guru (OpenAPI Directory)",
        "url": "https://apis.guru/",
        "action": "Submit OpenAPI spec to apis.guru directory",
        "auto": True,
    },
    {
        "name": "MCP Server Registry",
        "url": "https://github.com/modelcontextprotocol/servers",
        "action": "PR to add OmniSwap as MCP server for AI agents",
        "manual": True,
    },
    {
        "name": "Toolhouse.ai",
        "url": "https://toolhouse.ai",
        "action": "Register OmniSwap tools for AI agent marketplace",
        "manual": True,
    },
    {
        "name": "AgentOps",
        "url": "https://agentops.ai",
        "action": "Register as agent tool provider",
        "manual": True,
    },
]

# ============================================================
# STEP 2: Auto-submissions (where API exists)
# ============================================================

def submit_to_apis_guru():
    """Submit OpenAPI spec to APIs.guru directory."""
    try:
        r = requests.post("https://apis.guru/api/v1/submit", json={
            "url": OMNISWAP_INFO["openapi"],
            "name": "omniswap",
        }, timeout=15)
        return r.status_code, r.text[:200]
    except Exception as e:
        return 0, str(e)

def test_api_reachability():
    """Test if our API endpoints are reachable."""
    endpoints = [
        ("OpenAPI Spec", f"{OMNISWAP_INFO['url']}api/openapi.json"),
        ("MCP Manifest", f"{OMNISWAP_INFO['url']}api/mcp-manifest.json"),
        ("Docs Page", f"{OMNISWAP_INFO['url']}docs/"),
        ("Python SDK", f"{OMNISWAP_INFO['url']}sdk/python/omniswap.py"),
        ("JS SDK", f"{OMNISWAP_INFO['url']}sdk/js/omniswap.js"),
        ("Main Site", OMNISWAP_INFO['url']),
    ]
    results = []
    for name, url in endpoints:
        try:
            r = requests.head(url, timeout=10, allow_redirects=True)
            results.append((name, url, r.status_code))
        except Exception as e:
            results.append((name, url, f"ERROR: {e}"))
    return results

# ============================================================
# STEP 3: Generate bot-friendly README for GitHub
# ============================================================

def generate_bot_readme():
    return f"""# OmniSwap API - Solana Token Swaps for Bots & Agents

> **The simplest way to swap tokens on Solana.** 3 lines of code. Best prices via Jupiter. Built for trading bots and AI agents.

## Quick Start

### Python
```python
from omniswap import OmniSwap

swap = OmniSwap()
quote = swap.quote("SOL", "USDC", amount_sol=1.5)
result = swap.execute("SOL", "USDC", amount_sol=1.5, private_key="your_key")
```

### JavaScript
```javascript
import {{ OmniSwap }} from '@omniswap/sdk';

const swap = new OmniSwap();
const quote = await swap.quote('SOL', 'USDC', 1.5);
const tx = await swap.buildTransaction('SOL', 'USDC', 1.5, walletPublicKey);
```

### cURL
```bash
curl "https://omniswap-api.workers.dev/v1/quote?inputMint=So11...112&outputMint=EPjF...1v&amount=1000000000&slippageBps=300"
```

## Features
- Best prices via Jupiter aggregator
- All Solana SPL tokens supported
- 0.5% platform fee (lowest in market)
- Python + JavaScript SDKs
- AI agent tool definitions (Claude, GPT, custom agents)
- MCP server support
- OpenAPI 3.1 spec available

## Links
- [API Documentation]({OMNISWAP_INFO['docs']})
- [OpenAPI Spec]({OMNISWAP_INFO['url']}api/openapi.json)
- [MCP Manifest]({OMNISWAP_INFO['url']}api/mcp-manifest.json)
- [Python SDK]({OMNISWAP_INFO['url']}sdk/python/omniswap.py)
- [JS SDK]({OMNISWAP_INFO['url']}sdk/js/omniswap.js)

## Fee
0.5% per swap (50 basis points) — collected automatically via Jupiter's platformFeeBps parameter.
Fee wallet: `{OMNISWAP_INFO['fee_wallet']}`
"""


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  OMNISWAP BOT DISCOVERY & REGISTRATION")
    print("=" * 60)
    print()

    # Test reachability
    print("Testing API endpoint reachability...")
    results = test_api_reachability()
    for name, url, status in results:
        icon = "[OK]" if status == 200 else "[!!]"
        print(f"  {icon} {name}: {status}")
    print()

    # Show directory registration checklist
    print("BOT DIRECTORY REGISTRATION CHECKLIST:")
    print("-" * 50)
    for d in DIRECTORIES:
        print(f"  [ ] {d['name']}")
        print(f"      URL: {d['url']}")
        print(f"      Action: {d['action']}")
        print()

    # Auto-submit where possible
    print("AUTO-SUBMISSIONS:")
    print("-" * 50)
    status, resp = submit_to_apis_guru()
    print(f"  APIs.guru: status={status}, response={resp[:100]}")
    print()

    # Generate README
    readme = generate_bot_readme()
    with open("BOT_README.md", "w") as f:
        f.write(readme)
    print("Generated BOT_README.md for GitHub")
    print()

    print("=" * 60)
    print("  HOW BOTS FIND & USE OMNISWAP")
    print("=" * 60)
    print("""
  1. DIRECT SDK INSTALL:
     pip install omniswap    (Python bots)
     npm install @omniswap/sdk  (JS bots)

  2. API DISCOVERY:
     OpenAPI spec at: /api/openapi.json
     MCP manifest at: /api/mcp-manifest.json
     Docs at: /docs/

  3. AI AGENT INTEGRATION:
     Claude/GPT agents use tool definitions from SDK
     MCP-compatible agents auto-discover via manifest

  4. REFERRAL:
     Share SDK link with bot developers
     Post on Twitter, Discord, Telegram bot groups
     Submit to DeFi directories (checklist above)

  5. EVERY SWAP = 0.5% FEE TO YOUR WALLET
     Fee wallet: 4CaTPEr4k17fsb6reefxRSaFg4jDUnSe29by3qpERZPn
""")
