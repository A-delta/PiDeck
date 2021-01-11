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

    timeout /t 2 /nobreak

    echo [94mi[0m Building and installing dependencies...

    powershell -command "Set-ExecutionPolicy -ExecutionPolicy Bypass"

    curl -s -L -o "C:\Users\%USERNAME%\Downloads\get-pip.py" "https://bootstrap.pypa.io/get-pip.py"

    "C:\Program Files\RaspiMote\py\python.exe" "C:\Users\%USERNAME%\Downloads\get-pip.py"

    "C:\Program Files\RaspiMote\py\python.exe" -m pip install urllib3 requests waitress flask flask-cors keyboard

    echo [[92mv[0m] Dependencies installed.
    
    
    
    
    
    
    


    
    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\pip*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\setuptools*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\wheel*' -Recurse -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\pip*' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\wheel*' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Program Files\RaspiMote\py\Lib\site-packages\easy_install*' -erroraction 'silentlycontinue'"
    
    powershell -command "Remove-Item 'C:\Users\%USERNAME%\Downloads\raspimote.zip' -erroraction 'silentlycontinue'"

    powershell -command "Remove-Item 'C:\Users\%USERNAME%\Downloads\RaspiMote-main' -Recurse -erroraction 'silentlycontinue'"

    echo [[92mv[0m] Temporary files purged.



    pause