import sqlite3
import time 
import string
import json 
import os 

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

#holds transcation history 
def transcation_history():
    print()
    print("==Transcation History==")
    with open('transcation.json', 'r') as f:
        transcation_history = json.load(f)
    
    for transcation in transcation_history:
        print(transcation)
 
def main():
    print() 
    print("==Welcome to the Main Menu.==")
    print('-'*25)
    print("1. View Accounts \n2. Update Account \n3. Create New Account \n4. Add to Account \n5. Withdraw from Account \n6. Delete Account \n7. Transcation History \n8. Exit Program ")
    print('-'*25)

    while True:
        user_choice = input(": ")
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            view_accounts()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            update_accounts()
            break
        elif user_choice == "3":
            print("Redirecting you shortly...")
            time.sleep(2)
            create_account()
            break
        elif user_choice == "4":
            print("Redirecting you shortly...")
            time.sleep(2)
            add_money_account()
            break
        elif user_choice == "5":
            print("Redirecting you shortly...")
            time.sleep(2)
            withdraw_account()
            break
        elif user_choice == "6":
            print("Redirecting you shortly...")
            time.sleep(2)
            delete_account()
            break
        elif user_choice == "7":
            transcation_history()
            break
        elif user_choice == "8":
            print("Program Closed.")
            break 
        else:
            print("Invalid input. Please choose an option from the list.")

#create, update, and view account functions
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
        user_choice = input("What would like to do next?: ").strip().translate(no_punct)
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
            add_money_account()
        else:
            print("Invalid input. Please choose an option on the list.")
            
def update_accounts():
    print()
    print("Update Accounts Page")

    while True:
        user_choice = input("What would you like to update? \n1. First Name \n2. Last Name \n: ").strip().translate(no_punct)

        if user_choice == "1":
            while True:
                first_name = input("What would you like to update the first name to?: ").translate(no_punct).strip()
                if first_name.isalpha() == True:
                    break
                else:
                    print("Name cannot include special characters or numbers.")
                    print() 

            while True:
                try: 
                    id = int(input("Provide the account id: "))
                    cursor.execute(f"SELECT * FROM Customer_Accounts WHERE id = {id}")
                    rows = cursor.fetchall()
                    if len(rows) == 0: #makes user input a new id if an account is not found with the one given 
                        print("No account found with this id.")
                    else:  
                        cursor.execute(f"UPDATE Customer_Accounts SET first_name = '{first_name}' WHERE id = {id}") 
                        conn.commit()
                        print()
                        break
                except ValueError:
                    print("Invalid id given.")
               
        elif user_choice == "2":
            while True:
                last_name = input("What would you like to update the last name to?: ").translate(no_punct).strip() 
                if last_name.isalpha() == True:
                    break
                else:
                    print("Name cannot include special characters or numbers.")
                    print() 

            while True:
                try: 
                    id = int(input("Provide the account id: "))
                    cursor.execute(f"SELECT * FROM Customer_Accounts WHERE id = {id}")
                    rows = cursor.fetchall()
                    if len(rows) == 0: #makes user input a new id if an account is not found with the one given 
                        print("No account found with this id.")
                    else:
                        cursor.execute(f"UPDATE Customer_Accounts SET last_name = '{last_name}' WHERE id = {id}") 
                        conn.commit()
                        print()
                        break
                except ValueError:
                    print("Invalid id given.")
        else:
            print(f"{user_choice} is not on the list")
            print()
        break

    print("Account Sucessfully updated!")
    print("-"*30)
    cursor.execute(f"SELECT * FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        print(row) 

    time.sleep(3)
    print()
    user_choice = input("What would you like to do next? \n1. Update Account \n2. Main Menu \n: ")
    while True:
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            update_accounts()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2) 
            main()
            break
        else:
            print("Invalid Input. Please pick an option from the list.")
      
def create_account():
    print()
    print("Welcome to Account Creation.")

    while True: #makes sure that names aren't created with numbers or special characters 
        first_name = input("Enter the first name of the account holder: ").translate(no_punct).strip()   
        if first_name.isalpha() == True:
            print()
            break 
        else:
            print() 
            print("Numbers and/or special characters are not allowed. Please try again.")

    while True: #makes sure last names aren't created with numbers or special characters 
        last_name = input("Enter the last name of the account holder: ").translate(no_punct).strip()
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
        answer = input(": ").translate(no_punct).strip() 
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
            print("Invalid Input. Please choose an option on the list")

#withdraw functions 
def withdraw_account():
    print()
    print("===Welcome to the Withdraw Account Page.=== ")
    print("Where would you like to withdraw from?")
    print("1. Checkings Account")
    print("2. Savings Account")
    while True:
        user_choice = input(": ").translate(no_punct).strip() 
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            withdraw_checkings()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            withdraw_savings()
            break
        else:
            print("===Invalid Option Choice. Please choose from the list.===")

