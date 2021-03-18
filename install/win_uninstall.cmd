@echo off
cls
echo [95mRaspiMote uninstaller - version 1.0.0[0m
echo(
echo(

goto check_Permissions


:check_Permissions
    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo [[92mv[0m] Administrative permissions granted.
    ) else (
        echo "[[91mx[0m] [91mYou must grant administrative permissions to the script, (C:\Program Files\RaspiMote\rm.cmd).[0m"
        pause >nul
        exit
    )

:main

    echo(

    echo Press any key to uninstall...

    pause >nul

    cls

    echo [95mRaspiMote uninstaller - version 1.0.0[0m

    echo(

    echo(

    C:
    
    cd C:\Windows\System32

    powershell -command "Remove-Item 'C:\Users\%USERNAME%\AppData\Roaming\RaspiMote' -Recurse -erroraction 'silentlycontinue'"

    setlocal enableextensions enabledelayedexpansion

    powershell -command "Get-ChildItem Cert:\LocalMachine\Root | Where-Object { $_.Subject -match 'RaspiMote Certification Authority' } | Remove-Item"
    
    reg.exe delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /f > nul

    powershell -command "Remove-Item 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\RaspiMote' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\RaspiMote.LNK' -erroraction 'silentlycontinue'"
