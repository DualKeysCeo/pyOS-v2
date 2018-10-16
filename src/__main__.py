import os
from time import sleep
from textwrap import wrap
from login import login, logout
from termcolor import colored, cprint
from operations import ops
from termInfo import termCols

global user
global password
global userI
global passwordI

cs = "Coming soon"

def mainOS():
    os.system("cls")
    cprint("PyOS v2", "magenta")
    cprint("Copyright DualKeys Inc. 2017-2018. All rights reserved", "magenta")
    # ? Prints functions
    for i in wrap("    ".join(ops.operations), width=termCols() * (2.0/3.0)):
        cprint(i, "cyan")
    while True:
        ops.mainOps()
    choice = input(colored("pyOS> ", "white"))
    if choice.lower() == "logout" or choice.lower() == "log out":
        os.system("cls")
        logout()
    else:
        cprint("No such operation", "red")

if __name__ == "__main__":
    os.system("cls")
    login()
    os.system("cls")
    while True:
        mainOS()