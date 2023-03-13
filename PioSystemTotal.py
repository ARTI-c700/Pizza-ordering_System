import sys 
import time
import os
import csv
import datetime

# File : py |------------------------------------------------------- 

def AnimPayment():
    print("Payment process ")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process .")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process ..")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process ...")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process .. ")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process .  ")
    time.sleep(0.5)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process    ")
    time.sleep(0.5)
    print("Success !")
    time.sleep(0.5)


def AnimCheck(hasAccount):
    print("Checking if the user is in the system : ")
    sys.stdout.write("\033[F")  # Move cursor up one line
    time.sleep(0.5) # Delay process only 0.5 second
    print("Checking if the user is in the system : ", hasAccount)
    time.sleep(0.8)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_prev_lines():
    sys.stdout.write("\033[F")  # Move cursor up one line
    sys.stdout.write("\033[K")  # Clear the line

 # -------------------------------------------------------------------------


 # File : importMenu.py |---------------------------------------------------

listOfText = [
        "** Please Choose a Pizza Base: ",
        "\n1: Classic ",
        "\n2: Margherita ",
        "\n3: TurkPizza ",
        "\n4: PlainPizza ",
        "\n\n* and sauce of your choice: ",
        "\n11: Olives ",
        "\n12: Mushrooms ",
        "\n13: GoatCheese ",
        "\n14: Meat ",
        "\n15: Onions ",
        "\n16: Corn ",
        "\n\n* Thank you!"
    ]
def importTheMenu(listOfText): 
    with open("Menu.txt", "w+") as menuFile:
        menuFile.writelines(listOfText)
    menuFile.close()
 # -------------------------------------------------------------------------




 # File : py |----------------------------------------------------

basePizza = None
withSaucePizza = None
extraSaucePizza = None

def selectPizza(base, sauce, select):
    global basePizza
    global withSaucePizza
    global extraSaucePizza
    
    if base == "1":
        basePizza = Classic()
        selectSauce(sauce, select)

    elif base == "2":
        basePizza = Margherita()       
        selectSauce(sauce, select)

    elif base == "3":
          basePizza = TurkPizza()
          selectSauce(sauce, select)
    elif base == "4":
          basePizza = PlainPizza()
          selectSauce(sauce, select)  


def selectSauce(sauce, select):
    global withSaucePizza
    global extraSaucePizza

    if sauce == "11":
            if select == None:
                  withSaucePizza = Olives(basePizza)
            else:
                  extraSaucePizza = Olives(basePizza)

    elif sauce == "12":
            if select == None:
                  withSaucePizza = Mushrooms(basePizza)
            else:
                  extraSaucePizza = Mushrooms(basePizza)

    elif sauce == "13":
            if select == None:
                  withSaucePizza = GoatCheese(basePizza)
            else:
                  extraSaucePizza = GoatCheese(basePizza)
    
    elif sauce == "14":
            if select == None:
                  withSaucePizza = Meat(basePizza)
            else:
                  extraSaucePizza = Meat(basePizza)

    elif sauce == "15":
            if select == None:
                  withSaucePizza = Onions(basePizza)
            else:
                  extraSaucePizza = Onions(basePizza)      
    elif sauce == "16":
            if select == None:
                  withSaucePizza = Corn(basePizza)
            else:
                  extraSaucePizza = Corn(basePizza)

 # ----------------------------------------------------------------------------------------------------------------------- 

 # File : OrdersTable.py |------------------------------------------------------------------------------------------------

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
    AnimCheck(hasAccount)    

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
        AnimPayment()
        clear_screen()
        print("Thanks for choosing us. We hope to see you in your future visits :)")
        sys.exit()

    else:    
        orderDescription = basePizza.get_description()
        pizzaName = f"'{basePizza._pizza_description[0]}' + '{withSaucePizza._description}'"
    
        if extraSaucePizza is not None:
            if withSaucePizza._description == extraSaucePizza._description:
                pizzaName += f" + '{extraSaucePizza._description}' (double extra)"    
            else:
                pizzaName += f" + '{extraSaucePizza._description}' (extra)"
    
        infoList = [userName, idNumber, cc_number, cc_password, pizzaName, orderDescription, dateOfOrder]
        # Adding information of the user to the database (Orders_Database.csv)
        
        AnimPayment()
        clear_prev_lines()
        
        addInformation(infoList)
        print("Data entered into the system")
        time.sleep(0.7)
        clear_screen()
        print("Thank you for choosing us. Our goal is to provide an invaluable service :D")

 # -----------------------------------------------------------------------------------------------------------------------

 # File : py |------------------------------------------------------------------------------------------------------------


# Creating process of superclass -> "Pizza"
class Pizza():
    def __init__(self, description, cost):
        self._description = description  # encapsulated attribute
        self._cost = cost  # encapsulated attribute

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost

# Classes for Pizza base are subclass of Pizza class
# Pizza class's constructor is used for these subclasses for using Pizza's methods e.g get_description() method 

# Creating subclass "Classic"        
class Classic (Pizza):
    _pizza_description = ["Classic Pizza","Tomatoes, Mozzarella and of course Basil"] # Description for Classic Pizza
    _pizza_cost = 100.00 # Cost of Classic Pizza
    
    def __init__(self, description = _pizza_description[1], cost = _pizza_cost):
        super().__init__(description, cost) 

