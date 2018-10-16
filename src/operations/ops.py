import os
import __main__
from textwrap import wrap
from sysops import login, termInfo
from termcolor import colored, cprint
from operations import credentials, maths, files, directories

item1 = "\t"

Math = maths.Math
Files = files.Files
Directories = directories.Directories

operations = [
    "hello",
    "changecreds",
    "math.add",
    "math.subtract",
    "math.multiply",
    "math.divide",
    "files.make",
    "files.open",
    "files.delete",
    "directory.make",
    "directory.delete",
    "ls",
    "back",
    "clear",
    "exit"
]

def mainOps():
    choice = input(colored("pyOS> ", "white"))
    choice = choice.lower()

    if choice == operations[0]:
        print("Hello world")
    elif choice == operations[-3]:
        __main__.mainOS()
    elif choice == operations[-2]:
        os.system("cls")
        for i in wrap("    ".join(operations), width=termInfo.termCols() * (2.0/3.0)):
            cprint(i, "cyan")
        mainOps()
    elif choice == operations[-1]:
        login.logout()
    elif choice == operations[1]:
        user = input("\tWhat is your new username? ")
        password = input("\tWhat is your new password? ")
        credentials.change(user, password)
        os.system("cls")
        login.login()
    elif choice == operations[2]:
        Math.add(Math, "\t\t")
    elif choice == operations[3]:
        Math.subtract(Math, "\t\t")
    elif choice == operations[4]:
        Math.multiply(Math, "\t\t")
    elif choice == operations[5]:
        Math.divide(Math, "\t\t")
    elif choice == operations[6]:
        Files.make(Files, "\t\t")
    elif choice == operations[7]:
        Files.use(Files, "\t\t")
    elif choice == operations[8]:
        Files.delete(Files, "\t\t")
    elif choice == operations[9]:
        Directories.make(Directories, "\t\t")
    elif choice == operations[10]:
        Directories.delete(Directories, "\t\t")
    elif choice == operations[-5]:
        Files.listF(Files, "\t\t")
    else:
        cprint("No such operation", "red")
    mainOps()