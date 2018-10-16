import os

currDir = "."

if not currDir:
    currDir = "."

currDir = currDir + "/"

def cd(indent):
    directory = input(str(indent) + "What directory would you like to change to? ")
    global currDir
    currDir = directory
# ! GET CD WORKING