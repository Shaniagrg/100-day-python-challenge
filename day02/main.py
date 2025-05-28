print("Welcome to the tip calculator")
print("What is the total bill amount?")
total_bill:float = float(input("$: "))

print("How much tip would you like to give?")
tip:int = int(input("Percent: "))

print("How many people to split the bill?")
people:int = int(input("People: "))

#the int(input(promt)) = is the actual assignment of the value to the variable. 
# Here, you are converting the user input (which is a string by default) into an integer.

print(f"Each person should pay: {(total_bill + tip) / people}")
