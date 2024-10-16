class Calculator:
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
while exit: #While loop keeps the calculator on till choice number 5 get choosen
    print("Welcome to the calculator!")
    print("Choose an operation:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit") #This Option closes the program

    choice = input("Enter the number of the operation you want to perform (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4','5']:
        if choice == '5':
            print("Closing Calculator")
            break
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))           
    if choice == '1':
        print(f"{num1} + {num2} = {Calculator.add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {Calculator.subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {Calculator.multiply(num1, num2)}")
    elif choice == '4':
        result = Calculator.divide(num1, num2)
        if isinstance(result, str):
            print(result)  # Prints error message
        else:
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid choice! Please select a valid operation (1/2/3/4).")