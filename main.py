### DEPENCIES ###
##pip3 install urllib3 colorama requests wmi pywin32

### CONFIGURATION ###
AutoLogin = True
UseRemote = False
GetCredientalsFromLocal = True
GetCredientalsFromRemote = False
RemoteMachineIP = "192.168.1.124"
LeagueClientIP = "127.0.0.1"
LeagueClientPort = ""
Login = 'riot'
Password = ''

## VARS
LeagueClientAdress = LeagueClientIP + ":" + str(LeagueClientPort)
LeagueClientURL = "https://"+LeagueClientAdress

def UpdateLeagueClientURL():
    global LeagueClientAdress
    global LeagueClientURL
    LeagueClientAdress = LeagueClientIP + ":" + LeagueClientPort
    LeagueClientURL = "https://"+LeagueClientAdress

## VARS for Requests
headers = {
    "Accept" : "application/json"
}
if UseRemote == True:
    proxies = {
    "https": "http://"+RemoteMachineIP+":808"
    }
else:
    proxies = None


#Disable insecure connection warning
import urllib3
urllib3.disable_warnings()

#Import Important stuff
import requests
import json
import sys
import socket
import time
from colorama import init as coloramainit
from colorama import Fore, Back, Style
coloramainit()

if GetCredientalsFromRemote == True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    server = RemoteMachineIP
    port = 25565
    s.connect((server, port))                               
    msg = s.recv(1024)
    s.close()

    credientals = json.loads(msg.decode('utf-8'))

    LeagueClientPort = str(credientals['Port'])
    Password = credientals['Password']
    UpdateLeagueClientURL()

    LastCredientalsFile = open("lastportpass.txt", "w")
    LastCredientalsFile.write(LeagueClientPort+"\n")
    LastCredientalsFile.write(Password)
    LastCredientalsFile.close

elif GetCredientalsFromLocal == True:
    import LauncherInfo

    LeagueClientPort = LauncherInfo.Credentials.Port
    Password = LauncherInfo.Credentials.Pass

    UpdateLeagueClientURL()



else: #GET LOCAL VALUES

    LastCredientalsFile = open("lastportpass.txt", "r")
    LeagueClientPort = str.strip(LastCredientalsFile.readline())
    Password = str.strip(LastCredientalsFile.readline())
    LastCredientalsFile.close()
    UpdateLeagueClientURL()
    #print(Fore.RED + "Cannot find informations about connection to League of Legends Launcher. Exiting..." + Fore.RESET)


#Create session
s = requests.Session()
s.auth = (Login, Password)
s.headers = headers
s.verify = False
s.proxies = proxies



def rqget(url):
    return s.get(LeagueClientURL+url)
def rqpost(url, data = None):
    return s.post(LeagueClientURL+url, data=data)
def rqpatch(url, data = None):
    return s.patch(LeagueClientURL+url, data=data)

def jsonget(url):
    return json.loads(rqget(url).text)

def jsongetkey(url, key = None):
    return json.loads(rqget(url).text)[key]

##Check Region Settings
region = jsongetkey('/riotclient/region-locale','region')
locale = jsongetkey('/riotclient/region-locale','locale')

if (region != 'EUNE') or (locale != 'en_GB'):
    print(Fore.YELLOW + "Wrong Region or Locale. Trying to change it to EUNE/English" + Fore.RESET)
    rqpost('/riotclient/set_region_locale?region=EUNE&locale=en_GB')
    print('Region and Language: ['+ Fore.YELLOW + 'Fixed' + Fore.RESET + ']')
else:
    print('Region and Language: ['+ Fore.GREEN + 'OK' + Fore.RESET + ']')

def CheckLauncherScale():
    LauncherScale = rqget('/riotclient/zoom-scale')
    if LauncherScale.text == '1.25':
        return Fore.GREEN + 'OK'
    else:
        rqpost('/riotclient/zoom-scale?newZoomScale=1.25')
        return Fore.YELLOW + 'Fixed'

if (rqget('/lol-login/v1/session').status_code) == 404:
    import LoginCredentials
    rqpost('/lol-login/v1/session', json.dumps(LoginCredentials.data))

if (jsongetkey('/lol-login/v1/session','username')) != 'zsltv':
    print("Account: [" + Fore.RED + "ERROR" + Fore.RESET + "]")
    print(Fore.RED + Style.BRIGHT + "You are not using accout dedicated for streaming!\n" + Style.NORMAL + "You have been warned!!!" + Style.RESET_ALL)
else:
    print("Account:             [" + Fore.GREEN + "OK" + Fore.RESET + "]")
summonerId = jsongetkey('/lol-login/v1/session', 'summonerId')

print('Launcher Size:       ['+ CheckLauncherScale() + Fore.RESET + ']')

### CHAMPIONS AND SKINS VARS ###

AllChampionsDictionary = rqget("/lol-champions/v1/inventories/" + str(summonerId) + "/champions").json()


###Saving champion image to folder, selected by ID

#AllChamps = rqget("/lol-champions/v1/inventories/" + str(summonerId) + "/champions").json()
def SelectChampion(id):
    for champ in AllChampionsDictionary:
        if (champ['id']) == id:
            return champ

def ChampionTileURL(ChampID, skinID = 0):
    return SelectChampion(ChampID)['skins'][skinID]['tilePath']

def ChampionTileImage(ChampID, skinID = 0):
    return rqget(ChampionTileURL(ChampID, skinID)).content

def SaveTile(filename, ChampID, skinID = 0):
    open('obs/'+filename+'.jpg', 'wb').write(ChampionTileImage(ChampID, skinID))

#countChamps = 0
#ChampID = showchamp()['actions'][countChamps][0]['championId']
#open('obs/Champ1.jpg', 'wb').write(rqget(ChampionTileURL(ChampID)).content)

"""

while True:
    banchamps(countChamps)
    if showchamp()['actions'][countChamps][0]['completed'] == True:
        open('obs/1.jpg', 'wb').write(rqget(ChampionTileURL(0)).content)
"""

### BANNING PHASE ###

while True:
    Session = rqget('/lol-champ-select/v1/session').json()
    AllActions = rqget('/lol-champ-select/v1/session').json()["actions"][1]
    LastAction = AllActions[-1][0]
    
    if LastAction["type"] == "ban":
        if LastAction["championId"] == 0:
            pass
        else:
            SaveTile("ban"+str(LastAction["pickTurn"]), LastAction["championId"])




###### TO DO
##### Lobby


#### Chamption Select
### AfterMatch Stats