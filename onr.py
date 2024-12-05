import pymysql.cursors

# Database connection
con = pymysql.connect(
    host="localhost",
    user="root",          
    cursorclass=pymysql.cursors.DictCursor,
    database="bank_management"
)

print(con)
mycursor=con.cursor()
# mycursor.execute()

import tkinter as tk
from tkinter import messagebox
import mysql.connector


cursor = con.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    account_no INT NOT NULL UNIQUE,
    contact_details VARCHAR(255),
    email_address VARCHAR(255)
)
""")
con.commit()

# Main application class
class BankManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System 💳")
        self.create_widgets()

    def create_widgets(self):
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack(pady=20)

        tk.Label(self.welcome_frame, text="Welcome to the Bank Management System", font=("Helvetica", 16)).pack()
        tk.Button(self.welcome_frame, text="Existing User", command=self.existing_user).pack(pady=10)
        tk.Button(self.welcome_frame, text="New User", command=self.new_user).pack(pady=10)

    def new_user(self):
        self.welcome_frame.pack_forget()
        self.new_user_frame = tk.Frame(self.root)
        self.new_user_frame.pack(pady=20)

        tk.Label(self.new_user_frame, text="New User Registration", font=("Helvetica", 16)).pack()
        tk.Label(self.new_user_frame, text="Username:").pack()
        self.username_entry = tk.Entry(self.new_user_frame)
        self.username_entry.pack()

        tk.Label(self.new_user_frame, text="Name:").pack()
        self.name_entry = tk.Entry(self.new_user_frame)
        self.name_entry.pack()

        tk.Label(self.new_user_frame, text="Account No:").pack()
        self.account_no_entry = tk.Entry(self.new_user_frame)
        self.account_no_entry.pack()

        tk.Label(self.new_user_frame, text="Contact Details:").pack()
        self.contact_entry = tk.Entry(self.new_user_frame)
        self.contact_entry.pack()

        tk.Label(self.new_user_frame, text="Email Address:").pack()
        self.email_entry = tk.Entry(self.new_user_frame)
        self.email_entry.pack()

        tk.Button(self.new_user_frame, text="Register", command=self.register_user).pack(pady=10)

    def register_user(self):
        username = self.username_entry.get()
        name = self.name_entry.get()
        account_no = self.account_no_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()

        cursor.execute("INSERT INTO users (username, name, account_no, contact_details, email_address) VALUES (%s, %s, %s, %s, %s)",
                       (username, name, account_no, contact, email))
        con.commit()
        messagebox.showinfo("Success", "User registered successfully!")
        self.new_user_frame.pack_forget()
        self.create_widgets()

    def existing_user(self):
        self.welcome_frame.pack_forget()
        self.existing_user_frame = tk.Frame(self.root)
        self.existing_user_frame.pack(pady=20)

        tk.Label(self.existing_user_frame, text="Existing User Login", font=("Helvetica", 16)).pack()
        tk.Label(self.existing_user_frame, text="Account No:").pack()
        self.account_no_entry = tk.Entry(self.existing_user_frame)
        self.account_no_entry.pack()

        tk.Button(self.existing_user_frame, text="Login", command=self.user_dashboard).pack(pady=10)

    def user_dashboard(self):
        account_no = self.account_no_entry.get()
        cursor.execute("SELECT * FROM users WHERE account_no = %s", (account_no,))
        user = cursor.fetchone()

        if user:
            self.existing_user_frame.pack_forget()
            self.dashboard_frame = tk.Frame(self.root)
            self.dashboard_frame.pack(pady=20)

            tk.Label(self.dashboard_frame, text=f"Welcome {user[1]}!", font=("Helvetica", 16)).pack()
            tk.Button(self.dashboard_frame, text="Update Balance", command=self.update_balance).pack(pady=10)
            tk.Button(self.dashboard_frame, text="Debit Amount", command=self.debit_amount).pack(pady=10)
            tk.Button(self.dashboard_frame, text="Credit Amount", command=self.credit_amount).pack(pady=10)
        else:
            messagebox.showerror("Error", "Account not found!")

    def update_balance(self):
        # Functionality to update balance
        pass

    def debit_amount(self):
        # Functionality to debit amount
        pass

    def credit_amount(self):
        # Functionality to credit amount
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BankManagementSystem(root)
    root.mainloop()
