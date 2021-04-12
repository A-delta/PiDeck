@echo off
cls
echo Please check you have granted administrative permissions.
echo Press any key to continue...
pause > nul
cls
echo Please wait...

reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayName /t REG_SZ /d "RaspiMote" > nul
reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayIcon /t REG_SZ /d "C:\Program Files\RaspiMote\driver\driver\lan_server\ui\RaspiMote_logo.ico" > nul
reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v DisplayVersion /t REG_SZ /d "1.0.0" > nul
reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v Publisher /t REG_SZ /d "RaspiMote" > nul
reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v HelpLink /t REG_EXPAND_SZ /d "https://raspimote.tk/" > nul
reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v InstallLocation /t REG_SZ /d "C:\Program Files\RaspiMote" > nul
reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v InstallSource /t REG_SZ /d "C:\Program Files\RaspiMote\install.cmd" > nul
reg.exe add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RaspiMote /v UninstallString /t REG_SZ /d "C:\Program Files\RaspiMote\uninstall.cmd" > nul

cls
echo RaspiMote is registered in the Windows Registry!
echo Press any key to exit...
pause > nul
exit