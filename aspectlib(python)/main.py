from Account import Account
import AccountAspect


def main():
    account = Account()
    account.withdraw(5)
    print("------------------------------------------------------------------------")
    account.withdraw(10)
    print("------------------------------------------------------------------------")
    account.withdraw(5)
    print("------------------------------------------------------------------------")
    account.withdraw(10)

if __name__ == "__main__":
    main()
