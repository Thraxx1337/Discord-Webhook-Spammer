from ast import While
from distutils.log import error
from pickle import TRUE
from tokenize import Double
from urllib import request, response
from colorama import Fore, init
import sys
import time
from os import system
import requests


system("title " + "Discord WebHook Spammer,   Made By Thraxx#1402,   Discord: https://discord.gg/49YAGUEcMf")


print(Fore.LIGHTCYAN_EX + """
     _    _      _     _                 _      _____                                           
    | |  | |    | |   | |               | |    /  ___|                                          
    | |  | | ___| |__ | |__   ___   ___ | | __ \ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
    | |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /  `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|""" + Fore.LIGHTBLUE_EX + """
    ------------------------------------Made by Thraxx#1402----------------------------------- """ + Fore.LIGHTCYAN_EX + """
     \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                    | |                                        
                                                    |_|                                    
------------------------------------------------------------------------------------------------------
""")

du = input(Fore.LIGHTBLUE_EX + "Enter ur Discord Webhook url: ")
dn = input("What do you want the Webhook's username to be: ")
ms = input("What's the msg you want it to spam: ")
dm = input("What's the delay between msg's: ")
sa = int(input("How many msg's you want it to spam (enter 0 for ∞): "))

dmf = float(dm)
discord_webhook_url = du

discord_webhook_url = du
num = 0

if sa == 0:
    while True:
        Message = {
            "content": ms
        }
        result = requests.post(discord_webhook_url, data={"username": dn, "content": ms})
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(Fore.RED + "Rate limited Please wait! (est 45s)")
            print(Fore.LIGHTCYAN_EX + "---------------------------------------------------------------------------")
        else:
            print(Fore.GREEN + "["+ str(num) +"] Your message (" + ms + ") has successfully been sent to the Webook!")
            print(Fore.LIGHTCYAN_EX + "---------------------------------------------------------------------------")
            num +=1 
        time.sleep(dmf)

for i in range(sa):
        Message = {
            "content": ms
        }
        result = requests.post(discord_webhook_url, data={"username": dn, "content": ms})
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(Fore.RED + "Rate limited Please wait! (est 45s)")
            print(Fore.LIGHTCYAN_EX + "---------------------------------------------------------------------------")
        else:
            print(Fore.GREEN + "["+ str(num) +"] Your message (" + ms + ") has successfully been sent to the Webook!")
            print(Fore.LIGHTCYAN_EX + "---------------------------------------------------------------------------")
            num +=1 
        time.sleep(dmf)







