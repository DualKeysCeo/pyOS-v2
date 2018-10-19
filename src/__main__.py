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
    os.system("cls")
    cprint("PyOS v" + version, "magenta")
    cprint("Copyright DualKeys Inc. 2017-2018.", "magenta")
    mainOps()


if __name__ == "__main__":
    try:
        os.system("cls")
    except:
        os.system("clear")
    login.login()
    while True:
        mainOS()