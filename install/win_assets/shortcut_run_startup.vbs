Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\RaspiMote.LNK"
Set oLink = oWS.CreateShortcut(sLinkFile)
    oLink.TargetPath = "C:\Program Files\RaspiMote\RaspiMote.exe"
    oLink.Description = "Run RaspiMote driver."
oLink.Save