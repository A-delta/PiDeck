@echo off
cls
echo [95mRaspiMote - version 1.0.0[0m
echo [95m!!! This installer only works on Windows 10 1706+ !!![0m
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

    echo(

    echo Press any key to continue installation...

    pause >nul

    cls

    echo [95mRaspiMote - version 1.0.0[0m

    echo(

    echo(

    C:
    
    cd C:\Windows\System32

    powershell -command "mkdir '%LOCALAPPDATA%\Temp\RaspiMote' -erroraction 'silentlycontinue' | Out-Null"

    curl -s -L -o "%LOCALAPPDATA%\Temp\RaspiMote\raspimote.zip" "https://github.com/A-delta/RaspiMote/archive/main.zip"

    echo [[92mv[0m] RaspiMote code downloaded.

    powershell -command "Remove-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\RaspiMote - driver.vbs' -erroraction 'silentlycontinue'"
    
    powershell -command "Add-Type -A 'System.IO.Compression.FileSystem';[IO.Compression.ZipFile]::ExtractToDirectory('%LOCALAPPDATA%\Temp\RaspiMote\raspimote.zip', '%LOCALAPPDATA%\Temp\RaspiMote\')"

    echo [[92mv[0m] RaspiMote code extracted.

    powershell -command "mkdir 'C:\Program Files\RaspiMote' -erroraction 'silentlycontinue' | Out-Null"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\driver' 'C:\Program Files\RaspiMote\' -recurse -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\logo' 'C:\Program Files\RaspiMote\' -recurse -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\ui' 'C:\Program Files\RaspiMote\' -recurse -erroraction 'silentlycontinue'"

    powershell -command "mkdir 'C:\Program Files\RaspiMote\py' -erroraction 'silentlycontinue' | Out-Null"

    powershell -command "mkdir 'C:\Users\%USERNAME%\AppData\Roaming\RaspiMote' -erroraction 'silentlycontinue' | Out-Null"

    powershell -command "mkdir 'C:\Users\%USERNAME%\AppData\Roaming\RaspiMote\tmp' -erroraction 'silentlycontinue' | Out-Null"

    powershell -command "mkdir 'C:\Users\%USERNAME%\AppData\Roaming\RaspiMote\custom_fcn' -erroraction 'silentlycontinue' | Out-Null"

    echo [[92mv[0m] RaspiMote code copied to installation folder.

    if %PROCESSOR_ARCHITECTURE% == AMD64 (
        curl -s -L -o "%LOCALAPPDATA%\Temp\RaspiMote\python_embeddable.zip" "https://www.python.org/ftp/python/3.9.2/python-3.9.2-embed-amd64.zip"
    ) else (
        curl -s -L -o "%LOCALAPPDATA%\Temp\RaspiMote\python_embeddable.zip" "https://www.python.org/ftp/python/3.9.2/python-3.9.2-embed-win32.zip"
    )

    echo [[92mv[0m] Python embeddable environment downloaded.

    powershell -command "Add-Type -A 'System.IO.Compression.FileSystem';[IO.Compression.ZipFile]::ExtractToDirectory('%LOCALAPPDATA%\Temp\RaspiMote\python_embeddable.zip', 'C:\Program Files\RaspiMote\py')"
    
    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\python39._pth' -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\win_assets\python39._pth' 'C:\Program Files\RaspiMote\py' -erroraction 'silentlycontinue'"

    echo [[92mv[0m] Python embeddable environment extracted to installation folder.

    timeout /t 2 /nobreak > nul

    echo [[94mi[0m] Downloading, building and installing dependencies...

    powershell -command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned"

    curl -s -L -o "%LOCALAPPDATA%\Temp\RaspiMote\get-pip.py" "https://bootstrap.pypa.io/get-pip.py"

    "C:\Program Files\RaspiMote\py\python.exe" "%LOCALAPPDATA%\Temp\RaspiMote\get-pip.py" -q 1> nul 2> nul

    "C:\Program Files\RaspiMote\py\python.exe" -m pip install urllib3 requests flask flask-cors keyboard psutil jaraco.functools -q 1> nul 2> nul

    curl -s -L -o "%LOCALAPPDATA%\Temp\RaspiMote\raspimote_https.zip" "https://github.com/RaspiMote/https/archive/1.0.0.zip"
    
    powershell -command "Add-Type -A 'System.IO.Compression.FileSystem';[IO.Compression.ZipFile]::ExtractToDirectory('%LOCALAPPDATA%\Temp\RaspiMote\raspimote_https.zip', '%LOCALAPPDATA%\Temp\RaspiMote\')"

    cd "%LOCALAPPDATA%\Temp\RaspiMote\https-1.0.0"

    "C:\Program Files\RaspiMote\py\python.exe" setup.py install 1> nul 2> nul

    curl -s -L -o "%LOCALAPPDATA%\Temp\RaspiMote\idle.zip" "https://github.com/RaspiMote/bin/releases/download/1.0.0_bin/idle-windows-python39.zip"

    powershell -command "Add-Type -A 'System.IO.Compression.FileSystem';[IO.Compression.ZipFile]::ExtractToDirectory('%LOCALAPPDATA%\Temp\RaspiMote\idle.zip', 'C:\Program Files\RaspiMote\py')"

    cd C:\Windows\System32

    echo [[92mv[0m] Dependencies installed.
    
    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\win_assets\init.cmd' 'C:\Program Files\RaspiMote' -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\common_assets\custom_fcn.py' 'C:\Users\%USERNAME%\AppData\Roaming\RaspiMote\custom_fcn' -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\win_install.cmd' 'C:\Program Files\RaspiMote\install.cmd' -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\win_uninstall.cmd' 'C:\Program Files\RaspiMote\rm.cmd' -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\uninstaller_entrypoint.cmd' 'C:\Program Files\RaspiMote\uninstall.cmd' -erroraction 'silentlycontinue'"

    if %PROCESSOR_ARCHITECTURE% == AMD64 (
        curl -s -L -o "C:\Program Files\RaspiMote\RaspiMote.exe" "https://github.com/RaspiMote/bin/releases/download/1.0.0_bin/run-windows-amd64-1.0.0.exe"
        curl -s -L -o "C:\Program Files\RaspiMote\RaspiMote_UI.exe" "https://github.com/RaspiMote/bin/releases/download/1.0.0_bin/ui-windows-amd64-1.0.0.exe"
    ) else (
        curl -s -L -o "C:\Program Files\RaspiMote\RaspiMote.exe" "https://github.com/RaspiMote/bin/releases/download/1.0.0_bin/run-windows-x86-1.0.0.exe"
        curl -s -L -o "C:\Program Files\RaspiMote\RaspiMote_UI.exe" "https://github.com/RaspiMote/bin/releases/download/1.0.0_bin/ui-windows-x86-1.0.0.exe"
    )*

    echo [[92mv[0m] Entrypoint binaries installed.

    setlocal enableextensions enabledelayedexpansion

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\common_assets\Open_Sans_regular.ttf' '%WINDIR%\Fonts' -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\common_assets\Open_Sans_bold.ttf' '%WINDIR%\Fonts' -erroraction 'silentlycontinue'"

    reg.exe add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "Open Sans Regular (TrueType)" /t REG_SZ /d Open_Sans_regular.ttf /f

    reg.exe add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "Open Sans Bold (TrueType)" /t REG_SZ /d Open_Sans_bold.ttf /f

    powershell -command "Import-Certificate -FilePath '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\common_assets\raspimote_ca.pem' -CertStoreLocation Cert:\LocalMachine\Root"

    powershell -command "mkdir 'C:\Program Files\Mozilla Firefox\distribution' -erroraction 'silentlycontinue' | Out-Null"

    powershell -command "Copy-Item '%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\win_assets\policies.json' 'C:\Program Files\Mozilla Firefox\distribution' -erroraction 'silentlycontinue'"

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayName /t REG_SZ /d "RaspiMote" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayIcon /t REG_SZ /d "C:\Program Files\RaspiMote\driver\driver\lan_server\ui\RaspiMote_logo.ico" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayVersion /t REG_SZ /d "1.0.0" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v Publisher /t REG_SZ /d "A-delta & Firmin-Launay" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v HelpLink /t REG_EXPAND_SZ /d "https://raspimote.tk/" > nul

    powershell -Command "Get-Date -Format yyyyMMdd" > "C:\Users\%USERNAME%\AppData\Local\Temp\currentdate.tmp"

    set /p c_date=<"C:\Users\%USERNAME%\AppData\Local\Temp\currentdate.tmp"

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v InstallDate /t REG_SZ /d %c_date% > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v InstallLocation /t REG_SZ /d "C:\Program Files\RaspiMote" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v InstallSource /t REG_SZ /d "C:\Program Files\RaspiMote\install.cmd" > nul

    cd "C:\Program Files\RaspiMote"

    powershell -Command "$totalsize = [long]0;Get-ChildItem -File -Recurse -Force -ErrorAction SilentlyContinue | %% {$totalsize += $_.Length};[math]::Round($totalsize/1000)" > "C:\Users\%USERNAME%\AppData\Local\Temp\rspfoldersize.tmp"

    set /p folder_size=<"C:\Users\%USERNAME%\AppData\Local\Temp\rspfoldersize.tmp"

    cd C:\Windows\System32

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v EstimatedSize /t REG_DWORD /d %folder_size% > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v UninstallString /t REG_SZ /d "C:\Program Files\RaspiMote\uninstall.cmd" > nul

    echo [[92mv[0m] RaspiMote added in the Windows Registry for uninstall.

    powershell -command "mkdir 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\RaspiMote' -erroraction 'silentlycontinue' | Out-Null"

    cscript "%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\win_assets\shortcut_run_startmenu.vbs" >nul

    cscript "%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\win_assets\shortcut_ui_startmenu.vbs" >nul

    cscript "%LOCALAPPDATA%\Temp\RaspiMote\RaspiMote-main\install\win_assets\shortcut_run_startup.vbs" >nul

    echo [[92mv[0m] Shortcuts for running at startup and for the start menu created.

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\pip*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\setuptools*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\wheel*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\pip*' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\wheel*' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\easy_install*' -erroraction 'silentlycontinue'"
    
    powershell -command "Remove-Item '%LOCALAPPDATA%\Temp\RaspiMote' -Recurse -erroraction 'silentlycontinue'"

    echo [[92mv[0m] Temporary files purged.

    timeout /t 3

    cls
    
    echo [95mRaspiMote - version 1.0.0[0m

    echo(
    
    echo(
    
    echo [[92mv[0m] RASPIMOTE HAS BEEN SUCCESSFULLY INSTALLED.

    echo(

    echo [[94mi[0m] To access to the driver or to the web-based configuration UI, go to “RaspiMote”, in the start menu.

    echo [[94mi[0m] To uninstall the driver, you can simply use the Programs and features menu, in the Control panel.

    echo(
    
    echo(
    
    echo Press any key to exit...

    pause >nul
