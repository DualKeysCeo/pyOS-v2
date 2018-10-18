import os
from time import sleep
from sysops import login
from textwrap import wrap
from operations.ops import mainOps, ask
from termcolor import colored, cprint
from sysops.termInfo import termCols

global user
global password
global userI
global passwordI

cs = "Coming soon"

def mainOS():
    os.system("cls")
    cprint("PyOS v2", "magenta")
    cprint("Copyright DualKeys Inc. 2017-2018. All rights reserved", "magenta")
    mainOps()


if __name__ == "__main__":
    os.system("cls")
    login.login()
    os.system("cls")
    while True:
        mainOS()