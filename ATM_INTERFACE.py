#atm interface

import tkinter as tk
from tkinter import messagebox

# Initialize the account balance
balance = 100000
def pin_entry():
    pin=pin_enter.get()
    if pin =='1234':
      messagebox.showinfo("Proceed")
    else:
      messagebox.showerror("Incorrect pin")
    

# Function to check balance
def check_balance():
    global balance
    messagebox.showinfo("Balance", f"Your current balance is: ${balance}")

# Function to deposit money
def deposit():
    global balance
    amount = deposit_entry.get()
    if amount.isdigit() and int(amount) > 0:
        balance += int(amount)
        messagebox.showinfo("Deposit", f"${amount} has been deposited.")
    else:
        messagebox.showerror("Error", "Please enter a valid amount.")
    deposit_entry.delete(0, tk.END)

# Function to withdraw money
def withdraw():
    global balance
    amount = withdraw_entry.get()
    if amount.isdigit() and int(amount) > 0:
        if int(amount) <= balance:
            balance -= int(amount)
            messagebox.showinfo("Withdraw", f"${amount} has been withdrawn.")
        else:
            messagebox.showerror("Error", "Insufficient amount.")
    else:
        messagebox.showerror("Error", "Please enter a valid amount.")
    withdraw_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple ATM Interface")

# Create and place the widgets
balance_button = tk.Button(root, text="Check Balance", command=check_balance)
balance_button.grid(row=3, column=1)

tk.Label(root, text="Deposit Amount:").grid(row=1, column=0)
deposit_entry = tk.Entry(root)
deposit_entry.grid(row=1, column=1)
deposit_button = tk.Button(root, text="Deposit", command=deposit)
deposit_button.grid(row=1, column=2)

tk.Label(root, text="Withdraw Amount:").grid(row=2, column=0)
withdraw_entry = tk.Entry(root)
withdraw_entry.grid(row=2, column=1)
withdraw_button = tk.Button(root, text="Withdraw", command=withdraw)
withdraw_button.grid(row=2, column=2)

tk.Label(root,text="Enter the pin").grid(row=0,column=0)
pin_enter=tk.Entry(root)
pin_enter.grid(row=0,column=1)
pin_enter.delete(0, tk.END)
button=tk.Button(root,text="Enter",command=pin_entry,bg="blue",fg="white")
button.grid(column=2,row=0)
# Run the application
root.mainloop()
