import csv
import datetime
import userInput
import sys
import time
import Anim

main_headers = ["User Name","ID Number","Credit Card Number","Credit Card Password","Pizza Name","Pizza Description","Date"]

def addHeaders():
    with open("Orders_Database.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(main_headers)
 
# This function is used for checking if the user has data in Orders_Database.csv 
def checkUser(idNumber):
    with open("Orders_Database.csv", "r") as file:
        reader = csv.reader(file)
        thereIs = False
        
        for row in reader:
            if row[0] == "User Name":
                continue
            if row[1] == idNumber:
                thereIs = True

        return thereIs        

# This function is used for finding the user from Orders_Database.csv
def findUser(idNumber):
    with open("Orders_Database.csv", "r") as file:
        Info = [" "," "]

        for row in csv.reader(file):
            if row[0] == "User Name":
                continue
            if row[1] == idNumber:
                Info[0] = row[2]
                Info[1] = row[3]
        return Info        

# This function is used for adding user's detailed information to Orders_Database.csv
def addInformation(infoList):

    # Adding information to "Orders_Database.csv"
    with open("Orders_Database.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(infoList)

# This function is used for some operations for the Customer. 
# Mainly used for accepting information from the customer (or user)
# If the user wants to add his/her detailed information to save in the database (Orders_Database.csv),
# function will give this chance. Also this is true for the opposite situation.

def addToDatabase():
    print("\n--------------------------------------------------------------")
    print("Please, enter the information to pay for the order [required] ")
    
    dateOfOrder = datetime.datetime.now()
    userName = input("~ Name/Surname : ")
    idNumber = input("~ ID number (Turkish Identity Number) : ")
    hasAccount = checkUser(idNumber)
    
    # Small animation :
    Anim.AnimCheck(hasAccount)    

    sys.stdout.write("\033[F")  # Move cursor up one line
    sys.stdout.write("\033[K")  # Clear the line
    
    if hasAccount == True:
        setAccount = input("Do you want to pay with a pre-registered card ? (yes - 'enter' , no - 'n') : ")
        if setAccount == "n":
            cc_number = input("~ Credit Card Number : ")
            cc_password = input("~ Credit Card Password : ")

        else:
            cc_number = findUser(idNumber)[0]
            cc_password = findUser(idNumber)[1]
    
    else:
        print("\n+ Please enter the required information for payment:")
        cc_number = input("~ Credit Card Number : ")
        cc_password = input("~ Credit Card Password : ")

    choice = input("Do you want to save your detailed information ? (yes - 'enter' , no - 'n') : ")
    if choice == 'n':
        Anim.AnimPayment()
        Anim.clear_screen()
        print("Thanks for choosing us. We hope to see you in your future visits :)")
        sys.exit()

    else:    
        orderDescription = userInput.basePizza.get_description()
        pizzaName = f"'{userInput.basePizza._pizza_description[0]}' + '{userInput.withSaucePizza._description}'"
    
        if userInput.extraSaucePizza is not None:
            if userInput.withSaucePizza._description == userInput.extraSaucePizza._description:
                pizzaName += f" + '{userInput.extraSaucePizza._description}' (double extra)"    
            else:
                pizzaName += f" + '{userInput.extraSaucePizza._description}' (extra)"
    
        infoList = [userName, idNumber, cc_number, cc_password, pizzaName, orderDescription, dateOfOrder]
        # Adding information of the user to the database (Orders_Database.csv)
        
        Anim.AnimPayment()
        Anim.clear_prev_lines()
        
        addInformation(infoList)
        print("Data entered into the system")
        time.sleep(0.7)
        Anim.clear_screen()
        print("Thank you for choosing us. Our goal is to provide an invaluable service :D")