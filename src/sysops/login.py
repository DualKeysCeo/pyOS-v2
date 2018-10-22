import os
import __main__
from time import sleep
from operations import credentials
from integrations.termcolor import colored, cprint

def login():
    try:
        fp = open(os.path.dirname(__file__) + "\\..\\user\\user_login.info", "r+")
        for i, line in enumerate(fp):
            line = line.rstrip()
            if i == 0:
                global user
                user = line
            elif i == 1:
                global password
                password = line
    except:
        cprint("Please make an account", "yellow")
        user = input(colored("pyOS/Login/new username> ", "white"))
        password = input(colored("pyOS/Login/new password> ", "white"))
        credentials.change(user, password)
        __main__.clear()
        login()

    global userI
    global passwordI
    if user and password:
        cprint("User authentication needed!", "yellow")
        userI = input(colored("pyOS/Login/username> ", "white"))
        passwordI = input(colored("pyOS/Login/password> ", "white"))
        if userI == user:
            if passwordI == password:
                print("Access Granted")
                sleep(1)
                __main__.mainOS()
            else:
                cprint("Password incorrect", "red")
                login()
        else:
            cprint("Username incorrect", "red")
            login()


def logout():
    string = "Logging out"
    sleep(0.5)
    for i in range(4):
        if string == "Logging out...":
            string = "Logging out"
            sleep(0.5)
        else:
            string = string + "."
            cprint(" "*14, end="\r")
            cprint(string, "red", end="\r")
            sleep(0.5)
        exit(1)