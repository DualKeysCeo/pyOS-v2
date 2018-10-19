import os
from time import sleep
from sysops import login
from textwrap import wrap
from operations.ops import mainOps
from termcolor import colored, cprint
from sysops.termInfo import termCols

global user
global password
global userI
global passwordI

version = "2.2"
cs = "Coming soon"

def mainOS():
    clear()
    cprint("PyOS v" + version, "magenta")
    cprint("Copyright DualKeys Inc. 2017-2018.", "magenta")
    mainOps()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    clear()
    login.login()
    while True:
        mainOS()
