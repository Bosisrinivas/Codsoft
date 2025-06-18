class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2

def main():
    calculator = Calculator()
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if choice == "1":
                    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
                elif choice == "2":
                    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
                elif choice == "3":
                    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
                elif choice == "4":
                    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except ZeroDivisionError as e:
                print(str(e))
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

main()
