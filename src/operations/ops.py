import os
import __main__
from textwrap import wrap
from sysops import login, termInfo
from termcolor import colored, cprint
from operations import credentials, maths, files, directories

item1 = "\t"

Files = files.Files
Directories = directories.Directories

operations = [
    "hello",
    "changecreds",
    "math",
    "file",
    "directory",
    "ls",
    "clear",
    "exit"
]

def mainOps():
    choice = ask()
    if choice == operations[0]:
        print("Hello world")
    elif choice == operations[-1]: # logout
        login.logout()
    elif choice == operations[-2]: # clear
        os.system("cls")
    elif choice == operations[-3]: # lists files
        files.Files.listF(Files, "\t\t")
    elif choice == operations[1]:
        user = input("\tWhat is your new username? ")
        password = input("\tWhat is your new password? ")
        credentials.change(user, password)
        os.system("cls")
        login.login()
    elif choice == operations[2]:
        maths.choose()
    elif choice == operations[3]:
        files.choose()
    elif choice == operations[4]:
        directories.choose()
    elif choice == "help" or choice == "list":
        list()
    else:
        cprint("That is not a function. Type help or list for a list of commands", "red")
    mainOps()

def list():
    for i in wrap("    ".join(operations), width=termInfo.termCols() * (2.0/3.0)):
        cprint(i, "cyan")

def ask():
    choice = input(colored("pyOS> ", "white"))
    choice = choice.lower()
    return choice