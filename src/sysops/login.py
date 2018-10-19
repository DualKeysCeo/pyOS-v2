import os
import __main__
from time import sleep
from termcolor import colored, cprint

def login():
    cprint("User authentication needed!", "yellow")
    fp = open(os.path.dirname(__file__) + "/user.info", "r+")
    for i, line in enumerate(fp):
        line = line.rstrip()
        if i == 0:
            global user
            user = line
        elif i == 1:
            global password
            password = line

    global userI
    global passwordI
    if user and password:
        userI = input(colored("pyOS/Login/Username> ", "white"))
        passwordI = input(colored("pyOS/Login/Password> ", "white"))
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
    else:
        cprint("Please make an account")

def logout():
    string = "Logging out"
    sleep(0.5)
    for _ in range(4):
        if string == "Logging out...":
            string = "Logging out"
            sleep(0.5)
        else:
            string = string + "."
            cprint(" "*14, end="\r")
            cprint(string, "red", end="\r")
            sleep(0.5)
        exit(1)