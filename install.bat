@echo off
REM PPT Finder Skill - Windows 安装脚本
echo.
echo ========================================
echo   PPT Finder Skill - 安装程序
echo ========================================
echo.

echo [1/5] Checking Python environment...
C:\Python314\python.exe --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found
    goto :error
)
echo [OK] Python environment ready
echo.

echo [2/5] Installing dependencies...
C:\Python314\python.exe -m pip install python-pptx
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    goto :error
)
echo [OK] Dependencies installed
echo.

echo [3/5] Checking configuration...
if not exist "%USERPROFILE%\Desktop\PPT集合" (
    echo Creating PPT directory...
    mkdir "%USERPROFILE%\Desktop\PPT集合"
)
echo [OK] Configuration ready
echo.

echo [4/5] Creating desktop shortcut...
copy "%~dp0ppt_finder.bat" "%USERPROFILE%\Desktop\ppt_finder.bat" >nul
echo [OK] Desktop shortcut created: %USERPROFILE%\Desktop\ppt_finder.bat
echo.

echo [5/5] Verifying installation...
if exist "%~dp0scripts\ppt_tool.py" (
    echo [OK] ppt_tool.py found
) else (
    echo ERROR: ppt_tool.py not found
    goto :error
)
echo [OK] Installation verified
echo.

echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo Quick Start:
echo   1. Open Command Prompt
echo   2. cd %USERPROFILE%\Desktop
echo   3. ppt_finder --build
echo   4. ppt_finder --search AI
echo.
echo Or use desktop shortcut: ppt_finder.bat
echo.
echo Documentation:
echo   - SKILL.md: Full documentation
echo   - README.md: Quick start guide
echo.
goto :end

:error
echo.
echo ERROR: Installation failed
echo Please check the error messages above
exit /b 1

:end
pause
