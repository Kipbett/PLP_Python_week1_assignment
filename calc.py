'''
This is a calculator program.
Allows the user to input two number and choose the mathematical operation they intend to perform
'''
# Ask the users to enter the values
number1 = float(input("Enter the First Number: "))
number2 = float(input("Enter the Second Number: "))
operation = input("Enter the mathematical operation +,-,/,*: ")


if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '/':
    result = number1 / number2
elif operation == '*':
    result = number1 * number2
else:
    print("You entered an invalid option")

print(f"You Selected {operation} and entered {number1} and {number2} and the Result is: {result}")