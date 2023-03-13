with open("Menu.txt", "w+") as menuFile:

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
    menuFile.writelines(listOfText)

menuFile.close()
