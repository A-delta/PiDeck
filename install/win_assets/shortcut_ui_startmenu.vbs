Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\RaspiMote\RaspiMote configuration UI.LNK"
Set oLink = oWS.CreateShortcut(sLinkFile)
    oLink.TargetPath = "C:\Program Files\RaspiMote\RaspiMote_UI.exe"
    oLink.Description = "Run RaspiMote configuration UI, to bind actions to buttons / potentiometers / keyboards / gamepads."
oLink.Save