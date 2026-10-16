@echo off
setlocal
cd /d "%~dp0"
echo === HealthCar first-time setup ===
where py >nul 2>nul
if %errorlevel%==0 (
  py -m venv .venv
) else (
  python -m venv .venv
)
if errorlevel 1 goto failed
.venv\Scripts\python.exe -m pip install --upgrade pip
if errorlevel 1 goto failed
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto failed
.venv\Scripts\python.exe scripts\download_data.py
if errorlevel 1 goto failed
.venv\Scripts\python.exe scripts\run_audit.py --dataset both
if errorlevel 1 goto failed
echo DONE. Open notebooks using OPEN_NOTEBOOKS_WINDOWS.bat
pause
exit /b 0
:failed
echo Setup/download/audit failed. See docs\dataset_feasibility.md for manual source links.
pause
exit /b 1
