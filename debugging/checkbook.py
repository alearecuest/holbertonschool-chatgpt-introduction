#!/usr/bin/python3

class Checkbook:
    """
    A class representing a checkbook that tracks deposits and withdrawals.
    
    This class provides methods to manage a simple bank account,
    allowing users to deposit, withdraw money and check their balance.
    """
    
    def __init__(self):
        """
        Initialize a new Checkbook with zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add money to the checkbook balance.
        
        Parameters:
            amount (float): The amount of money to deposit.
        
        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Remove money from the checkbook balance if sufficient funds are available.
        
        Parameters:
            amount (float): The amount of money to withdraw.
        
        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance in the checkbook.
        
        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function that runs the checkbook application.
    
    Provides a command-line interface for users to interact with
    their checkbook by depositing, withdrawing money, checking
    balance, or exiting the application.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Error: Amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Error: Amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
