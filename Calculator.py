
# calculator.py
# Menu-Driven Scientific Calculator

import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a // b

def square_root(a):
    if a < 0:
        return "Error! Cannot calculate square root of a negative number."
    return math.sqrt(a)

def percentage(a, b):
    return (a * b) / 100

def factorial(a):
    if a < 0 or not a.is_integer():
        return "Error! Enter a non-negative whole number."
    return math.factorial(int(a))

def calculator():
    while True:
        print("\n========== PYTHON CALCULATOR ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Floor Division")
        print("8. Square Root")
        print("9. Percentage")
        print("10. Factorial")
        print("11. Exit")
        print("=======================================")

        choice = input("Enter your choice (1-11): ")

        if choice == "11":
            print("Thank you for using the calculator!")
            break

        if choice in ["1", "2", "3", "4", "5", "6", "7", "9"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = addition(num1, num2)
                elif choice == "2":
                    result = subtraction(num1, num2)
                elif choice == "3":
                    result = multiplication(num1, num2)
                elif choice == "4":
                    result = division(num1, num2)
                elif choice == "5":
                    result = modulus(num1, num2)
                elif choice == "6":
                    result = power(num1, num2)
                elif choice == "7":
                    result = floor_division(num1, num2)
                else:
                    result = percentage(num1, num2)

                print("Result:", result)

            except ValueError:
                print("Invalid input! Please enter numbers.")

        elif choice == "8":
            try:
                num = float(input("Enter a number: "))
                print("Result:", square_root(num))
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "10":
            try:
                num = float(input("Enter a number: "))
                print("Result:", factorial(num))
            except ValueError:
                print("Invalid input! Please enter a number.")

        else:
            print("Invalid choice! Please select between 1 and 11.")


if __name__ == "__main__":
    calculator()

