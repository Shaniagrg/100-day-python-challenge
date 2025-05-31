print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Left or right?")
side:str = input("Type Right/Left: ")
if side == "left":
    print("Nice, you made it to the next level!")
elif side == "right":
    print("Sonic got the treasure before you, try again.")

print("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the sea, pick one.")
sea:str = input("Type Swim/Wait: ")
if sea == "wait":
    print("Nice, you made it to the next level, you're pretty good at this!")
elif sea =="swim":
        print("The end") 

print("Welcome to: TREASURE ISLAND")

print("Now that you've amde it to Treasure Island, you can dig or search the cave.")
cave:str = input("Type Dig/Cave: ")
if cave == "dig":
    print("You've found the treasure, you win!")
elif cave == "cave":
    print("Try again")
     

