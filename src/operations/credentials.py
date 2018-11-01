import os

def change(user, passw):
    fp = open(os.path.dirname(__file__) + "\\..\\user\\user_login.info", "w+")
    fp.write(user + "\n")
    fp.write(passw)
    fp.close()