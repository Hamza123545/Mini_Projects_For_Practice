# simple calculator

print("Welcome to the simple calculator app")

def calculator():
    num1 = int(input("Enter First Number:  "))
    operators = input("Enter an operator(+, -, *, /): ")
    num2 = int(input("Enter secound Number:  "))


    if operators == "+":
        result = num1 + num2
    elif operators == "-":
        result = num1 - num2
    elif operators == "*":
        result = num1 * num2
    elif operators == "/":
        result = num1 / num2
    else:
    
        print("Enter an valid operator")
        return
    print("Result: ", result)

calculator()