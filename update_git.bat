@echo off
echo ==========================================
echo Updating GitHub Repository...
echo ==========================================

echo Pulling latest changes from GitHub...
git pull origin main --no-edit

echo.
echo Adding files...
git add .

echo Committing changes...
git commit -m "Improved app structure, added utils and tests"

echo Pushing to GitHub...
git push origin main

echo.
if %errorlevel% equ 0 (
    echo ==========================================
    echo Success! Your project is updated.
    echo ==========================================
) else (
    echo ==========================================
    echo Something went wrong. Please check the error above.
    echo ==========================================
)

pause
