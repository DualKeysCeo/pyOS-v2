import os

def change(user, passw):
    fp = open(os.path.dirname(__file__) + "/../user info/user.info", "w+")
    fp.write(user + "\n")
    fp.write(passw + "\n")
    fp.close()