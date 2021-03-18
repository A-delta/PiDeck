powershell -command "Copy-Item 'C:\Program Files\RaspiMote\driver\driver\lan_server\built_in_fcn\nircmd.exe' '%LOCALAPPDATA%\Temp' -erroraction 'silentlycontinue'"

"%LOCALAPPDATA%\Temp\nircmd.exe" elevate "C:\Program Files\RaspiMote\rm.cmd"
