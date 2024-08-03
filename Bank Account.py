from random import randrange


class BankAccount:
    all_account_numbers = set()

    def __init__(self, name: str):
        self.account_number: float = 0
        while True:
            if (an := randrange(10_000, 100_000)) not in BankAccount.all_account_numbers:
                BankAccount.all_account_numbers.add(an)
                self.account_number = an
                break
        self.name = name
        self.balance: float = 0

    def display(self):
        print(40 * "*")
        print(f"Hi {self.name} your balance is: {self.balance}")
        print(40 * "*")

    def deposit(self):
        amount = int(input("please enter amount of money you want to deposit: "))
        self.balance += amount
        self.display()
        print(40 * "*")

    def withdraw(self):
        amount = int(input("please enter amount of money you want to withdraw: "))
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount
        self.display()


def main():
    acc1 = BankAccount("Reza Dolati")
    print(40 * "*")
    print(f"account_number: {acc1.account_number}")
    print(40 * "*")
    acc1.display()

    while True:
        choice = int(input("1 to see your balance\n2 to to deposit\n3 to withdraw\n4 to exit\n\t your choice: "))
        if choice == 1:
            acc1.display()
        elif choice == 2:
            acc1.deposit()
        elif choice == 3:
            acc1.withdraw()
        elif choice == 4:
            break
        else:
            print("invalid number!!")


if __name__ == "__main__":
    main()
