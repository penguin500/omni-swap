@echo off
echo ==========================================
echo  OmniSeed AI - Deploy to GitHub Pages
echo ==========================================
echo.

cd /d "%~dp0"

:: Check if git is initialized
if not exist ".git" (
    echo Initializing git repo...
    git init
    git branch -M main
)

:: Add all files
git add -A
git commit -m "Deploy OmniSeed AI swap site"

:: Check if remote exists
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo.
    echo ==========================================
    echo  SETUP NEEDED - Run this command first:
    echo ==========================================
    echo.
    echo   git remote add origin https://github.com/YOUR_USERNAME/omniseedai.com.git
    echo.
    echo Replace YOUR_USERNAME with your GitHub username, then run this script again.
    echo.
    pause
    exit /b 1
)

:: Push to GitHub
echo Pushing to GitHub...
git push -u origin main

echo.
echo ==========================================
echo  DONE! Now enable GitHub Pages:
echo ==========================================
echo.
echo 1. Go to your repo on github.com
echo 2. Settings ^> Pages
echo 3. Source: Deploy from branch
echo 4. Branch: main / root
echo 5. Save
echo.
echo Your site will be live at:
echo   https://YOUR_USERNAME.github.io/omniseedai.com
echo.
echo Then set custom domain to: omniseedai.com
echo.
pause