# Creating subclass "Margherita"
class Margherita (Pizza):
    _pizza_description = ["Margherita Pizza","Tomatoes, Mozzarella, Basil, Olive Oil"] # Description for Margherita Pizza
    _pizza_cost = 119.00 # Cost of Margherita Pizza

    def __init__(self, description = _pizza_description[1], cost = _pizza_cost):
        super().__init__(description, cost)

# Creating subclass "TurkPizza"
class TurkPizza (Pizza):
    _pizza_description = ["Turk Pizza","Mozzarella, Sausage, also Green Pepper"] # Description for Turk Pizza
    _pizza_cost = 165.55 # Cost of Turk Pizza

    def __init__(self, description = _pizza_description[1], cost = _pizza_cost):
        super().__init__(description, cost) 

# Creating subclass "Plain Pizza"
class PlainPizza (Pizza):
    _pizza_description = ["Plain Pizza","Pizza cheese, Red strip pepper, Thyme"] # Description for Plain Pizza
    _pizza_cost = 100.00 # Cost of Plain Pizza

    def __init__(self, description = _pizza_description[1], cost = _pizza_cost):
        super().__init__(description, cost)



# Creating superclass -> "Decorator" (also child class of "Pizza")
class Decorator(Pizza):
    # For initialization, i take 2 objects : Pizza base (e.g Classic, PlainPizza) and Pizza sauce as a component variable
    def __init__(self, BasePizza, component):
        self.BasePizza = BasePizza
        self.component = component
        
        # additional is used for extra sauce. When extra sauce is ordered it will added to additional variable
        self.additional = None

    # Description for Pizza with sauce
    def get_description(self):
        description = f"Pizza description: '{self.BasePizza.get_description()}' with '{self.component.get_description()}'"
        
        if self.additional is not None:
            if self.additional._description == self.component.get_description():
                description += f" + '{self.additional._description}' double sauce :D"
            else:
                description += f" + '{self.additional._description}'(extra) double sauces :D"

        else:
            description += " sauce :)"

        return description

    # calculating for Total cost
    def get_cost(self):
        cost = self.BasePizza.get_cost() + self.component.get_cost()
        
        if self.additional is not None:
            cost += self.additional._cost

        return f"Total cost : \033[4m{round(cost, 3)}\033[0m TL"

    # If extra sauce is ordered, program will use this method
    def addSauce(self, additional):
        self.additional = additional

# SubClasses take Decorator class's constructor. Description and cost have their values as a constant
# While Decorator's constructor is called, instances of the Pizza class is created with description and cost

# Creating subclass "Olives"
class Olives(Decorator):
    _description = "Olives"
    _cost = 15.45

    def __init__(self, BasePizza, description = _description, cost = _cost):
        super().__init__(BasePizza, Pizza(description, cost))

# Creating subclass "Mushrooms"
class Mushrooms(Decorator):
    _description = "Mushrooms"
    _cost = 14.90
    
    def __init__(self, BasePizza, description = _description, cost = _cost):
        super().__init__(BasePizza, Pizza(description, cost))

# Creating subclass "GoatCheese"
class GoatCheese(Decorator):
    _description = "Goat Cheese"
    _cost = 20.65
    
    def __init__(self, BasePizza, description = _description, cost = _cost):
        super().__init__(BasePizza, Pizza(description, cost))

# Creating subclass "Meat"
class Meat(Decorator):
    _description = "Meat"
    _cost = 30.55
    
    def __init__(self, BasePizza, description = _description, cost = _cost):
        super().__init__(BasePizza, Pizza(description, cost))

# Creating subclass "Onions"
class Onions(Decorator):
    _description = "Onions"
    _cost = 11.20
    
    def __init__(self, BasePizza, description = _description, cost = _cost):
        super().__init__(BasePizza, Pizza(description, cost))

# Creating subclass "Corn"
class Corn(Decorator):
    _description = "Corn"
    _cost = 16.00
    
    def __init__(self, BasePizza, description = _description, cost = _cost):
        super().__init__(BasePizza, Pizza(description, cost))


# Creating main function
def main():
    print("Welcome to Pizza Order System !")
    time.sleep(1)

    # To print contexts of the Menu to the Screen
    for i in listOfText:
        print(i[1:])

    extraSauce = None
    # To select Pizza Base, Sauce and extra sauce if required
    print("\nCustomer's choice:")
    
    pizza_base = input("1] Pizza Base -> ")
    sauce = input("2] Pizza Sauce -> ")
    selectPizza(pizza_base, sauce, extraSauce)
    saucePizza = withSaucePizza

    # Ask for the customer for extra sauce
    extraSauce = input("Do you want additional Sauce (yes - 'y' , no - 'enter') : ")
    
    # Clears previous line
    clear_prev_lines()
    
    if extraSauce == "y":
        print("Please, select extra sauce from the Menu : ")
        forExtra = input("3] Extra Sauce -> ")
        selectSauce(forExtra, extraSauce)
        sauceExtra = extraSaucePizza
        saucePizza.addSauce(sauceExtra)
    time.sleep(0.5)
    clear_screen()
    
    print("Information about the order : ")    
    print("::", saucePizza.get_description())
    print("::", saucePizza.get_cost())
    
    # Calling function of OrdersTable.py file
    time.sleep(0.3)
    addToDatabase()

if __name__ == '__main__':
    main()



