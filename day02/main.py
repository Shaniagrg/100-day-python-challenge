print("Welcome to the tip calculator")
total_bill:float=input("What is the total bill amount?")
tip:int=input("How much tip would you like to give?")
people:int=input("How many people to split the bill?")

total_amount:float = total_bill + tip

each_people:int = total_amount/people 
