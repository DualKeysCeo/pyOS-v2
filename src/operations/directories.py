import os
from textwrap import wrap
from sysops import termInfo
from termcolor import colored, cprint

class Directories:
    def make(self, indent):
        try:
            dirname = input(str(indent) + "What directory would you like to make? ")
            os.mkdir(os.path.dirname(__file__) + "\\..\\..\\Files\\" + dirname)
        except:
            cprint("There was an error while making this directory, it may already exist", "red")
    
    def delete(self, indent):
        dirname = input(str(indent) + "What directory would you like to delete? ")
        try:
            os.rmdir(os.path.dirname(__file__) + "\\..\\..\\Files\\\'" + dirname + "\'")
        except:
            cprint("Please empty the directory first", "red")

dirOps = [
    "make",
    "delete"
]

def choose():
    for i in wrap("    ".join(dirOps), width=termInfo.termCols() * (2.0/3.0)):
        cprint(i, "cyan")

    choice = input(colored("pyOS/operations/file> ", "white"))
    choice = choice.lower()

    if choice == dirOps[0]:
        Directories.make(Directories, "\t\t")
    elif choice == dirOps[1]:
        Directories.delete(Directories, "\t\t")
    else:
        cprint("That is not a function. Type help or commands for a list of commands", "red")