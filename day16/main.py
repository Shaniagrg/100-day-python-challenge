class Machine:
    brand:str = "coffee machine"
    espresso:float = 3.25
    latte:float = 4.50
    cappaucino:float = 5.20
    @classmethod
    def coin(cls, money:float = 0.0)->float:
        quarter:int = int(input("How many quarters?: "))
        dime:int = int(input("How many dimes?: "))
        nickle:int = int(input("How many nickles?: "))
        penny:int = int(input("How many pennies?: "))
        converted_value:float = cls.convert(quarter,dime,nickle,penny,money)
        return converted_value
    
    @classmethod
    def convert(cls,quarter:float,dime:float,nickle:float,penny:float,money:float) -> float:
        convert_quarter:float = quarter * 0.25 
        convert_dime:float = dime * 0.1
        convert_nickle:float = nickle * 0.05
        convert_penny:float = penny * 0.01
        total_convert:float = convert_quarter + convert_nickle + convert_dime + convert_penny + money
        return total_convert
    


while True:

    coffee:str = input("Choose between espresso, latte or cappucino: ")
    if coffee == "espresso" or coffee == "latte" or coffee == "cappucino":
        print("Please insert coins.")
        user_money:float = Machine.coin()
        change:float = 0.0
        while True:
            if coffee == "espresso" and user_money > Machine.espresso:
                change = user_money - Machine.espresso
                break
            elif coffee == "latte" and user_money > Machine.latte:
                change = user_money - Machine.latte
                break
            elif coffee == "cappucino" and user_money > Machine.cappaucino:
                change = user_money - Machine.cappaucino
                break
            else:
                print("Add more money!")
                print(f"You have ${user_money}")
                user_money = Machine.coin(user_money)
                continue
        print(f"Here's your change {change}.")
        print(f"Here is your {coffee}. Enjoy!")
        continue
    elif coffee == "off":
        print("Have a good one!")
        break
    else:
        print("Type the correct word")
        continue