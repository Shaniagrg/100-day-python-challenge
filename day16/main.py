class Machine:
    brand:str = "coffee machine"
    espresso:float = 3.25
    latte:float = 4.50
    cappucino:float = 5.20
    
    @classmethod
    def start_machine(cls,customer_name) -> list[str]:
        #print(f"Hello {customer}!")
        total_coffee:list[str] = []
        customer_got:str = ""
        while True:
            coffee:str = input("Choose between espresso, latte or cappucino: ")
            if coffee == "espresso" or coffee == "latte" or coffee == "cappucino":
                total_coffee.append(coffee)
                customer_got = coffee
                print("Please insert coins.")
                user_money:float = cls.insert_coin()
                change:float = 0.0
                while True:
                    if coffee == "espresso" and user_money > Machine.espresso:
                        change = user_money - cls.espresso
                        break
                    elif coffee == "latte" and user_money > Machine.latte:
                        change = user_money - cls.latte
                        break
                    elif coffee == "cappucino" and user_money > Machine.cappucino:
                        change = user_money - cls.cappucino
                        break
                    else:
                        print("Add more money!")
                        print(f"You have ${user_money}")
                        user_money = cls.insert_coin(user_money)
                        continue
                print(f"Here's your change ${round(change,2)}.")
                print(f"Enjoy your {customer_got} {customer_name}.")
                continue
            elif coffee == "off":
                #print("Have a good one!")
                break
            else:
                print("Type the correct word")
                continue
        return total_coffee
    @classmethod
    def insert_coin(cls, money:float = 0.0)->float:
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
    
customer_records:dict[str,list[str]] = {}
while True:
    customer:str = input("Your name: ")
    if customer == "off":
        break
    else:
        customer_gets:list[str] = Machine.start_machine(customer)
        #print(f"Here is your {customer1_gets}{customer1}. Enjoy!")
        customer_records[customer] = customer_gets
        continue

print(customer_records)
