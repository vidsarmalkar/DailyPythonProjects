class Account:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance = self.balance + amount

    def view_balance(self):
        print(f"Account holder: {self.name}, Balance: {self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        user_name = input("Enter your name: ")
        bal = float(input("Enter initial deposit: "))
        self.accounts[user_name] = Account(user_name, bal)
        print(f"Account created for {user_name} with balance {bal}")

    def deposit_money(self):
        user_name = input("Enter your name: ")
        deposit = float(input("Enter amount to deposit: "))
        if user_name in self.accounts:
            self.accounts[user_name].deposit(deposit)
            print(f"{deposit} deposited. New balance: {self.accounts[user_name].balance}")

    def view_balance(self):
        user_name = input("Enter your name: ")
        if user_name in self.accounts:
            self.accounts[user_name].view_balance()

    def run(self):
        while True:
            print()
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. View Balance")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.view_balance()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Existing, Wrong choice..")

if __name__ == '__main__':
    bank_system = BankSystem()
    bank_system.run()
