@echo off
cls
echo [95mRaspiMote - version 0.1 beta[0m
echo(
echo(

goto check_Permissions


:check_Permissions
    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo [[92mv[0m] Administrative permissions granted.
    ) else (
        echo [[91mx[0m] [91mYou must grant administrative permissions to the script.[0m
        pause >nul
        exit
    )

:main
    powershell -command "Set-ExecutionPolicy -ExecutionPolicy Bypass"

    curl -s -L -o raspimote.zip "https://github.com/A-delta/RaspiMote/archive/main.zip"

    echo [[92mv[0m] RaspiMote code downloaded.

    powershell -command "Remove-Item .\RaspiMote-main\ -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Add-Type -A 'System.IO.Compression.FileSystem';[IO.Compression.ZipFile]::ExtractToDirectory('.\raspimote.zip', '.')"

    echo [[92mv[0m] RaspiMote code extracted.

    pause