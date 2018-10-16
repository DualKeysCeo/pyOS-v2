import os
from operations import cd
from termcolor import colored,cprint

class Directories:
    def make(self, indent):
        try:
            dirname = input(str(indent) + "What directory would you like to make? ")
            os.mkdir(os.path.dirname(__file__) + "/../../Files/" + cd.currDir + dirname)
        except:
            cprint("There was an error while making this directory, it may already exist", "red")
    
    def delete(self, indent):
        dirname = input(str(indent) + "What directory would you like to delete? ")
        try:
            os.rmdir(os.path.dirname(__file__) + "/../../Files/" + cd.currDir + dirname)
        except:
            cprint("Please empty the directory first", "red")
# def listF(self, indent):
