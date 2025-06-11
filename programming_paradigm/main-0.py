# main-0.py

# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command
    input_parts = sys.argv[1].split(':')

    command = input_parts[0].lower()

    # For deposit and withdraw, ensure amount is provided and valid
    if command in ("deposit", "withdraw"):
        if len(input_parts) != 2:
            print(f"Usage: python main-0.py {command}:<amount>")
            return
        try:
            amount = float(input_parts[1])
        except ValueError:
            print("Amount must be a number.")
            return

        if command == "deposit":
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif command == "withdraw":
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
