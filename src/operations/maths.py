from textwrap import wrap
from sysops import termInfo
from integrations.termcolor import colored, cprint

class Math:
    def _init_(self):
        num = 0

    def add(self, indent):
        print("\tAdding mode, number 1 + number 2")
        num1 = input("\t\tWhat is your first number? ")
        num2 = input("\t\tWhat is your second number? ")
        num = int(num1) + int(num2)
        print(indent + str(num))

    def subtract(self, indent):
        print("\tAdding mode, number 1 - number 2")
        num1 = input("\t\tWhat is your first number? ")
        num2 = input("\t\tWhat is your second number? ")
        num = int(num1) - int(num2)
        print(indent + str(num))

    def multiply(self, indent):
        print("\tAdding mode, number 1 * number 2")
        num1 = input("\t\tWhat is your first number? ")
        num2 = input("\t\tWhat is your second number? ")
        num = int(num1) * int(num2)
        print(indent + str(num))

    def divide(self, indent):
        print("\tAdding mode, number 1 / number 2")
        num1 = input("\t\tWhat is your first number? ")
        num2 = input("\t\tWhat is your second number? ")
        num = int(num1) / int(num2)
        print(indent + str(num))

mathOps = [
    "add",
    "subtract",
    "multiply",
    "divide"
]

def choose():
    for i in wrap("    ".join(mathOps), width=termInfo.termCols() * (2.0/3.0)):
        cprint(i, "cyan")

    choice = input(colored("pyOS/operations/math> ", "white"))
    choice = choice.lower()

    if choice == mathOps[0]:
        try:
            Math.add(Math, "\t\t")
        except:
            cprint("Error: Unexpected Input/Internal Error", "red")
    elif choice == mathOps[1]:
        try:
            Math.subtract(Math, "\t\t")
        except:
            cprint("Error: Unexpected Input/Internal Error", "red")
    elif choice == mathOps[2]:
        try:
            Math.multiply(Math, "\t\t")
        except:
            cprint("Error: Unexpected Input/Internal Error", "red")
    elif choice == mathOps[3]:
        try:
            Math.divide(Math, "\t\t")
        except:
            cprint("Error: Unexpected Input/Internal Error", "red")
    else:
        cprint("That is not a function. Type help or commands for a list of commands", "red")