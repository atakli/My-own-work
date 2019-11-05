Set oShell = CreateObject("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c video2mp3.bat"
oShell.Run strArgs, 0, false