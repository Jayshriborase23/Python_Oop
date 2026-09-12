
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("₹", amount, "deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("₹", amount, "withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Jayshri", 5000)

print("Account Holder:", account.name)
print("Initial Balance: ₹", account.get_balance())

account.deposit(2000)
print("Balance: ₹", account.get_balance())

account.withdraw(1500)
print("Balance: ₹", account.get_balance())
