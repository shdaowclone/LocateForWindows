#LocateForWindows
#Made by Shadowclone
#Link https://github.com/shdaowclone/LocateForWindows

This is an Alternative for Linux locate for windows
Fast search for file location

The pre-compiled version was compiled using "pyinstaller", If added to "Windows" folder it can be used directly from CMD or Powershell

For first run it will gather all File location into a SQLite database (to gather 1.5M file location it can take up to 3 minutes)
It's tested on Windows 10, but should work with any windows version

Usage: locate name_of_file

To update the database run "locate -refill_database"
