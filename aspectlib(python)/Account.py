class Account():
    ANSI_YELLOW = "\033[33m"
    ANSI_RESET = '\033[0m'

    def __init__(self):
        self.balance = 20

    def withdraw(self, amount: int) -> bool:
        if (self.balance < amount):
            print(f"{self.ANSI_YELLOW}[ACTUAL FUNCTION] Not enough balance |  Balance left: {self.balance}{self.ANSI_RESET}")
            return False

        self.balance -= amount
        print(f"{self.ANSI_YELLOW}[ACTUAL FUNCTION] Widraw {amount} | Balance left: {self.balance}{self.ANSI_RESET}")
        return True

    def deposit(self, amount: int) -> bool:
        self.balance += amount
        return True