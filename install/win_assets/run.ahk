Menu, Tray, NoStandard 
Menu, Tray, Add, Exit, ByeScript 
Menu, Tray, Default, Exit 

#Persistent
Menu, tray, Tip, RaspiMote

RunWait %comspec% /c "C:\Program Files\RaspiMote\init.cmd",,Hide

OnExit("ExitFunc")
ExitFunc(ExitReason, ExitCode)
{
    RunWait %comspec% /c "C:\Windows\System32\taskkill.exe /f /im pythonw.exe",,Hide
    RunWait %comspec% /c "C:\Windows\System32\taskkill.exe /f /im cmd.exe",,Hide
}

ByeScript: 
  RunWait %comspec% /c "C:\Windows\System32\taskkill.exe /f /im pythonw.exe",,Hide
  RunWait %comspec% /c "C:\Windows\System32\taskkill.exe /f /im cmd.exe",,Hide
  ExitApp 
Return