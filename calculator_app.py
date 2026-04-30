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

    @staticmethod
    def get_number(prompt):
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

            n1 = self.get_number("Enter first number: ")
            n2 = self.get_number("Enter second number: ")

            try:
                result = self.operator.calculate(n1, n2, self.menu[choice])
                print(f"\n Result: {n1} {self._get_symbol(choice)} {n2} = {result}")
            except ZeroDivisionError as e:
                print(f"\n {e}")
            except Exception as e:
                print(f"\n An expected error occurred: {e}")

            retry = input("\n Want ot go another round? (y/n): ") .lower()
            if retry != "y":
                print("\n Thank you for using calculator.")
                sys.exit()

    @staticmethod
    def _get_symbol(choice):
        symbols = {'1': '+', '2': '-', '3': '*', '4': '/'}
        return symbols.get(choice)

if __name__ == "__main__":
    app = Calculator()
    app.run()