def withdraw_savings():
    while True:
        try:
            id = int(input("==Enter Id==: "))
            cursor.execute(f"SELECT * FROM Customer_Accounts WHERE id = {id}")
            rows = cursor.fetchall()
            if len(rows) == 0: #makes user input a new id if an account is not found with the one given 
                print("No account found with this id.")
            else:
                break
        except ValueError:
            print("Invalid Input. Please enter a valid id.")

    while True:
        try:
            withdraw = float(input("==Withdrawl Amount==: "))
            cursor.execute(f"SELECT savings_balance FROM Customer_Accounts WHERE id = {id}")
            rows = cursor.fetchall()
            for row in rows:
                balance = int(float(''.join(map(str, list(row))))) #turns it into an integer 
            if balance >= withdraw:
                break
            else:
                print("===Insufficient Funds.===")
                print("You can not withdraw more than what you have.")
        except ValueError:
            print("Invalid Input. Please enter an integer.")

    new_balance = balance - withdraw #math for updated balance 
    cursor.execute(f"UPDATE Customer_Accounts SET savings_balance = {new_balance} WHERE id = {id}")
    conn.commit()
    print("==Withdraw Successful!==")
    cursor.execute(f"SELECT savings_balance FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Updated Balance: {row}")
    
    #grabs the first name of the customer and turns it into a string 
    cursor.execute(f"SELECT first_name FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        first_name = (''.join(map(str, list(row))))

    #grabs the last name of a customer and turns it into a string 
    cursor.execute(f"SELECT last_name FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        last_name = (''.join(map(str, list(row))))

    #gets the time transcation was made 
    current_time = time.asctime()
   
    transcation = f"${withdraw} withdrawl from {first_name} {last_name}'s account on {current_time}"
    if os.path.exists("transcation.json"):
        with open("transcation.json", "r") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(transcation)

    with open('transcation.json','w') as f:
        json.dump(data, f, indent=4)
    
    print()
    print("==What would you like to do next?==")
    print("1. Main Menu")
    print("2. Go Back To Withdraw Accounts Page")
    
    while True:
        user_choice = input(": ").strip().translate(no_punct)
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            main()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            withdraw_account()
            break
        else:
            print("Invalid choice. Please choose an option from the list.")
            print()

def withdraw_checkings():
    while True:
        try:
            id = int(input("==Enter Id==: "))
            cursor.execute(f"SELECT * FROM Customer_Accounts WHERE id = {id}")
            rows = cursor.fetchall()
            if len(rows) == 0: #makes user input a new id if an account is not found with the one given 
                print("No account found with this id.")
            else:
                break
        except ValueError:
            print("Invalid Input. Please enter a valid id.")

    while True:
        try:
            withdraw = float(input("==Withdrawl Amount==: "))
            cursor.execute(f"SELECT checkings_balance FROM Customer_Accounts WHERE id = {id}")
            rows = cursor.fetchall()
            for row in rows:
                #turns it into a list so it can be later turned into an integer 
                balance = int(float(''.join(map(str, list(row))))) #turns it into an integer 
            if balance >= withdraw:
                break
            else:
                print("===Insufficient Funds.===")
                print("You can not withdraw more than what you have.")

        except ValueError:
            print("Invalid Input. Please enter an integer.")

    new_balance = balance - withdraw #math for updated balance 
    cursor.execute(f"UPDATE Customer_Accounts SET checkings_balance = {new_balance} WHERE id = {id}")
    conn.commit()
    print("==Withdraw Successful!==")
    cursor.execute(f"SELECT checkings_balance FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Updated Balance: {row}")
    
    #grabs the first name of the customer and turns it into a string 
    cursor.execute(f"SELECT first_name FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        first_name = (''.join(map(str, list(row))))

    #grabs the last name of a customer and turns it into a string 
    cursor.execute(f"SELECT last_name FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        last_name = (''.join(map(str, list(row))))

    #gets the time transcation was made 
    current_time = time.asctime()

    #saves the transcation history to a file 
    transcation = f"${withdraw} withdrawl from {first_name} {last_name}'s account on {current_time}"
    if os.path.exists("transcation.json"):
        with open("transcation.json", "r") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(transcation)

    with open('transcation.json','w') as f:
        json.dump(data, f, indent=4)
   
   
    
    print()
    print("==What would you like to do next?==")
    print("1. Main Menu")
    print("2. Go Back To Withdraw Accounts Page")
    
    while True:
        user_choice = input(": ").strip().translate(no_punct)
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            main()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            withdraw_account()
            break
        else:
            print("Invalid choice. Please choose an option from the list.")
            print()

#deposit functions 
def add_money_account():
    print()
    print("==Deposit Account Page==")
    print("What type of account would you like to add to?")
    print("1. Checkings Account")
    print("2. Savings Account")
    
    while True:
        user_choice = input(": ")
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            add_checkings()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            add_savings()
            break
        else:
            print("Invalid input. Please choose an option from the list.")

def add_savings():
    print()
    while True:
        try:
            deposit = float(input("==Deposit Amount==: "))
            break
        except ValueError:
            print("Invalid Input. Please enter an integer.")

    while True:
        try:
            id = int(input("==Enter Id==: "))
            cursor.execute(f"SELECT * FROM Customer_Accounts WHERE id = {id}")
            rows = cursor.fetchall()
            if len(rows) == 0: #makes user input a new id if an account is not found with the one given 
                print("No account found with this id.")
            else:
                break
        except ValueError:
            print("Invalid Input. Please enter a valid id.")

    cursor.execute(f"SELECT savings_balance FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        list_r = list(row) #turns it into a list so it can be later turned into an integer 
    balance = int(float(''.join(map(str, list_r)))) #turns it into an integer 

    
    new_balance = balance + deposit #math for updated balance 
    cursor.execute(f"UPDATE Customer_Accounts SET savings_balance = {new_balance} WHERE id = {id}")
    conn.commit()
    print("==Deposit Successful!==")
    cursor.execute(f"SELECT savings_balance FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Updated Balance: {row}")
    
    #grabs the first name of the customer and turns it into a string 
    cursor.execute(f"SELECT first_name FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        first_name = (''.join(map(str, list(row))))

    #grabs the last name of a customer and turns it into a string 
    cursor.execute(f"SELECT last_name FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        last_name = (''.join(map(str, list(row))))

    #gets the time transcation was made 
    current_time = time.asctime()
   
    transcation = f"${deposit} deposit in {first_name} {last_name}'s savings account on {current_time}"
    if os.path.exists("transcation.json"):
        with open("transcation.json", "r") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(transcation)

    with open('transcation.json','w') as f:
        json.dump(data, f, indent=4)
    
    
    print()
    print("==What would you like to do next?==")
    print("1. Main Menu")
    print("2. Go Back Add Accounts Page")
    
    while True:
        user_choice = input(": ").strip().translate(no_punct)
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            main()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            add_money_account()
            break
        else:
            print("Invalid choice. Please choose an option from the list.")
            print()

def add_checkings():
    print()
    while True:
        try:
            deposit = float(input("==Deposit Amount==: "))
            break
        except ValueError:
            print("Invalid Input. Please enter an integer.")

    while True:
        try:
            id = int(input("==Enter Id==: "))
            cursor.execute(f"SELECT * FROM Customer_Accounts WHERE id = {id}")
            rows = cursor.fetchall()
            if len(rows) == 0: #makes user input a new id if an account is not found with the one given 
                print("No account found with this id.")
            else:
                break
        except ValueError:
            print("Invalid Input. Please enter a valid id.")

    cursor.execute(f"SELECT checkings_balance FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        list_r = list(row) #turns it into a list so it can be later turned into an integer 
    balance = int(float(''.join(map(str, list_r)))) #turns it into an integer 

    
    new_balance = balance + deposit #math for updated balance 
    cursor.execute(f"UPDATE Customer_Accounts SET checkings_balance = {new_balance} WHERE id = {id}")
    conn.commit()
    print("==Deposit Successful!==")
    cursor.execute(f"SELECT checkings_balance FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Updated Balance: {row}")
    
    #grabs the first name of the customer and turns it into a string 
    cursor.execute(f"SELECT first_name FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        first_name = (''.join(map(str, list(row))))

    #grabs the last name of a customer and turns it into a string 
    cursor.execute(f"SELECT last_name FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        last_name = (''.join(map(str, list(row))))

    #gets the time transcation was made 
    current_time = time.asctime()
   
    transcation = f"${deposit} deposit in {first_name} {last_name}'s checkings account on {current_time}"
    if os.path.exists("transcation.json"):
        with open("transcation.json", "r") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(transcation)

    with open('transcation.json','w') as f:
        json.dump(data, f, indent=4)
    
    print()
    print("==What would you like to do next?==")
    print("1. Main Menu")
    print("2. Go Back To Add Acounts Page")
    
    while True:
        user_choice = input(": ").strip().translate(no_punct)
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            main()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            add_money_account() 
            break
        else:
            print("Invalid choice. Please choose an option from the list.")
            print()

#delete account function 
def delete_account():

    print()
    print("==Delete Account Page==")
    while True:
        try:
            id = int(input("Enter the account id: "))
            break
        except ValueError:
            print("Invalid Input. Please enter an integer.")

    cursor.execute(f"SELECT * FROM Customer_Accounts WHERE id = {id}")
    rows = cursor.fetchall()
    for row in rows:
        print(f"=={row}==")

    while True:
        confirmation = input("Are you sure you wish to delete this account? (y/n): ").strip().translate(no_punct).lower() 
        if confirmation == 'y':
            cursor.execute(f"DELETE FROM Customer_Accounts WHERE id = {id}")
            conn.commit()
            print("==Account sucessfully deleted!==")
            break
        elif confirmation == 'n':
            print("==Account Deletion Canceled==")
            break
        else:
            print("Invalid Choice. Please use 'y' or 'n'")
            print()

    print()
    print("==What would you like to do next?==")
    print("1. Main Menu")
    print("2. Go Back To Delete Account Page")
    
    while True:
        user_choice = input(": ").strip().translate(no_punct)
        if user_choice == "1":
            print("Redirecting you shortly...")
            time.sleep(2)
            main()
            break
        elif user_choice == "2":
            print("Redirecting you shortly...")
            time.sleep(2)
            delete_account() 
            break
        else:
            print("Invalid choice. Please choose an option from the list.")
            print()

main() 