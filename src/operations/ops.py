import os
import __main__
from termcolor import colored, cprint
from operations.built_in import BaseBuilt_Ins

item1 = "\t"

built_ins = BaseBuilt_Ins()

def mainOps():
    while True:
        choice = ask()
        selected_builtin = built_ins.get_builtin(choice)
        if selected_builtin is not None:
            selected_builtin()
        else:
            cprint("That is not a function. Type help or list for a list of commands", "red")

def ask():
    choice = input(colored("pyOS> ", "white"))
    choice = choice.lower()
    return choice