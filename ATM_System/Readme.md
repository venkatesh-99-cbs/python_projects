🏧 ATM Management System (Python – OOPS)
📌 Project Overview

The ATM Management System is a console-based Python application designed using Object-Oriented Programming (OOPS) principles.
It simulates basic ATM operations such as balance inquiry, cash withdrawal, deposit, and transaction tracking.

This project helps in understanding how real-world banking systems can be modeled using classes, objects, inheritance, encapsulation, and abstraction.

🎯 Features

🔐 PIN verification

💰 Balance inquiry

➕ Cash deposit

➖ Cash withdrawal

📜 Transaction history

🚫 Withdrawal limit

🔢 Transaction counter

❌ Exit confirmation

🧠 OOPS Concepts Used

Class & Object

Encapsulation (public, protected, private variables)

Inheritance

Polymorphism

Abstraction (using ABC and @abstractmethod)

Static variables

🗂️ Project Structure
ATM-Management-System/
│
├── README.md
├── ATM_System.py

📄 File Description

ATM_System.py

Entry point of the application

Displays menu and handles user input

Core ATM operations

Withdraw, deposit, balance check

Account class

Stores account number and balance

Demonstrates encapsulation

Manages transaction history

Counts number of transactions

Handles PIN verification

Security-related logic

▶️ How to Run the Project
Requirements

Python 3.x installed

Steps
python main.py

🧪 Sample Operations

Enter PIN

Choose operation:

1 → Check Balance

2 → Deposit

3 → Withdraw

4 → Transaction History

5 → Exit

🔒 Example of Encapsulation Used
self.name = name          # Public
self._account_number = acc_no   # Protected
self.__balance = balance        # Private

📚 Learning Outcomes

Real-world application of OOPS

Clean project structuring

Better understanding of data hiding

Improved logical thinking
