@echo off
echo ==========================================
echo Setting up Emotion Detection System...
echo ==========================================

echo Attempting to install dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] 'pip' command failed. 
    echo If you are using Anaconda, make sure to run this script from the "Anaconda Prompt".
    echo.
)

echo.
echo ==========================================
echo Starting Streamlit App...
echo ==========================================
streamlit run app.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to run Streamlit app.
    echo Please ensure you have installed the requirements and are in the correct environment.
)

pause
