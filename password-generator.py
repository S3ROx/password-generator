#!/usr/bin/python
#
#       S3RO PASSWORD GENERATOR v1.0
#       
#       Created By : S3RO
#       GitHub : https://github.com/S3ROx
#       
#       Disclaimer : Educational Purpose only

import random
import colorama
from colorama import Fore
import time
import os
import sys

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
characters_total = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!£$%&/()=?^[]€<>#+-*"


colorama.init(autoreset=True)

banner = f"""{Fore.CYAN}
██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

{Fore.YELLOW}
<==================== Option List - By S3RO ====================>
    [1] Letters Only                        [2] Alpha Numeric
    [3] Alpha Numeric + Simbols             [4] Coming Soon!
    [5] Comin Soon!                         [6] Coming Soon!
    [q] Quit
"""

print(banner)

def quit():
    print(Fore.BLUE + "Thanks for using S3RO's Password Generator!. Goodbye")
    sys.exit()

def mainMenu():
    print(Fore.BLUE + "Thanks for using S3RO's Password Generator!. Goodbye")
    os.system("python3 s3ro_tools.py")
    sys.exit()

def quitting():
    quittingChoose = input(f"{Fore.YELLOW}Do you want to return to the main menu? (y/n)>: ").lower()
    if quittingChoose == "y":
            mainMenu()
    else:
        quit()

def genNormalPass():
    len = int(input("Password's lenght>: "))
    psw = ""

    for x in range(len):
        psw += random.choice(letters)
    
    print("Generated password:", psw)

def genAlphaNumPass():
    len = int(input("Password's lenght>: "))
    psw = ""

    for x in range(len):
        psw += random.choice(letters_numbers)
    
    print("Generated password:", psw)

def genStrongPass():
    len = int(input("Password's lenght>: "))
    psw = ""

    for x in range(len):
        psw += random.choice(characters_total)
    
    print("Generated password:", psw)

loop = True

while loop:
    choose = input(f"{Fore.YELLOW}Select an option>: ")

    if choose == "q":
        quitting()

    elif choose == "1":
        genNormalPass()

    elif choose == "2":
        genAlphaNumPass()

    elif choose == "3":
        genStrongPass()

    else:
        print(f"{Fore.RED}\nPlease choose an option from the list.\n")
        time.sleep(1)
        print(banner)
    
    loop = input(f"{Fore.YELLOW}Do you want to generate another password? (y/n)>: ").lower()

    if loop == "y":
        continue
    else:
        loop = False
        quitting()
