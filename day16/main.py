while True:

    coffee:str = input("Choose between espresso, latte or cappucino: ")
    if coffee == "espresso" or coffee == "latte" or coffee == "cappucino":
        print("Please insert coins.")
        quarter:str = input("How many quarters?: ")
        dime:str = input("How many dimes?: ")
        nickle:str = input("How many nickles?: ")
        penny:str = input("How many pennies?: ")
        print(f"Here is your {coffee}. Enjoy!")
        continue
    elif coffee == "off":
        print("Have a good one!")
        break
    else:
        print("Type the correct word")
        continue