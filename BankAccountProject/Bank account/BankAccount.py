class BankAccount:
    def __init__(self):
        self.balance = 0.0
        
    def deposite(self,amount):
        if amount > 0:        
            self.amount = amount
            self.balance += self.amount
            print("Balance: ",self.balance)
        else:
            print("Invalid Amount Value")
            
    def withdraw(self, amountW):
        if self.balance == 0 or amountW < 0 or amountW > self.balance:
            print("Invalid To Withdraw \n Check Your Account Balance or Value enterd")
        else:
            self.balance -= amountW
            print("Balance: ",self.balance,"\n")
            
    def CheckBalance(self):
        print("Balance: ",self.balance,"\n")
    
exit = True
def exit_program():
    global exit
    exit = False
    print("Exiting the program...")
account = BankAccount()
key = {
        "1": lambda: account.deposite(float(input("Enter amount to deposite: \n"))),
        "2": lambda: account.withdraw(float(input("Enter amount to withdraw: \n"))),
        "3": lambda:account.CheckBalance(),
        "4": lambda: exit_program()
    }
print("Welcome to our Bank\n")
while exit:
    print("1: Deposite \n 2: Withdraw \n 3: Check Balance \n 4: Exite")
    start = input("Select the operation: \n(Enter 4 to Exite)\n")
    if int(start) > 4 or int(start) < 1:
        print("Invalid Value ! try Again")
    else:
        key[start]()
