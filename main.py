##pip3 install urllib3 colorama requests wmi pywin32 

import urllib3
urllib3.disable_warnings()

import requests
import json
import sys

from colorama import init as coloramainit
from colorama import Fore, Back, Style
coloramainit()
"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""

import LauncherInfo
if (LauncherInfo.Credentials.Port is None) or (LauncherInfo.Credentials.Pass is None):
    print(Fore.RED + "Cannot find informations about connection to League of Legends Launcher. Exiting..." + Fore.RESET)
    sys.exit()

headers = {
    'Accept' : 'application/json'
}

def rqget(url):
    url='https://127.0.0.1:'+LauncherInfo.Credentials.Port+url
    return requests.get(url, headers=headers, auth=('riot', LauncherInfo.Credentials.Pass), verify=False)
def rqpost(url, data = None):
    url='https://127.0.0.1:'+LauncherInfo.Credentials.Port+url
    return requests.post(url, headers=headers, auth=('riot', LauncherInfo.Credentials.Pass), data=data, verify=False)
def rqpatch(url, data = None):
    url='https://127.0.0.1:'+LauncherInfo.Credentials.Port+url
    return requests.patch(url, headers=headers, auth=('riot', LauncherInfo.Credentials.Pass), data=data, verify=False)

def jsonget(url):
    return json.loads(rqget(url).text)

def jsongetkey(url, key = None):
    return json.loads(rqget(url).text)[key]

def ChampionTileURL(ChampID, skinID = 0):
    return AllChamps[ChampID]['skins'][skinID]['tilePath']

def showchamp():
    return jsonget('/lol-champ-select/v1/session')

def banchamps(greatInt):
    if rqget('/lol-champ-select/v1/session').status_code == 200:
        if showchamp()['actions'][greatInt][0]['completed'] == True:
            print("dupa")

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
        #rqpost('/riotclient/zoom-scale?newZoomScale=1.25')
        return Fore.YELLOW + 'Fixed'

if (rqget('/lol-login/v1/session').status_code) == 404:
    import LoginCredentials
    rqpost('/lol-login/v1/session', json.dumps(LoginCredentials.data))

if (jsongetkey('/lol-login/v1/session','username')) != 'zsltv':
    print("Account: [" + Fore.RED + "ERROR" + Fore.RESET + "]")
    print(Fore.RED + Style.BRIGHT + "You are not using accout dedicated for streaming!\n" + Style.NORMAL + "You have been warned!!!" + Style.RESET_ALL)
    rqpost('/player-notifications/v1/notifications', json.dumps({"critical": "true", "dismissible": "true", "iconUrl": "https://cdn4.iconfinder.com/data/icons/ninja-emoji/512/ninja-17-512.png", "state": "unread", "titleKey": "", "type": ""}))
    rqpost('/lol-simple-dialog-messages/v1/messages', json.dumps({"msgBody": ["You are not logged in on dedicated stream account!"],"msgType": "Wrong accout"}))
else:
    print("Account:             [" + Fore.GREEN + "OK" + Fore.RESET + "]")
summonerId = jsongetkey('/lol-login/v1/session', 'summonerId')

print('Launcher Size:       ['+ CheckLauncherScale() + Fore.RESET + ']')

##Launcehr Settings

import GameSettings
if (rqget('/lol-game-settings/v1/game-settings').json()) != GameSettings.conf:
    detectedconf = rqget('/lol-game-settings/v1/game-settings').text
    GameSettings.confbackup(detectedconf)
    rqpatch('/lol-game-settings/v1/game-settings', json.dumps(GameSettings.conf))
    print("Game Settings:       [" + Fore.YELLOW + "Fixed" + Fore.RESET + "]")
    print("Your Config probably didn't match our config, it has been overwritten please check it.")
    
else:
    print("Game Settings:       [" + Fore.GREEN + "OK" + Fore.RESET + "]")


###Saving champion image to folder, selected by ID
ChampID = 30
AllChamps = rqget("/lol-champions/v1/inventories/" + str(summonerId) + "/champions").json()

#open('obs/1.jpg', 'wb').write(rqget(ChampionTileURL(ChampID)).content)
countChamps = 0
ChampID = showchamp()['actions'][countChamps][0]['championId']
open('obs/Champ1.jpg', 'wb').write(rqget(ChampionTileURL(ChampID)).content)
"""

while True:
    banchamps(countChamps)
    if showchamp()['actions'][countChamps][0]['completed'] == True:
        open('obs/1.jpg', 'wb').write(rqget(ChampionTileURL(0)).content)
"""