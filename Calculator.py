import re

def calculate(expression):
    return eval(expression)

operators = ['+', '-', '*', '/']

print("Welcome to the Calculator Application!")
print("Enter the math problem you would like solved (e.g. '1+1').")
print("Valid operators:", operators)
print("Enter 'exit' to exit the application.")

while True:
    user_input = input("Enter problem: ")
    if user_input == 'exit':
        break
    else:
        try:
            result = calculate(user_input)
            print("Result: ", result)
        except:
            print("Invalid input. Please try again.")
