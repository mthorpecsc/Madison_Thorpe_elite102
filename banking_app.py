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
    print("Welcome to the Main Menu.")
    print('-'*25)
    print("1. View Accounts \n2. Update Account \n3. Create New Account \n4. Add to Account \n5. Withdraw from Account \n6. Delete Account \n7. Exit Program ")
    print('-'*25)

def view_accounts():
    cursor.execute('SELECT * FROM Customer_Accounts')

def update_accounts():
    print()
    
def create_account():
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
    answer = int(input(": "))
    match answer:
        case 1:
            print("Redirecting you shortly...")
            time.sleep(2)
            create_account()
        case 2:
            print("Redirecting you to main menu...")
            time.sleep(2)
            main() 
           
def withdraw_account():
    print()
    
def add_account():
    print()

def delete_account():
    print()

create_account()