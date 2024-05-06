class Calculator:
    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        if n2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return n1 / n2

    def calculate(self, operator, n1, n2):
        if operator == "+":
            return self.add(n1, n2)
        elif operator == "-":
            return self.sub(n1, n2)
        elif operator == "*":
            return self.mul(n1, n2)
        elif operator == "/":
            return self.div(n1, n2)


def main():
    calculator = Calculator()

    while True:
        try:
            user_input = input("Enter an operator (+ - * /), 'q' to quit: ")

            if user_input == "q":
                print("Goodbye!")
                break

            operators = ["+", "-", "*", "/"]

            if user_input not in operators:
                raise ValueError("Invalid Operator!")

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calculator.calculate(user_input, num1, num2)
                print(f"The result is {result}")
            except ValueError:
                print("Error: Please enter valid input.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")


if __name__ == "__main__":
    main()
