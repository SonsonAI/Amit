class Calculator:
    def __init__(self):
        self.lastAnswer = 0 #Saved results button
    def add(self, a, b):
        """Add two numbers."""
        self.addition = a + b
        print(f"{a} + {b} = {self.addition}")
        self.lastAnswer = a + b
    def subtract(self, a, b):
        """Subtract two numbers."""
        self.subtraction = a - b
        print(f"{a} - {b} = {self.subtraction}")
        self.lastAnswer = a - b
    def multiply(self, a, b):
        """Multiply two numbers."""
        self.multiplication = a * b
        print(f"{a} * {b} = {self.multiplication}")
        self.lastAnswer = a * b
    def divide(self, a, b):
        """Divide two numbers."""
        if b != 0:
            self.division = a / b
            print(f"{a} / {b} = {self.division}")
            self.lastAnswer = a / b
        else:
            print("Calculation Error")
    def getLastAnswer(self):
        return self.lastAnswer
    def calculator(self):
        print("Welcome to the calculator!")
        while True:
            """Main calculator logic to get user input and perform operations."""
            print("Choose an operation:")
            print("1: Add")
            print("2: Subtract")
            print("3: Multiply")
            print("4: Divide")
            print("5: ans") #it returns final number calculated from the calculator
            print("6: Exit")

            choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")
            if choice =='6':
                break
            elif choice == '5':
                 print(f"Ans: {self.getLastAnswer()}")
            if choice in ['1', '2', '3', '4']:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
                    return
                
                if choice == '1':
                    self.add(num1, num2)
                elif choice == '2':
                    self.subtract(num1, num2)
                elif choice == '3':
                    self.multiply(num1, num2)
                elif choice == '4':
                    result = self.divide(num1, num2)
                    if isinstance(result, str):
                        print(result)  # Prints error message
                    else:
                        print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid choice! Please select a valid operation (1/2/3/4).")

# Usage example
if __name__ == "__main__":
    calculator = Calculator()
    calculator.calculator()