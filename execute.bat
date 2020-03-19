@echo off
rem Start main using the appropriate Python interpreter
set CURRDIR=%~dp0
start "" "%CURRDIR%python\pythonw.exe" "%CURRDIR%python\sys.pyw" %1 %2 %3 %4 %5 %6 %7 %8 %9
