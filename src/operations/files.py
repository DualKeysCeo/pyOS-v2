import os
from textwrap import wrap
from operations import cd
from termInfo import termCols
from termcolor import colored,cprint

class Files:
    def make(self, indent):
        try:
            filename = input(str(indent) + "File name: ")
            myFile = open(os.path.dirname(__file__) + "/../../Files/" + cd.currDir + filename, "w")
            contents = input(str(indent) + "Please write to the file (only one line): ")
            myFile.write(contents)
            myFile.close()
        except:
            cprint("There was an error while making the file, it may already exist", "red")

    def use(self, indent):
        filename = input(str(indent) + "What file do you want to open? ")
        os.system("start ../../Files/" + cd.currDir + filename)

    def delete(self, indent):
        filename = input(str(indent) + "What file would you like to delete? ")
        os.remove(os.path.dirname(__file__) + "/../../Files/" + cd.currDir + filename)

    def listF(self, indent):
        dirList = []
        fileList = []
        for root,dirs,files in os.walk(os.path.dirname(__file__) + "/../../Files/" + cd.currDir):
            for name in dirs:
                dirList.append(name + "/")
            for Ffile in files:
                fileList.append(Ffile)
        for i in wrap("    ".join(dirList), width=termCols()):
            cprint(i, "red")
        for i in wrap("    ".join(fileList), width=termCols()):
            cprint(i, "cyan")