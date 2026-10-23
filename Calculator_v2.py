# # """
# # This version of calculator includes the use of functions.

# # Using functions some additional operations have been added into the calculator.

# # Functions like recursive functions are also implemented

# # """

#Defining all the operation functions


def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x//y

def power(x,y):

    if y == 0:
        return x
    return x*power(x,y-1)

def factorial(x):
    if x == 0:
        return 1

    return x * factorial(x-1)

def start():
    print("Welcome to the Calculator_v2 this is an advanced version of the old fashioned one which was brainstormed out of nothing.\n")
    print("This new calculator has two new features, and is made entirely of functions and recursive functions. Which makes this calculator faster and more reliable.\n")


def options():
    print("Choose from the following operations to perform on the numbers.")
    print("Addition(+)\n Subtraction(-)\n Multiplication(*)\n Division(/) \n Factorial(!) \n power(**)\n")
    z = input("Enter your response: ")
    return z



start()


choice = options()


if choice == "addition" or choice == "+":
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    print(addition(x,y))
elif choice == "subtraction" or choice == "-":
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    print(subtraction(x,y))
elif choice == "multiplication" or choice == "*":
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    print(multiplication(x,y))
elif choice == "division" or choice == "/":
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    print(division(x,y))
elif choice == "power" or choice == "**":
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    print(power(x,y))
elif choice == "factorial" or choice == "!":
    x = int(input("Enter number 1 : "))
    print(factorial(x))
