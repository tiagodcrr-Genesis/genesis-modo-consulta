@echo off
echo ============================================
echo   GENESIS — MODO CONSULTORIA
echo   Abrindo no navegador...
echo ============================================
echo.
cd /d "%~dp0"
streamlit run interface_genesis.py --server.headless false
pause
