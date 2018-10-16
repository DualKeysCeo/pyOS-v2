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

