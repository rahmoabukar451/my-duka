# TASK 1.Create a class called BankAccount with the attributes: - account number , balance , owner name , date opened 
# 2.Add some behaviour to the above class using the methods: - deposit() - withdraw() -display_info()
# 3.Create 2 BankAccount objects that can deposit , withdraw and display amount
from datetime import date
date_time = date.today()        
print(date_time)

import random
account_number = random.randint(100000,999999)

amount = float(input("Enter the amount to deposit: "))
withdraw_amount = float(input("Enter the amount to withdraw: "))

class BankAccount:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number =account_number
        self.balance = balance
        self.owner_name =owner_name
        self.date_opened = date_opened
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount     
        else:
            print("Invalid amount. Please enter a positive number.")    
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

    def display_info(self):
        print("Bank Account Information:")
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")
        print("-----------------------------")

account1 = BankAccount(account_number,amount,"Hillary",date_time)
account2 = BankAccount(account_number+1,amount,"Job",date_time)
account1.display_info()
account1.deposit(amount)
account1.withdraw(withdraw_amount)
account1.display_info()
account2.display_info()
account2.deposit(amount)
account2.withdraw(withdraw_amount)
account2.display_info()
