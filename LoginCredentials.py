"""
Create file account.txt
In first line put username
in second line put password
"""
from colorama import Fore, Back, Style

try:
    CredientalsFile = open("account.txt", "r")
    
    user = str.strip(CredientalsFile.readline())
    passwd = str.strip(CredientalsFile.readline())

    if (user == '') or (passwd == ''):
        raise FileNotFoundError

    CredientalsFile.close()                #Make memory FREE! :D 
except(FileNotFoundError):
    print(Fore.YELLOW + "File with login informations not found!\n" + Fore.RESET)
    CredientalsFile = open("account.txt", "w")

    user = input("Please enter username: ")
    CredientalsFile.writelines(user+"\n")
    passwd = input("Please enter password: ")
    CredientalsFile.writelines(passwd)

    CredientalsFile.close

data = {"password": passwd,"username": user}