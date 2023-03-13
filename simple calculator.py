# Functions definition
def addition(num1,num2) :
    return num1 + num2

def subtraction(num1,num2) :
    return num1 - num2

def multiplication(num1,num2) :
    return num1 * num2

def division(num1,num2) :
    return num1 / num2

def exponent(num1,num2) :
    return num1 ** num2

# Operator recognize
def calculator(num1,num2) :

    # Get the operator from user
    operator = input("Please enter operator (+,-,*,/,**) :")
    # Addition
    if operator == "+" :
        print(num1,"plus",num2,"is ",addition(num1,num2))
    # Subtracion
    elif operator == "-" :
        print(num1,"minus",num2,"is ",subtraction(num1,num2))
    # Division
    elif operator == "/" :
        print(num1,"divided by",num2,"is ",division(num1,num2))
    # Multiplication
    elif operator == "*" :
        print(num1,"times",num2,"is ",multiplication(num1,num2))
    # Exponent
    elif operator == "**" :
        print(num1,"to the power of",num2,"is",exponent(num1,num2))
    # Exception handling (+,-,/,*,**)
    else :
        print("the operator isn't correct!")

# Welcome title
print("""Welcome to calculator.
_______________________________
-------------------------------""")

# Program loop
while True :

    # Exception handling(int,float)
    try :
        num1 = float(input("Please enter first number :"))
        num2 = float(input("Please enter second number :"))
    except :
        print("Please enter an integer or float!")
    else :
        # Calculate
        calculator(num1,num2)
    # Get a order to continue
    order = input("Do you wanna play again? Please enter y or n :")
    # Exit the program
    if order == 'n' :
        print("Goodluck!")
        break
    # Play again
    elif order == 'y' :
        pass
    # Exception handling (y,n)
    else :
        print("Something went wrong! you didn't enter y or n")
        break
