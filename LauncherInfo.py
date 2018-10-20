import wmi
import winreg

class LoLDirectory(object):
  LolDir = None #It's defined - less bugs
  try: #First check Windows Registry
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\WOW6432Node\Riot Games, Inc\League of Legends")
    LolDir = winreg.QueryValueEx(key, "Location")[0] #We need only first value from array
  except:
    print("League of Legends not found in registry! Trying to find info in process")
    try:
      Found = False
      for process in wmi.WMI().Win32_Process (name="LeagueClient.exe"):
        print("Process found! Trying to get it's path")
        if process.ExecutablePath:
          LolDir = process.ExecutablePath
          LolDir = LolDir.rsplit('\\', 7)[0] #remove file name from directory and move to main folder
          Found = True
        else:
          print("Cannot access process path information! (Launcher was probably launched as administrator or) ")
      if Found is False:
        print("Program is probably not launched")
    except:
      print("It didn't work. Asking user...")
  if LolDir is None:
    ##Ask user about dir, temporaly using hardcoded value
    LolDir = 'C:/Program Files/Riot Games/League of Legends'

  LolDir = LolDir.replace('\\', '/') #Linux-like slashes rulez!

class LauncherCredentials(object):
  Port = None
  Pass = None
  try:
    lockfile = open(LoLDirectory.LolDir + "/lockfile", "r") #Open 'lockfile' inside LoL Directory as read-only

    for line in lockfile: 
        fields = line.split(":")    #Split fields seperated by ":" in lockfile to array
        Port = fields[2]      #Port number is 3rd information in lockfile
        Pass = fields[3]      #and Password is 4th

    lockfile.close()                #Make memory FREE! :D 
  except(FileNotFoundError):
    print("File not Found! Launcher is not opened or can't access it's lockfile (maybe directory is wrong?) ")

print(LauncherCredentials.Pass)
print(LauncherCredentials.Port)