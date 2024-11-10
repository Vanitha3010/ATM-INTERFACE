# ATM-INTERFACE
The ATM Interface project is a simple application developed using Python's Tkinter library to simulate essential banking transactions. This program provides users with options to check their account balance, deposit money, and withdraw funds. This project serves as a basic model of an Automated Teller Machine (ATM) interface, demonstrating how user interactions with ATM functions can be implemented programmatically.

# Objective:

The primary objective of this project is to create an ATM interface that enables a user to:

Check their current account balance.
Deposit a specified amount.
Withdraw a specified amount (if sufficient funds are available).
Verify the user’s identity through a PIN check.
# Program Design
The project is built using Python and Tkinter, a standard GUI library, allowing for easy development of graphical interfaces. The program implements the following features:

PIN Verification: Users must enter a PIN to proceed with any transactions. This security feature is essential for simulating real-world ATM functionality, where only authorized users should access account operations.

Balance Inquiry: Users can check their current balance, which is initially set to a predefined amount of $100,000. The balance is updated in real-time based on deposits and withdrawals.

Deposit Function: Users can enter an amount to deposit, which will be added to their current balance if the amount is valid.

Withdraw Function: Users can enter an amount to withdraw, provided there are sufficient funds in the account. If funds are inadequate, an error message is displayed, preventing overdrafts.
