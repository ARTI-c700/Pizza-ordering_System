import Main

basePizza = None
withSaucePizza = None
extraSaucePizza = None

def selectPizza(base, sauce, select):
    global basePizza
    global withSaucePizza
    global extraSaucePizza
    
    if base == "1":
        basePizza = Main.Classic()
        selectSauce(sauce, select)

    elif base == "2":
        basePizza = Main.Margherita()       
        selectSauce(sauce, select)

    elif base == "3":
          basePizza = Main.TurkPizza()
          selectSauce(sauce, select)
    elif base == "4":
          basePizza = Main.PlainPizza()
          selectSauce(sauce, select)  


def selectSauce(sauce, select):
    global withSaucePizza
    global extraSaucePizza

    if sauce == "11":
            if select == None:
                  withSaucePizza = Main.Olives(basePizza)
            else:
                  extraSaucePizza = Main.Olives(basePizza)

    elif sauce == "12":
            if select == None:
                  withSaucePizza = Main.Mushrooms(basePizza)
            else:
                  extraSaucePizza = Main.Mushrooms(basePizza)

    elif sauce == "13":
            if select == None:
                  withSaucePizza = Main.GoatCheese(basePizza)
            else:
                  extraSaucePizza = Main.GoatCheese(basePizza)
    
    elif sauce == "14":
            if select == None:
                  withSaucePizza = Main.Meat(basePizza)
            else:
                  extraSaucePizza = Main.Meat(basePizza)

    elif sauce == "15":
            if select == None:
                  withSaucePizza = Main.Onions(basePizza)
            else:
                  extraSaucePizza = Main.Onions(basePizza)      
    elif sauce == "16":
            if select == None:
                  withSaucePizza = Main.Corn(basePizza)
            else:
                  extraSaucePizza = Main.Corn(basePizza)    
          

