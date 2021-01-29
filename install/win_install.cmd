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

    curl -s -L -o "C:\Users\%USERNAME%\Downloads\raspimote.zip" "https://github.com/A-delta/RaspiMote/archive/main.zip"

    echo [[92mv[0m] RaspiMote code downloaded.

    powershell -command "Remove-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main\' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\RaspiMote - driver.vbs' -erroraction 'silentlycontinue'"
    
    powershell -command "Add-Type -A 'System.IO.Compression.FileSystem';[IO.Compression.ZipFile]::ExtractToDirectory('C:\Users\%USERNAME%\Downloads\raspimote.zip', 'C:\Users\%USERNAME%\Downloads\')"

    echo [[92mv[0m] RaspiMote code extracted.

    powershell -command "mkdir 'C:\Program Files\RaspiMote' -erroraction 'silentlycontinue' | Out-Null"

    powershell -command "Copy-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main\driver' 'C:\Program Files\RaspiMote\' -recurse -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main\logo' 'C:\Program Files\RaspiMote\' -recurse -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main\ui' 'C:\Program Files\RaspiMote\' -recurse -erroraction 'silentlycontinue'"

    powershell -command "mkdir 'C:\Program Files\RaspiMote\py' -erroraction 'silentlycontinue' | Out-Null"

    echo [[92mv[0m] RaspiMote code copied to installation folder.

    curl -s -L -o "C:\Users\%USERNAME%\Downloads\python_embeddable.zip" "https://www.python.org/ftp/python/3.9.1/python-3.9.1-embed-amd64.zip"

    echo [[92mv[0m] Python embeddable environment downloaded.

    powershell -command "Add-Type -A 'System.IO.Compression.FileSystem';[IO.Compression.ZipFile]::ExtractToDirectory('C:\Users\%USERNAME%\Downloads\python_embeddable.zip', 'C:\Program Files\RaspiMote\py')"
    
    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\python39._pth' -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main\install\win_assets\python39._pth' 'C:\Program Files\RaspiMote\py' -erroraction 'silentlycontinue'"

    echo [[92mv[0m] Python embeddable environment extracted to installation folder.

    timeout /t 2 /nobreak > nul

    echo [[94mi[0m] Downloading, building and installing dependencies...

    powershell -command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned"

    curl -s -L -o "C:\Users\%USERNAME%\Downloads\get-pip.py" "https://bootstrap.pypa.io/get-pip.py"

    "C:\Program Files\RaspiMote\py\python.exe" "C:\Users\%USERNAME%\Downloads\get-pip.py" -q 1> nul 2> nul

    "C:\Program Files\RaspiMote\py\python.exe" -m pip install urllib3 requests waitress flask flask-cors keyboard psutil -q 1> nul 2> nul

    echo [[92mv[0m] Dependencies installed.
    
    powershell -command "Copy-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main\install\win_assets\init.cmd' 'C:\Program Files\RaspiMote' -erroraction 'silentlycontinue'"

    powershell -command "Copy-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main\install\win_assets\RaspiMote - driver.vbs' 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp' -erroraction 'silentlycontinue'"
    
    

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayName /t REG_SZ /d "RaspiMote" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayIcon /t REG_SZ /d "C:\Program Files\RaspiMote\logo\RaspiMote_logo.ico" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayVersion /t REG_SZ /d "1.0" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v Publisher /t REG_SZ /d "A-delta & Firmin-Launay" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v HelpLink /t REG_EXPAND_SZ /d "https://docs.raspimote.tk/" > nul

    powershell -Command "Get-Date -Format yyyyMMdd" > "C:\Users\%USERNAME%\AppData\Local\Temp\currentdate.tmp"

    set /p c_date=<"C:\Users\%USERNAME%\AppData\Local\Temp\currentdate.tmp"

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v InstallDate /t REG_SZ /d %c_date% > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v InstallLocation /t REG_SZ /d "C:\Program Files\RaspiMote" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v InstallSource /t REG_SZ /d "C:\Program Files\RaspiMote\install.cmd" > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v EstimatedSize /t REG_DWORD /d 35840 > nul

    reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v UninstallString /t REG_SZ /d "C:\Program Files\RaspiMote\uninstall.cmd" > nul

    












    
    
    
    



    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\pip*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\setuptools*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\wheel*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\pip*' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\wheel*' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\easy_install*' -erroraction 'silentlycontinue'"
    
    powershell -command "Remove-Item 'C:\Users\%USERNAME%\Downloads\raspimote.zip' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Users\%USERNAME%\Downloads\get-pip.py' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main' -Recurse -erroraction 'silentlycontinue'"

    echo [[92mv[0m] Temporary files purged.



    pause