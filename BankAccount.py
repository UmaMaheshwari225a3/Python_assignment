class BankAccount:
    min_balance = 1000

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid")
        elif self.balance - amount < BankAccount.min_balance:
            print("Withdrawal denied")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")

    def display(self):
        print("Account No:", self.acc_no)
        print("Name:", self.name)
        print("Balance:", self.balance)
        print("Minimum Balance:", BankAccount.min_balance)

    @classmethod
    def update_min_balance(cls, new_min_balance):
        cls.min_balance = new_min_balance
        print("Minimum balance updated to:", new_min_balance)


acc1 = BankAccount(101, "Uma", 1000)
acc2 = BankAccount(102, "Ravi", 2000)

acc1.deposit(2000)
acc1.withdraw(4000)
acc1.display()

BankAccount.update_min_balance(2000)

acc2.withdraw(1500)
acc2.display()
