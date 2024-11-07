#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BankAccount:
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        
    def get_balance(self):
        print(f"Account Balance: {self.balance}")
        return self.balance

    def get_transaction_fee(self, amount):
        transaction_fee = amount * 0.0001
        print(f"Transaction fee for withdrawal of {amount}: {transaction_fee}")
        return transaction_fee

    def get_transaction_bonus(self, amount):
        bonus = amount * 0.0001
        print(f"Transaction bonus for deposit of {amount}: {bonus}")
        return bonus

    def deposit(self, amount):
        if amount > 0:
            bonus = amount * 0.0001  # 0.0001 percentage bonus
            self.balance += (amount + bonus)
            print(f"Deposited: {amount}, Bonus: {bonus}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            transaction_fee = amount * 0.0001  # 0.0001 percentage fee
            total_withdrawal = amount + transaction_fee
            if self.balance >= total_withdrawal:
                self.balance -= total_withdrawal
                print(f"Withdrawn: {amount}, Transaction Fee: {transaction_fee}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
            
    


# In[12]:


accounts = {
    "123456789": BankAccount("Alice", "123456789", "1111", 1000),
    "987654321": BankAccount("Bob", "987654321", "2222", 500),
    "555555555": BankAccount("Charlie", "555555555", "3333", 1500),
    "111222333": BankAccount("David", "111222333", "4444", 2000),
    "444555666": BankAccount("Eva", "444555666", "5555", 750),
    "777888999": BankAccount("Frank", "777888999", "6666", 1200),
    "999888777": BankAccount("Grace", "999888777", "7777", 300),
    "222333444": BankAccount("Hannah", "222333444", "8888", 950),
    "888777666": BankAccount("Ian", "888777666", "9999", 4000),
    "333444555": BankAccount("Jack", "333444555", "0000", 650),
    "666555444": BankAccount("Kira", "666555444", "1234", 120),
    "555444333": BankAccount("Liam", "555444333", "4321", 850),
    "444333222": BankAccount("Mia", "444333222", "5678", 780),
    "222111000": BankAccount("Nora", "222111000", "8765", 920),
}





# In[ ]:


#to update the account details whenever required
def add_account(name, account_number, pin, balance=0):
    if account_number not in accounts:
        accounts[account_number] = BankAccount(name, account_number, pin, balance)
        print(f"Account for {name} created successfully.")
    else:
        print("Account number already exists!")


# In[16]:


# Check if the account exists and if the pin matches
def authenticate(account_number, pin):
    
    return accounts.get(account_number) if accounts.get(account_number) and accounts.get(account_number).pin == pin else None

#input account number and PIN
account_number = input("Enter your account number: ")
pin = input("Enter your PIN: ")


user_account = authenticate(account_number, pin)


if user_account:
    
    print(f"\n--- Welcome {user_account.name} ---")
    user_account.get_balance()    # Show the initial balance

    
    print("Press 1 for Withdrawal\n")
    print("Press 2 for Deposit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        amount = float(input("Enter the amount to withdraw: "))
        user_account.withdraw(amount)  #  withdrawal
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        user_account.deposit(amount)  #  deposit
    else:
        print("Invalid choice!")

   
    print("\n--- Updated Balance ---")
    user_account.get_balance() # Show the updated balance
else:
    print("Authentication failed! Invalid account number or PIN.")


# In[14]:


#example


add_account("Jeeva", "987582102", "1212", balance=0)


# In[ ]:




