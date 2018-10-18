import os
import __main__
from termcolor import colored, cprint
from operations.bulletins import BaseBulletins

item1 = "\t"

bulletins = BaseBulletins()

def mainOps():
    while True:
        choice = ask()
        selected_builtin = bulletins.get_builtin(choice)
        if selected_builtin is not None:
            selected_builtin()
        ##else if lookup_path ?
        ##    pass
        else:
            cprint("That is not a function. Type help or list for a list of commands", "red")

def ask():
    choice = input(colored("pyOS> ", "white"))
    choice = choice.lower()
    return choice