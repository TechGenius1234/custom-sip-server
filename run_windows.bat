@echo off
echo Starting Custom SIP Server Setup...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed! Please install Python from https://www.python.org/
    pause
    exit /b
)

echo Installing dependencies...
pip install sippy flask twisted
if %errorlevel% neq 0 (
    echo Failed to install dependencies. Please check your internet connection.
    pause
    exit /b
)

echo Starting SIP Server...
python main.py
pause
