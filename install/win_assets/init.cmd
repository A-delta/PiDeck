@echo off

cd "C:\Program Files\RaspiMote\driver"

mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( 'Message!', 10, 'Title!', 64 );close()"

Rem "C:\Program Files\RaspiMote\py\pythonw.exe" main.py