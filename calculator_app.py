import sys

class Math:
    @staticmethod
    def calculate(num1, num2, operation):
        if operation == '1':
            return num1 + num2
        elif operation == '2':
            return num1 - num2
        elif operation == '3':
            return num1 * num2
        elif operation == '4':
            if num1 == 0:
                raise ZeroDivisionError ("You can't divide by zero")
            elif num2 == 0:
                raise ZeroDivisionError ("You can't divide by zero")
            return num1 / num2
        else:
            raise ValueError("Invalid operation")

class Calculator:
    def __init__(self):
        self.operator = Math()
        self.menu = {
            '1' : "Addition",
            '2' : "Subtraction",
            '3' : "Multiplication",
            '4' : "Division"
        }

    def get_numbers(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("That's not a number. Please try again.")

    def run(self):
        print("Welcome to Calculator")
        while True:
            print("\n Select an operation:")
            for key, value in self.menu.items():
                print(f"{key}: {value}")
            choice = input("\n Enter your choice: ")
            if choice not in self.menu:
                print("Invalid choice. Choose 1, 2, 3, or 4.")
                continue
                


