#Stephen Twomey
#R00163379

import random
import math

new_file = open("R00163379_bank.txt")
new_list = new_file.read().splitlines()
account_num = []
name = []
account_balance = []
for line in new_list:
    if line.isnumeric(): #checking to see if line is a number
        account_num.append(int(line))
    if line[0].isalpha(): #checking to see if line is letter
        name.append(line)
    else:
        account_balance.append(float(line)) #changing from line to float

def welcome(): #To welcome the customer
    print("welcome to your local credit union")
    print()

def open_account(name,account_num,account_balance): #This allows a person to open an account
    i = 0
    while i < len(account_num):
        if i == 0:
            new_num = random.randint(100000, 999999)  # generates a random 6 digit number
        if new_num != account_num[i]: # if number is not in list then a new account number is added
            i += 1
        else:
            i = 0 #resets loop
            print(account_num)
    ok = False
    while not ok:
        try:
            first_name = input("What is your first name? ")
            last_name = input("What is your last name? ")
            ok = len(first_name) > 0 and len(last_name) > 0 #This means that a person must enter initials
            if not ok:
                print("Don't forget your first and last name")
        except:
            print("enter your first and last name and no numbers")
        full_name = first_name +""+ last_name
        account_num.append(int(new_num)) #puts account number as integer
        name.append(full_name)
        account_balance.append(float(0)) #balance is entered as a float,0.00
        print("your account number is",new_num,"and thank you for making an account with us")

def close_account(account_num): #closes the persons account used pop instead of remove as removes the first occurrence of the  item if it exists on the list
    details_of_user = get_account_details()
    account_num.pop(details_of_user)
    account_balance.pop(details_of_user)
    name.pop(details_of_user)
    #tried to get ask the person for their account number and if it wasn't in the list it would not work, so left it out

def withdraw_money(): #This function allows a person to withdraw money but nothing less than zero euro
    details_of_user = get_account_details()
    ok = False
    while not ok:
        try:
            remove_money = float(input("How much money would you like to withdraw? "))
            balance_left = float(account_balance[details_of_user]) - remove_money# gets the balance minus money that the person wants to remove
            ok = balance_left >= 0  #You must have more than zero euro remaining after taking out money
            if not ok:
                print("You don't have enough money in your account or you used negative numbers")
        except:
            print("use numbers only")
    account_balance[details_of_user] = float(format(balance_left, ".2f"))#gets new balance to 2 digits example 59.73
    print("You're new balance is", account_balance[details_of_user])

def deposit_money(): #This function allows a person to deposit money
    details_of_user = get_account_details()
    ok = False
    while not ok:
        try:
            deposit = float(input("How much money would you like to deposit? "))
            ok = deposit > 0  # cant deposit a negative number
            if not ok:
                print("you can't deposit a negative amount of money")
        except:
            print("use numbers only")
        account_balance[details_of_user] = account_balance[details_of_user] + float(format(deposit, ".2f")) #gets the new account balance after putting in money
        print("You're new balance is", account_balance[details_of_user])

def Generate_a_report_for_management(): #generates a report for the credit union
    persons_largest_deposit = ""
    largest_deposit = math #gets largest deposit
    k = 0
    while k < len(name):
        print("name of person: ",name[k],"account number is: ",account_num[k],"bank balance is: ",account_balance[k])
        if account_balance[k] > largest_deposit:# if largest deposit is less than a different account balance then that account balance becomes the largest deposit
            largest_deposit = account_balance[k]
            persons_largest_deposit = name[k]
        elif largest_deposit == account_balance[k]:
            persons_largest_deposit = name[k]
        k +=1
    total_deposited = sum(account_balance)
    print("The total amount of money deposited is:", total_deposited)
    print("largest deposit is:", largest_deposit, "person with largest account balance is:", persons_largest_deposit)

def quit():
    file = open("R00163379_bank.txt", "w")#writes to R00163379_bank.txt file, w writes to file
    file.write(str(account_num) + "\n")#converts to string
    file.write(str(account_balance)+"\n")#converts to string
    file.write(str(name)+ "\n")#converts to string
    file.close()# closes the file
    #The "\n" is important as it brings the code to a new line took me a while to find out

def options(): #This function allows a person to choose 1 of 6 options
    print("What would you like to do?")
    print("1. Open an account")
    print("2. Close your account")
    print("3. Withdraw money")
    print("4. Deposit money")
    print("5. Generate a report for management ")
    print("6. quit")
    options_for_acc = int(input(">>> "))

    while True:
        if options_for_acc == 1:
            open_account(account_num,account_balance,name)
        elif options_for_acc == 2:
            close_account(account_num)
        elif options_for_acc == 3:
            withdraw_money()
        elif options_for_acc == 4:
            deposit_money()
        elif options_for_acc == 5:
            Generate_a_report_for_management()
        elif options_for_acc == 6:
            quit()
            break #stops the loop
        else:
            print("please pick a number between 1 and 6")
        print("What would you like to do next?")
        options_for_acc = int(input(">>> "))

def get_account_details(): #This function asks for the persons account number
    ok = False
    while not ok:
        try:
            num = int(input("What is your six digit account number? "))
            ok = 100000 <= num <= 999999
            if not ok:
                print("sorry that number will not work")
        except:
            print("error, please enter six digits and no letters")
    details_of_user=account_num.index(num) #index returns the position of the item
    return details_of_user

def main():
    welcome()
    get_options = options()

main()