
# Not so advanced calculator
# Use + to add, use - to substract, use * to multiply, use / to divide

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "x":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator, please try again")
