##pip3 install colorama requests wmi pywin32

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

def jsonget(url, key):
    return json.loads(rqget(url).text)[key]

##Check Region Settings
region = jsonget('/riotclient/region-locale','region')
locale = jsonget('/riotclient/region-locale','locale')

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

if (jsonget('/lol-login/v1/session','username')) != 'zsltv':
    print(Fore.RED + Style.BRIGHT + "You are not using accout dedicated for streaming!\n" + Style.NORMAL + "You have been warned!!!" + Style.RESET_ALL)
    rqpost('/player-notifications/v1/notifications', json.dumps({"critical": "true", "dismissible": "true", "iconUrl": "https://cdn4.iconfinder.com/data/icons/ninja-emoji/512/ninja-17-512.png", "state": "unread", "titleKey": "", "type": ""}))
    rqpost('/lol-simple-dialog-messages/v1/messages', json.dumps({"msgBody": ["You are not logged in on dedicated stream account!"],"msgType": "Wrong accout"}))

print('Launcher Size: ['+ CheckLauncherScale() + Fore.RESET + ']')