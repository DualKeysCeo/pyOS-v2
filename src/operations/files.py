import os
from textwrap import wrap
from sysops import termInfo
from termcolor import colored,cprint

class Files:
    def make(self, indent):
        try:
            filename = input(str(indent) + "File name: ")
            myFile = open(os.path.dirname(__file__) + "/../../Files/" + filename, "w")
            contents = input(str(indent) + "Please write to the file (only one line): ")
            myFile.write(contents)
            myFile.close()
        except:
            cprint("There was an error while making the file, it may already exist", "red")

    def use(self, indent):
        filename = input(str(indent) + "What file do you want to open? ")
        print(filename)
        os.system("start ..\\..\\Files\\" + filename)

    def delete(self, indent):
        filename = input(str(indent) + "What file would you like to delete? ")
        os.remove(os.path.dirname(__file__) + "/../../Files/" + filename)

    def listF(self, indent):
        dirList = []
        fileList = []
        for root,dirs,files in os.walk(os.path.dirname(__file__) + "/../../Files/"):
            for name in dirs:
                dirList.append(name + "/")
            for Ffile in files:
                fileList.append(Ffile)
        for i in wrap("    ".join(dirList), width=termInfo.termCols()):
            cprint(i, "red")
        for i in wrap("    ".join(fileList), width=termInfo.termCols()):
            cprint(i, "cyan")

fileOps = [
    "make",
    "open",
    "delete"
]

def choose():
    for i in wrap("    ".join(fileOps), width=termInfo.termCols() * (2.0/3.0)):
        cprint(i, "cyan")

    choice = input(colored("pyOS/operations/file> ", "white"))
    choice = choice.lower()

    if choice == fileOps[0]:
        Files.make(Files, "\t\t")
    elif choice == fileOps[1]:
        Files.use(Files, "\t\t")
    elif choice == fileOps[2]:
        Files.delete(Files, "\t\t")
    else:
        cprint("That is not a function. Type help or commands for a list of commands", "red")