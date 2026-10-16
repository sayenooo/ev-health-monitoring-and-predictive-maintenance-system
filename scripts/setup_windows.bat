@echo off
setlocal
cd /d "%~dp0\.."
echo HealthCar - environment setup
if not exist ".venv\Scripts\python.exe" (
  where py >nul 2>nul
  if %errorlevel%==0 (
    py -m venv .venv
  ) else (
    python -m venv .venv
  )
  if errorlevel 1 goto failed
)
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
echo.
echo Environment ready.
echo Run scripts\download_data.py to obtain the published datasets.
pause
exit /b 0
:failed
echo.
echo Setup failed. Check your Python installation and network connection.
pause
exit /b 1
