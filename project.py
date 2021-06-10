import time

class Bank:

    def __init__(self, initial_amount):

        self.balance = initial_amount
        print("\nWELCOME TO SKETCHY NATIONAL BANK! \n ")
        print('\nCurrent Balance: R'+str(initial_amount),'\n')
    def log_transaction(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(f'{transaction_string}\t\t\t\n\nNew Balance: {self.balance}\n\n')


    def withdrawal(self, amount):
        try:
            amount = float(amount)

        except ValueError:
            amount= 0
        if amount:            
            self.balance = self.balance - amount
            self.log_transaction(f"Withdrew: {amount}")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"Deposited: {amount}")


account = Bank(51000.53)


while True:
    
    
    inp = input(
        "\nWhat operation would you like to perform?\n\nPress 1 to Withdraw\nPress 2 to Deposit\nPress 3 To Check Balance\nPress 5 to Exit\n\n-")
    if inp == '5':   
        print('Exiting...')
        time.sleep(1)
        break
    if inp == '3':
        print('processing...')
        time.sleep(1)
        print("Balance: R", account.balance)
        time.sleep(3) 
        continue
    inp2 = input("Amount: ")
    if inp == "2":
        print('processing...')
        time.sleep(1)
        account.deposit(int(inp2))
        print('\nNew Balance: R',account.balance, '\n')
        input("Press Enter To Continue")
        time.sleep(1)
    elif inp == "1":
        print('processing...')
        time.sleep(1)
        account.withdrawal(int(inp2))
        print('\nNew Balance: R',account.balance,'\n')
        input("Press Enter To Continue")
        time.sleep(1)
    elif inp == '5':
        break
    else:
        print("Not an valid command! Try again!\n")
        continue
