import os
from textwrap import wrap
from sysops import login, termInfo
from termcolor import colored, cprint
from operations import credentials, maths, files, directories

class BaseBuiltins:
    builtins = None

    def __init__(self):
        self.builtins = self.Builtins()

    class Builtins:
        def __init__(self):
            pass

        def hello(self):
            print("Hello world")

        def exit(self):
            login.logout()

        def clear(self):
            os.system("cls")

        def ls(self):
            files.Files.listF(files.Files, "\t\t")

        def changecreds(self):
            user = input("\tWhat is your new username? ")
            password = input("\tWhat is your new password? ")
            credentials.change(user, password)
            os.system("cls")
            login.login()

        def math(self):
            maths.choose()

        def file(self):
            files.choose()

        def directory(self):
            directories.Directories.choose()

        def help(self):
            method_list = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
            for i in wrap("    ".join(method_list), width=termInfo.termCols() * (2.0/3.0)):
                cprint(i, "cyan")

    def get_builtin(self, command):
        if hasattr(self.builtins, command) is True:
            return getattr(self.builtins, command)
        return None