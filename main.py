##pip install colorama requests urlib3 wmi

import urllib3
urllib3.disable_warnings()

import requests

from colorama import init as coloramainit
from colorama import Fore, Back, Style
coloramainit()
"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""

import LauncherInfo






headers = {
    'Accept' : 'application/json'
}

def rqget(url, headers):
    url='https://127.0.0.1:52571'+url
    return requests.get(url, headers=headers, verify=False)
def rqpost(url, headers):
    url='https://127.0.0.1:52571'+url
    return requests.post(url, headers=headers, verify=False)

def CheckLauncherScale():
    LauncherScale = rqget('/riotclient/zoom-scale', headers)
    LauncherScale.json
    if LauncherScale.text == '1.25':
        return Fore.GREEN + 'OK'
    else:
        rqpost('/riotclient/zoom-scale?newZoomScale=1.25', headers)
        return Fore.YELLOW + 'Fixed'
        


#print('Launcher Size: ['+ CheckLauncherScale() + Fore.RESET + ']')
a = requests.get("https://127.0.0.1:53725/riotclient/zoom-scale", auth=('riot', 'a8VqRTIPF00aodgbmyEtkg'), headers=headers, verify=False).text
print(a)