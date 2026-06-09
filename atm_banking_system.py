import os

PASSBOOK_FILE = "passbook.txt"
MIN_BALANCE = 1000


# Create passbook when application runs for the first time
def initialize_passbook():
    if not os.path.exists(PASSBOOK_FILE):
        with open(PASSBOOK_FILE, "w") as file:
            file.write("ATM BANKING SYSTEM PASSBOOK\n")
            file.write("=" * 35 + "\n")
            file.write(f"Account Opening Balance: ₹{MIN_BALANCE}\n\n")
            file.write(f"Final Balance: ₹{MIN_BALANCE}\n")


# Extract current balance from the last line of the passbook
def get_balance():
    with open(PASSBOOK_FILE, "r") as file:
        lines = file.readlines()

    last_line = lines[-1].strip()
    return float(last_line.split("₹")[1])


def update_passbook(transaction, balance):
    with open(PASSBOOK_FILE, "r") as file:
        lines = file.readlines()

    # Remove old final balance before appending new transaction
    lines = lines[:-1]

    with open(PASSBOOK_FILE, "w") as file:
        file.writelines(lines)

        file.write(f"{transaction}\n")
        file.write(f"Current Balance: ₹{balance:.2f}\n\n")
        file.write(f"Final Balance: ₹{balance:.2f}\n")


def deposit():
    balance = get_balance()

    try:
        amount = float(input("Enter amount to deposit (₹): "))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    balance += amount

    update_passbook(
        f"Deposited ₹{amount:.2f}",
        balance
    )

    print("Deposit successful.")
    print(f"Current Balance: ₹{balance:.2f}")


def withdraw():
    balance = get_balance()

    try:
        amount = float(input("Enter amount to withdraw (₹): "))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    # Ensure minimum account balance is maintained
    if balance - amount < MIN_BALANCE:
        print(
            f"Withdrawal denied. "
            f"Minimum balance of ₹{MIN_BALANCE} must be maintained."
        )
        return

    balance -= amount

    update_passbook(
        f"Withdrawn ₹{amount:.2f}",
        balance
    )

    print("Withdrawal successful.")
    print(f"Current Balance: ₹{balance:.2f}")


def view_passbook():
    print("\nATM BANKING SYSTEM PASSBOOK")
    print("=" * 35)

    with open(PASSBOOK_FILE, "r") as file:
        print(file.read())


def main():
    initialize_passbook()

    print("Welcome to ATM Banking System")

    while True:

        print("\n===== ATM MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Passbook")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            deposit()

        elif choice == 2:
            withdraw()

        elif choice == 3:
            view_passbook()

        elif choice == 4:
            print("Thank you for using ATM Banking System.")
            break

        else:
            print("Invalid choice.")


# Run the application only when this file is executed directly
if __name__ == "__main__":
    main()