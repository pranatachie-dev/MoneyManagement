class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, amount, destination_account):
        self.withdraw(amount)
        destination_account.deposit(amount)


# Whenever the program starts, remember. It reads each code LINE BY LINE. In this case the Class is read first.
# For a reminder: Deposit, Withdraw, and Transfer are all methods. Methods are basically functions running inside a
# Class.
# A parameter is a specific type of variable located within the method's parentheses. Used to pass data into methods.

my_accounts = []
selected_account = None

def get_destination_accounts():
    filtered_account = my_accounts.copy()
    del filtered_account[selected_account]
    return filtered_account

while True:
    print("---------------------------------------------------------")
    print("----------1. create account         Withdraw 4.----------")
    print("----------2. select account         Transfer 5.----------")
    print("----------3. Deposit            Show summary 6.----------")
    print("---------------------------------------------------------")
    
    operation = int(input("Please select a number "))

# Matchcase. Basically just checks if the input matches a certain case, and then runs the code within the case.
# ignoring every other case until the program is finished within said case. For example. If Case 1 has a variable in it.
# That variable is exclusive to that case, when you try to run a variable that is present in another case, it will explode your computer (error.)
# Unless if the variables are mentioned before the match operation. There. Boom.



    match operation:
        case 1:
            account_name = input("Enter name? ")
            balance = float(input("Enter balance? "))
            account = Account(account_name, balance)
            my_accounts.append(account)

        case 2:
            for index, account in enumerate(my_accounts):
                print(f"{index + 1}: {account.name}")
                    
            account_input = int(input("Please select a Number for the Account"))
            
            if account_input < 0 or account_input > len(my_accounts):
                print("Invalid input")
                continue
            else:
                selected_account = account_input - 1
                
        case 3:
            takemoney = float(input("Enter the amount for deposit"))
            my_accounts[selected_account].deposit(takemoney)

        case 4:
            givemoney = float(input("Enter the amount you'd like to withdraw"))
            my_accounts[selected_account].withdraw(givemoney)

        case 5:
            if selected_account is None:
                print("Please select an account first")
                continue
                
            if len(my_accounts) < 2:
                print("Oops, you gotta make 2 accounts to transfer money.")
                continue
            
            print("Select your destination account")
            destination_accounts = get_destination_accounts()

            for index, account in enumerate(destination_accounts):
                print(f"{index + 1}: {account.name}")

            selected_destination_account = int(input("Enter the number corresponding to the account you want to transfer."))

            if selected_destination_account < 1 or selected_destination_account > len(destination_accounts):
                print("Invalid input")
                continue

            # selected_account_name = destination_accounts[selected_destination_account - 1].name
            selected_destination_account = destination_accounts[selected_destination_account - 1]

            transfermoney = float(input("Enter the amount you'd like to transfer"))

            my_accounts[selected_account].transfer(transfermoney, selected_destination_account)

            print(f"{my_accounts[selected_account].balance}, {selected_destination_account.balance} succesful, enjoy your day.")
        case 6:
            if len(my_accounts) == 0:
                print("Oops! You do not have an account, please create at least one to proceed")
                continue

            for account in my_accounts:
                print(f"Name: {account.name}")
                print(f"Balance: {account.balance}")
                print("------------------------------------------")