import os
import sys
import subprocess
import __main__
from termcolor import colored, cprint
from operations.built_in import BaseBuilt_Ins
from multiprocessing import Process

item1 = "\t"

def find_exec_in_path(executable_name):
    executable_path =  os.getcwd()
    current_path = os.path.join(executable_path, executable_name)
    if os.path.isfile(current_path) and os.access(current_path, os.X_OK):
        return executable_name
    for path in os.environ["PATH"].split(os.pathsep):
        exe_file = os.path.join(path, executable_name)
        if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
            return exe_file
        else:
            for extension in os.environ["PATHEXT"].split(';'):
                tmp = exe_file + extension
                if os.path.isfile(tmp) and os.access(tmp, os.X_OK):
                    return tmp

    return None

def execute_in_path(path, params):
    print(path)
    exec(open(path).read())

def mainOps():
    built_ins = BaseBuilt_Ins()
    while True:
        choice = ask()
        command = choice.split(' ', 1)
        selected_builtin = built_ins.get_builtin(command[0])
        if selected_builtin is not None:
            selected_builtin()
        elif find_exec_in_path(command[0]) is not None:
            try:
                result = subprocess.call(command, shell=True)
            except subprocess.CalledProcessError:
                pass
        else:
            cprint("That is not a function. Type help or list for a list of commands", "red")

def ask():
    choice = input(colored("pyOS> ", "white"))
    choice = choice.lower()
    return choice