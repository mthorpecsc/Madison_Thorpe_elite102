import sqlite3
import time 
import string

no_punct = str.maketrans('','',string.punctuation)
conn = sqlite3.connect('banking_program.db')
cursor = conn.cursor()

#creating database 
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customer_Accounts (
               id SERIAL PRIMARY KEY,
               first_name TEXT,
               last_name TEXT,
               checkings_balance REAL,
               savings_balance REAL
               )
''')

def main():
    print() 
    print("Welcome to the Main Menu.")
    print('-'*25)
    print("1. View Accounts \n2. Update Account \n3. Create New Account \n4. Add to Account \n5. Withdraw from Account \n6. Delete Account \n7. Exit Program ")
    print('-'*25)

def view_accounts():
    print() 
    print("A list of all registered accounts.")
    print("-"*30)
    print("∥ID∥ ∥First Name∥ ∥Last Name∥ ∥Checkings Balance∥ ∥Savings Balance∥")

    cursor.execute('SELECT * FROM Customer_Accounts')
    rows = cursor.fetchall()
    for row in rows:
        print(row) 

    print("1. Main Menu \n2. Withdraw from Account \n3. Add to account")
    while True: #loops if invalid answers are given 
        user_choice = input("What would like to do next?: ").strip() 
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            main()
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            withdraw_account()
        elif user_choice == "3":
            print("Redirecting you shortly...")
            time.sleep(2)
            add_account()
        else:
            print(f"{user_choice} is not an option on the list.")
            print()
            
def update_accounts():
    print()
    
def create_account():
    print()
    print("Welcome to Account Creation.")

    while True: #makes sure that names aren't created with numbers or special characters 
        first_name = input("Enter the first name of the account holder: ").translate(no_punct)   
        if first_name.isalpha() == True:
            print()
            break 
        else:
            print() 
            print("Numbers and/or special characters are not allowed. Please try again.")

    while True: #makes sure last names aren't created with numbers or special characters 
        last_name = input("Enter the last name of the account holder: ").translate(no_punct)
        if last_name.isalpha() == True:
            print()
            break
        else:
            print() 
            print("Numbers and/or special characters are not allowed. Please try again.")

    while True: #ensures checking and savings balances are numbers only 
        try: 
            checking_balance = float(input("Enter the initial checkings balance: "))
        except ValueError:
            print("Please type in a valid float or integer.")
        try: 
            savings_balance = float(input("Enter the initial savings balance: "))
        except ValueError:
            print("Please type in a valid float or integer.")
        break

    #creates new bank account based on info above 
    cursor.execute(f'''INSERT INTO Customer_Accounts (first_name, last_name, checkings_balance, savings_balance) 
                   VALUES ('{first_name}','{last_name}',{checking_balance},{savings_balance})
                   ''')
    print("Creating account...Please keep screen on")
    time.sleep(3)
    print("Account Successfully Created!")
    conn.commit()

    print("What would you like to do next? \n1. Create another Account \n2. Go back to Main Menu")
    
    #sends users back to account creation or the main menu 
    while True:
        answer = input(": ")
        if answer == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            create_account()
            break
        elif answer == "2":
            print("Redirecting you to main menu...")
            time.sleep(2)
            main() 
            break
        else:
            print()
            print(f"{answer} is not an option on the list")
                    
def withdraw_account():
    print()
    
def add_account():
    print()

def delete_account():
    print()

#create_account()
view_accounts()