import time
import importMenu
import userInput
import OrdersTable
import Anim

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
    for i in importMenu.listOfText:
        print(i[1:])

    extraSauce = None
    # To select Pizza Base, Sauce and extra sauce if required
    print("\nCustomer's choice:")
    
    pizza_base = input("1] Pizza Base -> ")
    sauce = input("2] Pizza Sauce -> ")
    userInput.selectPizza(pizza_base, sauce, extraSauce)
    saucePizza = userInput.withSaucePizza

    # Ask for the customer for extra sauce
    extraSauce = input("Do you want additional Sauce (yes - 'y' , no - 'enter') : ")
    
    # Clears previous line
    Anim.clear_prev_lines()
    
    if extraSauce == "y":
        print("Please, select extra sauce from the Menu : ")
        forExtra = input("3] Extra Sauce -> ")
        userInput.selectSauce(forExtra, extraSauce)
        sauceExtra = userInput.extraSaucePizza
        saucePizza.addSauce(sauceExtra)
    time.sleep(0.5)
    Anim.clear_screen()
    
    print("Information about the order : ")    
    print("::", saucePizza.get_description())
    print("::", saucePizza.get_cost())
    
    # Calling function of OrdersTable.py file
    time.sleep(0.3)
    OrdersTable.addToDatabase()

if __name__ == '__main__':
    main()
