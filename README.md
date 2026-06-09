# ATM Banking System

A menu-driven ATM Banking System built using Python. The application allows users to deposit and withdraw money while maintaining a passbook that records transaction history and account balance.

## Features

* Deposit money
* Withdraw money
* Minimum balance enforcement (₹1000)
* View passbook
* Transaction history tracking
* Persistent data storage using a text file
* Input validation and error handling
* Automatic passbook creation on first run

## Technologies Used

* Python
* File Handling
* Functions
* Exception Handling

## What I Learned

* Working with text files in Python
* Reading and writing data to files
* Building menu-driven applications
* Handling exceptions using try-except
* Implementing business rules in software
* Organizing code using functions

## Project Structure

```text
python-atm-simulator/
│
├── atm_simulator.py
└── README.md
```

## How to Run

1. Make sure Python is installed on your system.
2. Download or clone the repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python atm_simulator.py
```

The program automatically creates a `passbook.txt` file during its first execution.

## Sample Menu

```text
===== ATM MENU =====
1. Deposit
2. Withdraw
3. View Passbook
4. Exit
```

## Sample Operations

* Deposit money into the account
* Withdraw money while maintaining the minimum balance
* View complete transaction history through the passbook
* Track account balance after every transaction

## Future Improvements

* PIN authentication
* Multiple user accounts
* SQLite database integration
* GUI using Tkinter
