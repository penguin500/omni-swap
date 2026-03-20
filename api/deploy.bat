@echo off
echo ========================================
echo  OmniSwap API - Cloudflare Worker Deploy
echo ========================================
echo.
echo This will deploy the OmniSwap API to Cloudflare Workers (FREE)
echo Every bot that calls this API pays 0.5%% to your wallet.
echo.

REM Check if npm is installed
where npm >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: npm not found. Install Node.js from https://nodejs.org
    pause
    exit /b 1
)

REM Install wrangler if needed
echo Installing Cloudflare Wrangler...
npm install -g wrangler 2>nul

REM Login to Cloudflare (opens browser)
echo.
echo Opening browser to login to Cloudflare...
echo If you don't have an account, create one FREE at https://cloudflare.com
echo.
npx wrangler login

REM Deploy
echo.
echo Deploying OmniSwap API...
npx wrangler deploy

echo.
echo ========================================
echo  DEPLOYED! Your API is live at:
echo  https://omniswap-api.YOUR-SUBDOMAIN.workers.dev
echo ========================================
echo.
echo Bots can now call:
echo   GET /v1/quote?input=SOL^&output=USDC^&amount=1000000000
echo   POST /v1/swap
echo.
echo Every swap = 0.5%% fee to your wallet!
echo.
pause
