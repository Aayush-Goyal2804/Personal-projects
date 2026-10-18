"""
Hello this is my git hub page where I'll upload every one of my projects starting from extremely basic ones to intermediate level ones.



"""

"""
Project 1:-

Basic calculator using direct, if-elif-else conditional calculator.


"""



#This variable accepts operation input from the user.
user_in = (input("Which operation do you want to perform? \n Addition(+) \n Subtraction (-)\n Multiplication (*) \n division(/)\n").lower())



#Accpeting two numbers to do the mathematical operation
user_num = int(input("Number 1 :- "))
user_num1 = int(input("Number 2 :- "))


if user_in == "addition":
    print(f"Output:- {user_num + user_num1}")
elif user_in == "multiplication":
    print(f"Output: {user_num*user_num1}")
elif user_in == "subtraction":
    print(f"{user_num - user_num1}")
elif user_in == "division":
    print(f"Output: {user_num/user_num1}")


